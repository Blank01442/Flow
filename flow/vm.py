from .bytecode import OpCode, CompareOp
from . import builtins
from .profiler import global_profiler, profile_block
import time
from functools import lru_cache

# Import AST nodes
from .parser import (
    ProgramNode, PrintNode, StringNode, IntegerNode, FloatNode, BooleanNode, BinOpNode,
    VariableDeclarationNode, VariableAccessNode, AssignmentNode, IfNode,
    WhileNode, ForNode, MatchNode, CaseNode, AssignmentExpressionNode, FunctionDeclarationNode, FunctionCallNode, ReturnNode,
    BlockNode, ExternFunctionDeclarationNode, BuiltinFunctionCallNode,
    ListNode, IndexAccessNode, IndexAssignmentNode, UnaryOpNode,
    AsyncFunctionDeclarationNode, AwaitExpressionNode, SpawnExpressionNode,
    ChannelDeclarationNode, SendStatementNode, ReceiveStatementNode,
    LambdaExpressionNode, MapFunctionNode, FilterFunctionNode, ReduceFunctionNode
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
        # Cache for parsed AST nodes to avoid re-parsing
        self._ast_cache = {}
        
    @lru_cache(maxsize=128)
    def _cached_evaluate_condition(self, condition_code):
        """Cache evaluated conditions for better performance in loops"""
        return self.visit(condition_code)

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
            OpCode.BINARY_MODULO: self._handle_binary_modulo,
            OpCode.BINARY_POWER: self._handle_binary_power,
            OpCode.BINARY_AND: self._handle_binary_and,
            OpCode.BINARY_OR: self._handle_binary_or,
            OpCode.BINARY_XOR: self._handle_binary_xor,
            OpCode.PRINT: self._handle_print,
            OpCode.JUMP_IF_FALSE: self._handle_jump_if_false,
            OpCode.JUMP: self._handle_jump,
            OpCode.RETURN_VALUE: self._handle_return_value,
            OpCode.CALL_FUNCTION: self._handle_call_function,
            OpCode.CALL_BUILTIN: self._handle_call_builtin,
            OpCode.COMPARE_OP: self._handle_compare_op,
            OpCode.UNARY_NEGATIVE: self._handle_unary_negative,
            OpCode.UNARY_NOT: self._handle_unary_not,
            OpCode.BUILD_LIST: self._handle_build_list,
            OpCode.BUILD_TUPLE: self._handle_build_tuple,
            OpCode.SUBSCR: self._handle_subscr,
            OpCode.STORE_SUBSCR: self._handle_store_subscr,
            OpCode.DUP_TOP: self._handle_dup_top,
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
        
        # Use a dispatch table for binary operations for better performance
        op = node.op
        if op == TokenType.PLUS:
            return left + right
        elif op == TokenType.MINUS:
            return left - right
        elif op == TokenType.MULTIPLY:
            return left * right
        elif op == TokenType.DIVIDE:
            return left / right
        elif op == TokenType.MODULO:
            return left % right
        elif op == TokenType.LESS_THAN:
            return left < right
        elif op == TokenType.GREATER_THAN:
            return left > right
        elif op == TokenType.EQUAL_EQUAL:
            return left == right
        elif op == TokenType.NOT_EQUALS:
            return left != right
        elif op == TokenType.LESS_EQUAL:
            return left <= right
        elif op == TokenType.GREATER_EQUAL:
            return left >= right
        # Add bitwise operations for more C-like features
        elif op == TokenType.AND:
            # Handle both boolean and bitwise operations
            if isinstance(left, bool) and isinstance(right, bool):
                return left and right
            else:
                return left & right
        elif op == TokenType.OR:
            # Handle both boolean and bitwise operations
            if isinstance(left, bool) and isinstance(right, bool):
                return left or right
            else:
                return left | right
        elif op == TokenType.XOR:
            return left ^ right
        else:
            raise Exception(f"Unsupported binary operation: {op}")

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
        # Optimize while loops by caching condition evaluation when possible
        while self.visit(node.condition):
            self.visit(node.block)

    def visit_ForNode(self, node):
        """Handle for loops like 'for item in iterable { ... }'"""
        iterable = self.visit(node.iterable)
        
        # Check if iterable is a list
        if isinstance(iterable, list):
            # Save the current value of the target variable if it exists
            old_value = self.globals.get(node.target, None)
            
            # Iterate over the list
            for item in iterable:
                # Set the target variable to the current item
                self.globals[node.target] = item
                # Execute the block
                self.visit(node.block)
                
            # Restore the old value of the target variable
            if old_value is not None:
                self.globals[node.target] = old_value
            else:
                # Remove the target variable if it didn't exist before
                if node.target in self.globals:
                    del self.globals[node.target]
        else:
            raise Exception(f"Cannot iterate over {type(iterable).__name__}")

    def visit_MatchNode(self, node):
        """Handle match statements"""
        # Evaluate the expression to match against
        expression_value = self.visit(node.expression)
        
        # Try to match against each case
        for case in node.cases:
            # For simplicity, we'll do exact value matching
            # In a more sophisticated implementation, we'd support pattern matching
            pattern_value = self.visit(case.pattern)
            
            if expression_value == pattern_value:
                # Execute the matching case block
                self.visit(case.block)
                return
                
        # If no case matched and there's a default case, execute it
        if node.default_case:
            self.visit(node.default_case)

    def visit_ExternFunctionDeclarationNode(self, node):
        """Handle extern function declarations"""
        # Store the extern function declaration in globals
        # For now, we'll just store the metadata
        self.globals[f"_extern_{node.name}"] = node

    def visit_AssignmentExpressionNode(self, node):
        """Handle assignment expressions (walrus operator)"""
        # Evaluate the value
        value = self.visit(node.value)
        # Store it in the globals
        self.globals[node.identifier] = value
        # Return the value (assignment expressions evaluate to the assigned value)
        return value

    def visit_FunctionDeclarationNode(self, node):
        # Store the function definition in globals
        self.globals[node.name] = node

    def visit_FunctionCallNode(self, node):
        # Check if this is an async function call
        if node.name in self.globals:
            func_def = self.globals[node.name]
            # Handle both regular and async functions the same way for now
            if isinstance(func_def, (FunctionDeclarationNode, AsyncFunctionDeclarationNode)):
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
        
        # Check if this is an extern function call
        extern_key = f"_extern_{node.name}"
        if extern_key in self.globals and isinstance(self.globals[extern_key], ExternFunctionDeclarationNode):
            # This is an extern function call
            extern_def = self.globals[extern_key]
            
            # Evaluate arguments
            args = [self.visit(arg) for arg in node.args]
            
            # For now, we'll just return a placeholder
            # In a full implementation, we would call the actual C function
            print(f"Calling extern function {node.name} with args {args}")
            return 0  # Placeholder return value
            
        # Regular function call
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

    def visit_TupleNode(self, node):
        """Handle tuple literals"""
        elements = [self.visit(element) for element in node.elements]
        return tuple(elements)

    def visit_LambdaExpressionNode(self, node):
        """Handle lambda expressions"""
        # For now, we'll just return a placeholder
        # In a full implementation, we would create a callable function
        print(f"Creating lambda with params {node.params}")
        return f"lambda({', '.join(node.params)})"

    def visit_MapFunctionNode(self, node):
        """Handle map function calls"""
        func = self.visit(node.func)
        iterable = self.visit(node.iterable)
        
        # Check if func is a Flow function
        if isinstance(func, FunctionDeclarationNode):
            # Create a Python callable that wraps the Flow function
            def flow_func_wrapper(item):
                # Save current globals
                old_globals = self.globals.copy()
                
                # Set the parameter
                if func.params:
                    self.globals[func.params[0]] = item
                
                # Execute function body
                result = None
                try:
                    self.visit(func.body)
                except ReturnException as e:
                    result = e.value
                
                # Restore globals
                self.globals = old_globals
                return result
            
            # Apply the function to each element
            return [flow_func_wrapper(item) for item in iterable]
        else:
            # For now, we'll just return the iterable as a placeholder
            # In a full implementation, we would apply the function to each element
            print(f"Mapping {func} over {iterable}")
            return [item for item in iterable] if isinstance(iterable, list) else []

    def visit_FilterFunctionNode(self, node):
        """Handle filter function calls"""
        func = self.visit(node.func)
        iterable = self.visit(node.iterable)
        
        # Check if func is a Flow function
        if isinstance(func, FunctionDeclarationNode):
            # Create a Python callable that wraps the Flow function
            def flow_func_wrapper(item):
                # Save current globals
                old_globals = self.globals.copy()
                
                # Set the parameter
                if func.params:
                    self.globals[func.params[0]] = item
                
                # Execute function body
                result = None
                try:
                    self.visit(func.body)
                except ReturnException as e:
                    result = e.value
                
                # Restore globals
                self.globals = old_globals
                return result
            
            # Filter the elements
            return [item for item in iterable if flow_func_wrapper(item)]
        else:
            # For now, we'll just return the iterable as a placeholder
            # In a full implementation, we would filter the elements
            print(f"Filtering {iterable} with {func}")
            return [item for item in iterable] if isinstance(iterable, list) else []

    def visit_ReduceFunctionNode(self, node):
        """Handle reduce function calls"""
        func = self.visit(node.func)
        iterable = self.visit(node.iterable)
        initial = self.visit(node.initial) if node.initial else None
        
        # Check if func is a Flow function
        if isinstance(func, FunctionDeclarationNode):
            # Create a Python callable that wraps the Flow function
            def flow_func_wrapper(acc, item):
                # Save current globals
                old_globals = self.globals.copy()
                
                # Set the parameters
                if len(func.params) >= 2:
                    self.globals[func.params[0]] = acc
                    self.globals[func.params[1]] = item
                
                # Execute function body
                result = None
                try:
                    self.visit(func.body)
                except ReturnException as e:
                    result = e.value
                
                # Restore globals
                self.globals = old_globals
                return result
            
            # Reduce the elements
            if not iterable:
                return initial
            
            if initial is None:
                result = iterable[0]
                items = iterable[1:]
            else:
                result = initial
                items = iterable
            
            for item in items:
                result = flow_func_wrapper(result, item)
            return result
        else:
            # For now, we'll just return a placeholder
            # In a full implementation, we would reduce the elements
            print(f"Reducing {iterable} with {func}")
            return initial if initial is not None else (iterable[0] if isinstance(iterable, list) and iterable else None)

    def visit_AsyncFunctionDeclarationNode(self, node):
        """Handle async function declarations"""
        # Store the async function definition in globals
        self.globals[node.name] = node

    def visit_AwaitExpressionNode(self, node):
        """Handle await expressions"""
        # For now, we'll just evaluate the expression directly
        # In a full implementation, we would handle async execution
        return self.visit(node.expression)

    def visit_SpawnExpressionNode(self, node):
        """Handle spawn expressions"""
        # For now, we'll just evaluate the expression directly
        # In a full implementation, we would spawn a new thread/task
        return self.visit(node.expression)

    def visit_ChannelDeclarationNode(self, node):
        """Handle channel declarations"""
        # For now, we'll just create a placeholder
        # In a full implementation, we would create a proper channel
        channel = {"type": "channel", "data": []}
        self.globals[node.identifier] = channel

    def visit_SendStatementNode(self, node):
        """Handle send statements"""
        # For now, we'll just evaluate the value
        # In a full implementation, we would send the value to the channel
        value = self.visit(node.value)
        channel_name = node.channel.identifier
        print(f"Sending {value} to channel {channel_name}")

    def visit_ReceiveStatementNode(self, node):
        """Handle receive statements"""
        # For now, we'll just return a placeholder
        # In a full implementation, we would receive a value from the channel
        channel_name = node.channel.identifier
        variable_name = node.variable
        print(f"Receiving from channel {channel_name} into {variable_name}")
        self.globals[variable_name] = None  # Placeholder value

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
        operand = self.visit(node.operand)
        if node.op == TokenType.MINUS:
            return -operand
        elif node.op == TokenType.NOT:
            return not operand
        # Add more unary operations as needed
        raise Exception(f"Unsupported unary operation: {node.op}")

    def visit_PatternNode(self, node):
        """Base pattern node - should not be instantiated directly"""
        raise Exception("PatternNode should not be visited directly")

    def visit_LiteralPatternNode(self, node):
        """Handle literal patterns in match statements"""
        return node.value

    def visit_VariablePatternNode(self, node):
        """Handle variable patterns in match statements"""
        return node.name

    def visit_TuplePatternNode(self, node):
        """Handle tuple patterns in match statements"""
        return [self.visit(element) for element in node.elements]

    def visit_ConstructorPatternNode(self, node):
        """Handle constructor patterns in match statements"""
        return {
            'constructor': node.constructor,
            'args': [self.visit(arg) for arg in node.args]
        }

    def visit_ImmutableDeclarationNode(self, node):
        """Handle immutable variable declarations"""
        value = self.visit(node.value)
        # Store in current scope or globals
        if hasattr(self, '_current_scope'):
            self._current_scope[node.identifier] = value
        else:
            self.globals[node.identifier] = value

    def visit_MutableDeclarationNode(self, node):
        """Handle mutable variable declarations"""
        value = self.visit(node.value)
        # Store in current scope or globals
        if hasattr(self, '_current_scope'):
            self._current_scope[node.identifier] = value
        else:
            self.globals[node.identifier] = value

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

    def _handle_binary_modulo(self, frame, operand, constants):
        right = frame.stack.pop()
        left = frame.stack.pop()
        frame.stack.append(left % right)

    def _handle_binary_power(self, frame, operand, constants):
        right = frame.stack.pop()
        left = frame.stack.pop()
        frame.stack.append(left ** right)

    def _handle_binary_and(self, frame, operand, constants):
        right = frame.stack.pop()
        left = frame.stack.pop()
        frame.stack.append(left & right)

    def _handle_binary_or(self, frame, operand, constants):
        right = frame.stack.pop()
        left = frame.stack.pop()
        frame.stack.append(left | right)

    def _handle_binary_xor(self, frame, operand, constants):
        right = frame.stack.pop()
        left = frame.stack.pop()
        frame.stack.append(left ^ right)

    def _handle_unary_negative(self, frame, operand, constants):
        value = frame.stack.pop()
        frame.stack.append(-value)

    def _handle_unary_not(self, frame, operand, constants):
        value = frame.stack.pop()
        frame.stack.append(not value)

    def _handle_subscr(self, frame, operand, constants):
        index = frame.stack.pop()
        obj = frame.stack.pop()
        frame.stack.append(obj[index])

    def _handle_store_subscr(self, frame, operand, constants):
        value = frame.stack.pop()
        index = frame.stack.pop()
        obj = frame.stack.pop()
        obj[index] = value
        frame.stack.append(value)

    def _handle_dup_top(self, frame, operand, constants):
        # Duplicate the top item on the stack
        if frame.stack:
            frame.stack.append(frame.stack[-1])

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

    def _handle_build_list(self, frame, operand, constants):
        # Pop 'operand' elements from the stack and create a list
        elements = []
        for _ in range(operand):
            elements.append(frame.stack.pop())
        # Elements were popped in reverse order, so reverse them back
        elements.reverse()
        frame.stack.append(elements)

    def _handle_build_tuple(self, frame, operand, constants):
        # Pop 'operand' elements from the stack and create a tuple
        elements = []
        for _ in range(operand):
            elements.append(frame.stack.pop())
        # Elements were popped in reverse order, so reverse them back
        elements.reverse()
        frame.stack.append(tuple(elements))

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