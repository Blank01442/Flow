from .bytecode import OpCode, CompareOp
from . import builtins
from .profiler import global_profiler, profile_block
import time

# Import AST nodes
from .parser import (
    ProgramNode, PrintNode, StringNode, IntegerNode, FloatNode, BooleanNode, BinOpNode,
    VariableDeclarationNode, VariableAccessNode, AssignmentNode, IfNode,
    WhileNode, FunctionDeclarationNode, FunctionCallNode, ReturnNode,
    BlockNode, ExternFunctionDeclarationNode, BuiltinFunctionCallNode,
    ListNode, IndexAccessNode, IndexAssignmentNode, UnaryOpNode
)
from .lexer import TokenType

class Frame:
    __slots__ = ['code_obj', 'ip', 'stack', 'locals', 'globals']
    
    def __init__(self, code_obj, globals):
        self.code_obj = code_obj
        self.ip = 0
        self.stack = []
        self.locals = [None] * code_obj.get('num_locals', 0) # Initialize locals as a list
        self.globals = globals

class VM:
    def __init__(self):
        self.frames = []
        self.globals = {}
        # Pre-compile instruction handlers for better performance
        self._instruction_handlers = self._build_instruction_handlers()
        self.profiler = global_profiler
        self._method_cache = {}  # Cache for visitor methods

    def _build_instruction_handlers(self):
        """Build instruction handler dispatch table for better performance"""
        return {
            OpCode.LOAD_CONST: self._handle_load_const,
            OpCode.STORE_NAME: self._handle_store_name,
            OpCode.LOAD_NAME: self._handle_load_name,
            OpCode.LOAD_FAST: self._handle_load_fast,
            OpCode.STORE_FAST: self._handle_store_fast,
            OpCode.BINARY_ADD: self._handle_binary_add,
            OpCode.BINARY_SUBTRACT: self._handle_binary_subtract,
            OpCode.BINARY_MULTIPLY: self._handle_binary_multiply,
            OpCode.BINARY_DIVIDE: self._handle_binary_divide,
            OpCode.PRINT: self._handle_print,
            OpCode.JUMP_IF_FALSE: self._handle_jump_if_false,
            OpCode.JUMP: self._handle_jump,
            OpCode.RETURN_VALUE: self._handle_return_value,
            OpCode.CALL_FUNCTION: self._handle_call_function,
            OpCode.CALL_BUILTIN: self._handle_call_builtin,
            OpCode.COMPARE_OP: self._handle_compare_op,
        }

    def run(self, bytecode, constants):
        # For AST nodes, we'll directly interpret them
        if hasattr(bytecode, '__iter__') and not isinstance(bytecode, (str, bytes)):
            # This is a list of AST nodes
            for node in bytecode:
                self.visit(node)
        else:
            # Original bytecode execution
            code_obj = {'bytecode': bytecode, 'constants': constants, 'params': [], 'num_locals': 0}
            frame = Frame(code_obj, self.globals)
            self.frames.append(frame)
            return self.execute_frame(frame)

    def execute_frame(self, frame):
        bytecode = frame.code_obj['bytecode']
        constants = frame.code_obj['constants']
        bytecode_len = len(bytecode)
        
        # Profile the execution if profiler is active
        start_time = None
        if self.profiler.start_time is not None:
            start_time = time.time()
            
        while frame.ip < bytecode_len:
            instruction = bytecode[frame.ip]
            opcode = instruction[0]
            operand = instruction[1] if len(instruction) > 1 else None
            frame.ip += 1

            # Use dispatch table for better performance
            handler = self._instruction_handlers.get(opcode)
            if handler:
                handler(frame, operand, constants)
            else:
                raise Exception(f"Unknown opcode: {opcode}")
        
        # Record execution time if profiler is active
        if start_time is not None and self.profiler.start_time is not None:
            elapsed_time = time.time() - start_time
            # Try to get function name for more meaningful profiling
            func_name = "unknown_function"
            if 'constants' in frame.code_obj and len(frame.code_obj['constants']) > 0:
                # This is a heuristic - in real implementation we'd need better tracking
                func_name = f"function_at_ip_{frame.ip}"
            self.profiler.record_function_time(func_name, elapsed_time)
        
        return None

    def visit(self, node):
        # Use cached method lookup for better performance
        method_name = f'visit_{type(node).__name__}'
        if method_name in self._method_cache:
            method = self._method_cache[method_name]
        else:
            method = getattr(self, method_name, self.no_visit_method)
            self._method_cache[method_name] = method
        return method(node)

    def no_visit_method(self, node):
        raise Exception(f'No visit_{type(node).__name__} method defined')

    def visit_ProgramNode(self, node):
        for statement in node.statements:
            self.visit(statement)

    def visit_PrintNode(self, node):
        values = []
        for value_node in node.values:
            value = self.visit(value_node)
            values.append(str(value))
        print(' '.join(values))

    def visit_StringNode(self, node):
        return node.value

    def visit_BooleanNode(self, node):
        return node.value

    def visit_IntegerNode(self, node):
        return node.value

    def visit_FloatNode(self, node):
        return node.value

    def visit_BinOpNode(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        
        if node.op == TokenType.PLUS:
            return left + right
        elif node.op == TokenType.MINUS:
            return left - right
        elif node.op == TokenType.MULTIPLY:
            return left * right
        elif node.op == TokenType.DIVIDE:
            return left / right
        elif node.op == TokenType.LESS_THAN:
            return left < right
        elif node.op == TokenType.GREATER_THAN:
            return left > right
        elif node.op == TokenType.EQUAL_EQUAL:
            return left == right
        elif node.op == TokenType.NOT_EQUALS:
            return left != right
        elif node.op == TokenType.LESS_EQUAL:
            return left <= right
        elif node.op == TokenType.GREATER_EQUAL:
            return left >= right
        else:
            raise Exception(f"Unsupported binary operation: {node.op}")

    def visit_VariableDeclarationNode(self, node):
        value = self.visit(node.value)
        self.globals[node.identifier] = value

    def visit_VariableAccessNode(self, node):
        if node.identifier in self.globals:
            return self.globals[node.identifier]
        else:
            raise NameError(f"Name '{node.identifier}' is not defined")

    def visit_AssignmentNode(self, node):
        value = self.visit(node.value)
        self.globals[node.identifier] = value

    def visit_IfNode(self, node):
        condition = self.visit(node.condition)
        if condition:
            self.visit(node.if_block)
        elif node.else_block:
            self.visit(node.else_block)

    def visit_WhileNode(self, node):
        while self.visit(node.condition):
            self.visit(node.block)

    def visit_FunctionDeclarationNode(self, node):
        # Store the function definition in globals
        self.globals[node.name] = node

    def visit_FunctionCallNode(self, node):
        if node.name not in self.globals:
            raise NameError(f"Function '{node.name}' is not defined")
            
        func_def = self.globals[node.name]
        if not isinstance(func_def, FunctionDeclarationNode):
            raise TypeError(f"'{node.name}' is not a function")
            
        # Evaluate arguments
        args = [self.visit(arg) for arg in node.args]
        
        # Create new frame for function execution
        # For simplicity, we'll just add the arguments to globals
        # A full implementation would use proper scoping
        old_globals = self.globals.copy()
        for i, param in enumerate(func_def.params):
            if i < len(args):
                self.globals[param] = args[i]
            else:
                self.globals[param] = None
                
        # Execute function body
        result = None
        try:
            self.visit(func_def.body)
        except ReturnException as e:
            result = e.value
            
        # Restore globals
        self.globals = old_globals
        return result

    def visit_ReturnNode(self, node):
        value = self.visit(node.value)
        raise ReturnException(value)

    def visit_BlockNode(self, node):
        for statement in node.statements:
            self.visit(statement)

    def visit_BuiltinFunctionCallNode(self, node):
        # Get the function from builtins module
        func = getattr(builtins, node.name, None)
        if func is None:
            raise NameError(f"Built-in function '{node.name}' is not defined")
            
        # Evaluate arguments
        args = [self.visit(arg) for arg in node.args]
        
        # Call the function
        return func(*args)

    def visit_ListNode(self, node):
        """Handle list literals"""
        elements = [self.visit(element) for element in node.elements]
        return elements

    def visit_IndexAccessNode(self, node):
        """Handle index access like arr[0]"""
        obj = self.visit(node.obj)
        index = self.visit(node.index)
        return obj[index]

    def visit_IndexAssignmentNode(self, node):
        """Handle index assignment like arr[0] = value"""
        obj = self.visit(node.obj)
        index = self.visit(node.index)
        value = self.visit(node.value)
        obj[index] = value
        return value

    def visit_UnaryOpNode(self, node):
        """Handle unary operations like -x"""
        operand = self.visit(node.operand)
        if node.op == TokenType.MINUS:
            return -operand
        # Add more unary operations as needed
        raise Exception(f"Unsupported unary operation: {node.op}")

    # Bytecode execution handlers (kept for backward compatibility)
    def _handle_load_const(self, frame, operand, constants):
        frame.stack.append(constants[operand])

    def _handle_store_name(self, frame, operand, constants):
        name = constants[operand]
        value = frame.stack.pop()
        self.globals[name] = value

    def _handle_load_name(self, frame, operand, constants):
        name = constants[operand]
        if name in frame.globals:
            frame.stack.append(frame.globals[name])
        else:
            raise NameError(f"name '{name}' is not defined")

    def _handle_load_fast(self, frame, operand, constants):
        frame.stack.append(frame.locals[operand])

    def _handle_store_fast(self, frame, operand, constants):
        value = frame.stack.pop()
        frame.locals[operand] = value

    def _handle_binary_add(self, frame, operand, constants):
        right = frame.stack.pop()
        left = frame.stack.pop()
        frame.stack.append(left + right)

    def _handle_binary_subtract(self, frame, operand, constants):
        right = frame.stack.pop()
        left = frame.stack.pop()
        frame.stack.append(left - right)

    def _handle_binary_multiply(self, frame, operand, constants):
        right = frame.stack.pop()
        left = frame.stack.pop()
        frame.stack.append(left * right)

    def _handle_binary_divide(self, frame, operand, constants):
        right = frame.stack.pop()
        left = frame.stack.pop()
        frame.stack.append(left / right)

    def _handle_print(self, frame, operand, constants):
        value = frame.stack.pop()
        print(value)

    def _handle_jump_if_false(self, frame, operand, constants):
        condition = frame.stack.pop()
        if not condition:
            frame.ip = operand

    def _handle_jump(self, frame, operand, constants):
        frame.ip = operand

    def _handle_return_value(self, frame, operand, constants):
        return frame.stack.pop()

    def _handle_call_function(self, frame, operand, constants):
        num_args = operand
        args = [frame.stack.pop() for _ in range(num_args)]
        args.reverse()
        func = frame.stack.pop()

        if isinstance(func, dict) and 'bytecode' in func:
            new_frame = Frame(func, self.globals)
            # Initialize locals for the new frame
            new_frame.locals = [None] * func['num_locals']
            # Assign parameters to locals using their indices
            for i, param_name in enumerate(func['params']):
                # The compiler ensures that parameters are assigned to local slots
                # in the order they appear in func['params'].
                # Therefore, the i-th parameter corresponds to the i-th local slot.
                new_frame.locals[i] = args[i]
            
            # Push the new frame onto the call stack
            self.frames.append(new_frame)
            result = self.execute_frame(new_frame)
            self.frames.pop()
            frame.stack.append(result)
        else:
            raise TypeError(f"'{type(func).__name__}' object is not callable")

    def _handle_call_builtin(self, frame, operand, constants):
        func_name = constants[operand]
        num_args = frame.stack.pop()
        args = [frame.stack.pop() for _ in range(num_args)]
        args.reverse()

        builtin_func = getattr(builtins, func_name, None)
        if builtin_func:
            result = builtin_func(*args)
            if result is not None:
                frame.stack.append(result)
        else:
            raise Exception(f"Built-in function '{func_name}' not found")

    def _handle_compare_op(self, frame, operand, constants):
        right = frame.stack.pop()
        left = frame.stack.pop()
        if operand == CompareOp.LESS_THAN:
            frame.stack.append(left < right)
        elif operand == CompareOp.LESS_EQUAL:
            frame.stack.append(left <= right)
        elif operand == CompareOp.EQUAL:
            frame.stack.append(left == right)
        elif operand == CompareOp.NOT_EQUAL:
            frame.stack.append(left != right)
        elif operand == CompareOp.GREATER_THAN:
            frame.stack.append(left > right)
        elif operand == CompareOp.GREATER_EQUAL:
            frame.stack.append(left >= right)
        elif operand == CompareOp.GREATER_THAN_OR_EQUAL:
            frame.stack.append(left >= right)
        elif operand == CompareOp.LESS_THAN_OR_EQUAL:
            frame.stack.append(left <= right)

# Exception for handling return statements
class ReturnException(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__()