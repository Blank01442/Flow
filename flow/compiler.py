
from .parser import (ProgramNode, PrintNode, StringNode, NumberNode, 
                     BinOpNode, VariableDeclarationNode, VariableAccessNode,
                     IfNode, FunctionDeclarationNode, FunctionCallNode, ReturnNode, BlockNode)
from .lexer import TokenType
from .bytecode import OpCode, CompareOp

class Compiler:
    def __init__(self):
        self.bytecode = []
        self.constants = []
        self._constant_cache = {}  # Cache for constant lookups
        self._method_cache = {}    # Cache for visitor methods
        self._locals_stack = [{}] # Stack of dictionaries for local variables (name -> index)
        self._local_count_stack = [0] # Stack of counts for local variables

    def compile(self, node):
        self.visit(node)
        return self.bytecode, self.constants

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
        self.visit(node.value)
        self.emit(OpCode.PRINT)

    def visit_StringNode(self, node):
        self.emit(OpCode.LOAD_CONST, self.add_constant(node.value))

    def visit_NumberNode(self, node):
        self.emit(OpCode.LOAD_CONST, self.add_constant(node.value))

    def visit_BinOpNode(self, node):
        self.visit(node.left)
        self.visit(node.right)
        
        # Use direct opcode mapping for better performance
        opcode_map = {
            TokenType.PLUS: OpCode.BINARY_ADD,
            TokenType.MINUS: OpCode.BINARY_SUBTRACT,
            TokenType.MULTIPLY: OpCode.BINARY_MULTIPLY,
            TokenType.DIVIDE: OpCode.BINARY_DIVIDE,
            TokenType.LESS_THAN: OpCode.COMPARE_OP,
        }
        
        opcode = opcode_map.get(node.op)
        if opcode == OpCode.COMPARE_OP:
            self.emit(opcode, CompareOp.LESS_THAN)
        else:
            self.emit(opcode)

    def visit_VariableDeclarationNode(self, node):
        self.visit(node.value)
        if len(self._locals_stack) > 1: # Inside a function
            current_locals = self._locals_stack[-1]
            current_local_count = self._local_count_stack[-1]
            if node.identifier not in current_locals:
                current_locals[node.identifier] = current_local_count
                self._local_count_stack[-1] += 1
            self.emit(OpCode.STORE_FAST, current_locals[node.identifier])
        else: # Global scope
            self.emit(OpCode.STORE_NAME, self.add_constant(node.identifier))

    def visit_VariableAccessNode(self, node):
        # Check if it's a local variable in the current scope or any enclosing scope
        for locals_scope in reversed(self._locals_stack):
            if node.identifier in locals_scope:
                self.emit(OpCode.LOAD_FAST, locals_scope[node.identifier])
                return
        # If not found in local scopes, assume it's a global
        self.emit(OpCode.LOAD_NAME, self.add_constant(node.identifier))

    def visit_IfNode(self, node):
        self.visit(node.condition)
        # Jump to else block if condition is false
        jump_if_false_pos = self.emit(OpCode.JUMP_IF_FALSE, -1) 
        self.visit(node.if_block)
        # Jump over else block
        jump_pos = self.emit(OpCode.JUMP, -1)
        # Set the jump target for the if statement
        self.bytecode[jump_if_false_pos] = (OpCode.JUMP_IF_FALSE, len(self.bytecode))
        if node.else_block:
            self.visit(node.else_block)
        # Set the jump target for the else statement
        self.bytecode[jump_pos] = (OpCode.JUMP, len(self.bytecode))

    def visit_WhileNode(self, node):
        loop_start_pos = len(self.bytecode) # Mark the beginning of the loop
        self.visit(node.condition)
        jump_if_false_pos = self.emit(OpCode.JUMP_IF_FALSE, -1) # Jump out if condition is false
        self.visit(node.block)
        self.emit(OpCode.JUMP, loop_start_pos) # Jump back to the beginning of the loop
        self.bytecode[jump_if_false_pos] = (OpCode.JUMP_IF_FALSE, len(self.bytecode)) # Set jump target to after the loop

    def visit_FunctionDeclarationNode(self, node):
        # Push a new local scope
        self._locals_stack.append({})
        self._local_count_stack.append(0)

        # Handle parameters as initial local variables
        current_locals = self._locals_stack[-1]
        current_local_count = self._local_count_stack[-1]
        for param in node.params:
            current_locals[param] = current_local_count
            current_local_count += 1
        self._local_count_stack[-1] = current_local_count

        # Compile the function body
        compiler = Compiler()
        compiler.compile(node.body)
        func_bytecode, func_constants = compiler.bytecode, compiler.constants

        # Get local variable names in order of their indices
        local_names = [None] * self._local_count_stack[-1]
        for name, index in self._locals_stack[-1].items():
            local_names[index] = name

        # Create a code object for the function
        code_obj = {
            'bytecode': func_bytecode,
            'constants': func_constants,
            'params': node.params,
            'num_locals': self._local_count_stack[-1], # Number of local variables
            'local_names': local_names # Names of local variables in order of indices
        }
        # Store the code object as a constant
        self.emit(OpCode.LOAD_CONST, self.add_constant(code_obj))
        self.emit(OpCode.STORE_NAME, self.add_constant(node.name))

        # Pop the local scope
        self._locals_stack.pop()
        self._local_count_stack.pop()

    def visit_FunctionCallNode(self, node):
        # Load the function
        self.emit(OpCode.LOAD_NAME, self.add_constant(node.name))
        # Load the arguments
        for arg in node.args:
            self.visit(arg)
        # Call the function
        self.emit(OpCode.CALL_FUNCTION, len(node.args))

    def visit_ReturnNode(self, node):
        self.visit(node.value)
        self.emit(OpCode.RETURN_VALUE)

    def visit_BuiltinFunctionCallNode(self, node):
        # Load the arguments
        for arg in node.args:
            self.visit(arg)
        # Push the number of arguments
        self.emit(OpCode.LOAD_CONST, self.add_constant(len(node.args)))
        # Call the built-in function
        self.emit(OpCode.CALL_BUILTIN, self.add_constant(node.name))

    def visit_BlockNode(self, node):
        for statement in node.statements:
            self.visit(statement)

    def add_constant(self, value):
        # Check if the value is already in the cache
        if value in self._constant_cache:
            return self._constant_cache[value]

        # If not in cache, it's a new constant
        # Add it to the list of constants and get its index
        index = len(self.constants)
        self.constants.append(value)

        # Store the value and its index in the cache
        self._constant_cache[value] = index
        return index

    def emit(self, opcode, operand=None):
        if operand is not None:
            instruction = (opcode, operand)
        else:
            instruction = (opcode,)
        
        self.bytecode.append(instruction)
        return len(self.bytecode) - 1
