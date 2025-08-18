import llvmlite.ir as ir
import llvmlite.binding as llvm
import time # Import time module
from ctypes import CFUNCTYPE, c_int # Import c_int for return type

from .parser import (
    ProgramNode,
    PrintNode,
    StringNode,
    IntegerNode,
    FloatNode,
    BinOpNode,
    VariableDeclarationNode,
    VariableAccessNode,
    IfNode,
    FunctionDeclarationNode,
    FunctionCallNode,
    ReturnNode,
    BlockNode,
    ListNode,
    IndexAccessNode,
    IndexAssignmentNode,
    UnaryOpNode,
)
from .lexer import TokenType
from .lexer import TokenType
from .jit_cache import JITCache

# Initialize LLVM


class LLVMCompiler:
    def __init__(self, optimize=True, use_cache=True):
        # Initialize LLVM
        llvm.initialize()
        llvm.initialize_native_target()
        llvm.initialize_native_asmprinter()

        self.module = ir.Module(name="flow_module")
        self.builder = None
        self.functions = {} # Store LLVM functions
        self.variables = {} # Store LLVM variables (pointers to alloca'd memory)
        self.format_strings = {} # Store global format strings
        self.optimize = optimize  # Enable optimization
        self.use_cache = use_cache  # Enable JIT caching

        # Define common types
        self.i32 = ir.IntType(32)
        self.i8_ptr = ir.IntType(8).as_pointer() # Pointer to i8 for strings
        self.void = ir.VoidType()
        self.double = ir.DoubleType() # For numbers

        # Declare external functions (e.g., printf)
        self._declare_external_functions()
        
        # Initialize optimization passes if enabled
        if self.optimize:
            self._initialize_optimization_passes()
            
        # Initialize JIT cache if enabled
        if self.use_cache:
            self.jit_cache = JITCache()
            
    def _initialize_optimization_passes(self):
        """Initialize LLVM optimization passes"""
        # Create a pass manager
        self.pass_manager = llvm.create_module_pass_manager()
        
        # Add common optimization passes (only those available in llvmlite)
        self.pass_manager.add_instruction_combining_pass()
        self.pass_manager.add_gvn_pass()
        self.pass_manager.add_cfg_simplification_pass()
        self.pass_manager.add_dead_code_elimination_pass()
        self.pass_manager.add_global_optimizer_pass()
        self.pass_manager.add_constant_merge_pass()
        
        # Initialize optimization passes if enabled
        if self.optimize:
            self._initialize_optimization_passes()

    def _declare_external_functions(self):
        # Declare printf
        printf_ty = ir.FunctionType(self.i32, [self.i8_ptr], var_arg=True)
        self.printf = ir.Function(self.module, printf_ty, name="printf")
        
        # Declare built-in functions that need to be handled by the runtime
        # For now, we'll handle these in the interpreter/VM rather than as external C functions

    def compile(self, ast_node):
        self.builder = ir.IRBuilder()
        self.visit(ast_node)
        
        # Apply optimization passes if enabled
        if self.optimize:
            self.pass_manager.run(self.module)
            
        return self.module

    

    def visit(self, node):
        method_name = f'visit_{type(node).__name__}'
        visitor_method = getattr(self, method_name, self.no_visit_method)
        return visitor_method(node)

    def no_visit_method(self, node):
        raise Exception(f'No visit_{type(node).__name__} method defined for LLVMCompiler')

    def visit_ProgramNode(self, node):
        # Create a dummy main function for top-level statements
        func_type = ir.FunctionType(self.void, [])
        main_func = ir.Function(self.module, func_type, name="main")
        block = main_func.append_basic_block(name="entry")
        self.builder = ir.IRBuilder(block)

        for statement in node.statements:
            self.visit(statement)
        self.builder.ret_void() # End the main function

    def visit_PrintNode(self, node):
        for value_node in node.values:
            value = self.visit(value_node)
            if isinstance(value.type, ir.DoubleType):
                fmt_name = "fmt_double"
                if fmt_name not in self.format_strings:
                    fmt_str = "%.2f".encode('utf-8')
                    global_fmt = ir.GlobalVariable(self.module, ir.ArrayType(ir.IntType(8), len(fmt_str) + 1), name=fmt_name)
                    global_fmt.initializer = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt_str) + 1), bytearray(fmt_str + b'\0'))
                    global_fmt.linkage = 'private'
                    global_fmt.unnamed_addr = True
                    global_fmt.global_constant = True
                    self.format_strings[fmt_name] = global_fmt
                else:
                    global_fmt = self.format_strings[fmt_name]
                fmt = self.builder.bitcast(global_fmt, self.i8_ptr)
                self.builder.call(self.printf, [fmt, value])
            elif isinstance(value.type, ir.IntType) and value.type.width == 32:
                fmt_name = "fmt_int"
                if fmt_name not in self.format_strings:
                    fmt_str = "%d".encode('utf-8')
                    global_fmt = ir.GlobalVariable(self.module, ir.ArrayType(ir.IntType(8), len(fmt_str) + 1), name=fmt_name)
                    global_fmt.initializer = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt_str) + 1), bytearray(fmt_str + b'\0'))
                    global_fmt.linkage = 'private'
                    global_fmt.unnamed_addr = True
                    global_fmt.global_constant = True
                    self.format_strings[fmt_name] = global_fmt
                else:
                    global_fmt = self.format_strings[fmt_name]
                fmt = self.builder.bitcast(global_fmt, self.i8_ptr)
                self.builder.call(self.printf, [fmt, value])
            elif isinstance(value.type, ir.PointerType) and value.type.pointee == ir.IntType(8):
                fmt_name = "fmt_string"
                if fmt_name not in self.format_strings:
                    fmt_str = "%s".encode('utf-8')
                    global_fmt = ir.GlobalVariable(self.module, ir.ArrayType(ir.IntType(8), len(fmt_str) + 1), name=fmt_name)
                    global_fmt.initializer = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt_str) + 1), bytearray(fmt_str + b'\0'))
                    global_fmt.linkage = 'private'
                    global_fmt.unnamed_addr = True
                    global_fmt.global_constant = True
                    self.format_strings[fmt_name] = global_fmt
                else:
                    global_fmt = self.format_strings[fmt_name]
                fmt = self.builder.bitcast(global_fmt, self.i8_ptr)
                self.builder.call(self.printf, [fmt, value])
            else:
                raise Exception(f"Unsupported type for print: {value.type}")

        # Print a newline character at the end
        fmt_name = "fmt_newline"
        if fmt_name not in self.format_strings:
            fmt_str = "\n".encode('utf-8')
            global_fmt = ir.GlobalVariable(self.module, ir.ArrayType(ir.IntType(8), len(fmt_str) + 1), name=fmt_name)
            global_fmt.initializer = ir.Constant(ir.ArrayType(ir.IntType(8), len(fmt_str) + 1), bytearray(fmt_str + b'\0'))
            global_fmt.linkage = 'private'
            global_fmt.unnamed_addr = True
            global_fmt.global_constant = True
            self.format_strings[fmt_name] = global_fmt
        else:
            global_fmt = self.format_strings[fmt_name]
        fmt = self.builder.bitcast(global_fmt, self.i8_ptr)
        self.builder.call(self.printf, [fmt])

    def visit_IntegerNode(self, node):
        return ir.Constant(self.i32, node.value)

    def visit_FloatNode(self, node):
        return ir.Constant(self.double, node.value)

    def visit_StringNode(self, node):
        # Global string constant
        string_val = node.value.encode('utf-8')
        global_string = ir.GlobalVariable(self.module, ir.ArrayType(ir.IntType(8), len(string_val) + 1), name=f"str_{hash(string_val)}")
        global_string.initializer = ir.Constant(ir.ArrayType(ir.IntType(8), len(string_val) + 1), bytearray(string_val + b'\0'))
        global_string.linkage = 'private'
        global_string.unnamed_addr = True
        global_string.global_constant = True
        return self.builder.bitcast(global_string, self.i8_ptr)

    def visit_BinOpNode(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)

        if isinstance(left.type, ir.DoubleType) and isinstance(right.type, ir.DoubleType):
            if node.op == TokenType.PLUS:
                return self.builder.fadd(left, right, name="addtmp")
            elif node.op == TokenType.MINUS:
                return self.builder.fsub(left, right, name="subtmp")
            elif node.op == TokenType.MULTIPLY:
                return self.builder.fmul(left, right, name="multmp")
            elif node.op == TokenType.DIVIDE:
                return self.builder.fdiv(left, right, name="divtmp")
            elif node.op == TokenType.LESS_THAN:
                return self.builder.fcmp_ordered("<", left, right, name="cmptmp")
        elif isinstance(left.type, ir.IntType) and isinstance(right.type, ir.IntType):
            if node.op == TokenType.PLUS:
                return self.builder.add(left, right, name="addtmp")
            elif node.op == TokenType.MINUS:
                return self.builder.sub(left, right, name="subtmp")
            elif node.op == TokenType.MULTIPLY:
                return self.builder.mul(left, right, name="multmp")
            elif node.op == TokenType.DIVIDE:
                return self.builder.sdiv(left, right, name="divtmp")
            elif node.op == TokenType.LESS_THAN:
                return self.builder.icmp_signed("<", left, right, name="cmptmp")
        else:
            raise Exception(f"Unsupported operand types for binary operation: {left.type} and {right.type}")

    def visit_VariableDeclarationNode(self, node):
        value = self.visit(node.value)
        var_type = value.type
        ptr = self.builder.alloca(var_type, name=node.identifier)
        self.variables[node.identifier] = ptr
        self.builder.store(value, ptr)

    def visit_VariableAccessNode(self, node):
        if node.identifier not in self.variables:
            raise Exception(f"Undefined variable: {node.identifier}")
        ptr = self.variables[node.identifier]
        return self.builder.load(ptr, name=node.identifier)

    def visit_AssignmentNode(self, node):
        if node.identifier not in self.variables:
            raise Exception(f"Undefined variable for assignment: {node.identifier}")
        ptr = self.variables[node.identifier]
        value = self.visit(node.value)
        self.builder.store(value, ptr)

    def visit_IfNode(self, node):
        condition = self.visit(node.condition)
        
        with self.builder.if_else(condition) as (then, otherwise):
            with then:
                self.visit(node.if_block)
            with otherwise:
                if node.else_block:
                    self.visit(node.else_block)

    def visit_WhileNode(self, node):
        # Create basic blocks for loop header, body, and exit
        loop_header_block = self.builder.append_basic_block(name="loop_header")
        loop_body_block = self.builder.append_basic_block(name="loop_body")
        loop_exit_block = self.builder.append_basic_block(name="loop_exit")

        # Branch to loop header
        self.builder.branch(loop_header_block)
        self.builder.position_at_end(loop_header_block)

        # Evaluate condition
        condition = self.visit(node.condition)
        self.builder.cbranch(condition, loop_body_block, loop_exit_block)

        # Loop body
        self.builder.position_at_end(loop_body_block)
        self.visit(node.block)
        self.builder.branch(loop_header_block) # Loop back to header

        # Loop exit
        self.builder.position_at_end(loop_exit_block)

    def visit_FunctionDeclarationNode(self, node):
        param_types = [self.double] * len(node.params)
        func_type = ir.FunctionType(self.double, param_types)
        
        func = ir.Function(self.module, func_type, name=node.name)
        self.functions[node.name] = func

        for i, param_name in enumerate(node.params):
            func.args[i].name = param_name
            ptr = self.builder.alloca(self.double, name=param_name)
            self.builder.store(func.args[i], ptr)
            self.variables[param_name] = ptr

        entry_block = func.append_basic_block(name="entry")
        self.builder.position_at_end(entry_block)

        self.visit(node.body)

        if not self.builder.block.is_terminated:
            self.builder.ret(ir.Constant(self.double, 0.0))

    def visit_FunctionCallNode(self, node):
        if node.name not in self.functions:
            raise Exception(f"Undefined function: {node.name}")
        
        func = self.functions[node.name]
        args = [self.visit(arg) for arg in node.args]
        
        converted_args = []
        for i, arg in enumerate(args):
            if isinstance(func.args[i].type, ir.DoubleType) and isinstance(arg.type, ir.DoubleType):
                converted_args.append(arg)
            else:
                raise Exception(f"Type mismatch for argument {i} in call to {node.name}")

        return self.builder.call(func, converted_args, name="calltmp")

    def visit_ReturnNode(self, node):
        value = self.visit(node.value)
        self.builder.ret(value)

    def visit_BlockNode(self, node):
        for statement in node.statements:
            self.visit(statement)

    def visit_ExternFunctionDeclarationNode(self, node):
        param_types = [self.double] * len(node.params)
        func_type = ir.FunctionType(self.double, param_types)
        ir.Function(self.module, func_type, name=node.name)

    def visit_BuiltinFunctionCallNode(self, node):
        if node.name == "print":
            self.visit_PrintNode(node)
            return
        
        if node.name not in self.functions:
            raise Exception(f"Built-in function {node.name} not declared as external.")
        
        func = self.functions[node.name]
        args = [self.visit(arg) for arg in node.args]
        
        converted_args = []
        for i, arg in enumerate(args):
            if isinstance(func.args[i].type, ir.DoubleType) and isinstance(arg.type, ir.DoubleType):
                converted_args.append(arg)
            else:
                raise Exception(f"Type mismatch for argument {i} in call to built-in {node.name}")
        
        return self.builder.call(func, converted_args, name="builtin_calltmp")

    def visit_ListNode(self, node):
        """Handle list literals"""
        # For now, we'll create a simple array representation
        # In a full implementation, we'd create a more sophisticated list structure
        elements = [self.visit(element) for element in node.elements]
        # Return the first element for now as a placeholder
        # A full implementation would create a proper list structure
        return elements[0] if elements else ir.Constant(self.i32, 0)

    def visit_IndexAccessNode(self, node):
        """Handle index access like arr[0]"""
        # This is a placeholder implementation
        # A full implementation would generate code to access array elements
        obj = self.visit(node.obj)
        index = self.visit(node.index)
        # For now, just return the object itself
        return obj

    def visit_IndexAssignmentNode(self, node):
        """Handle index assignment like arr[0] = value"""
        # This is a placeholder implementation
        # A full implementation would generate code to assign to array elements
        obj = self.visit(node.obj)
        index = self.visit(node.index)
        value = self.visit(node.value)
        # For now, just return the value
        return value

    def visit_UnaryOpNode(self, node):
        """Handle unary operations like -x"""
        operand = self.visit(node.operand)
        if node.op == TokenType.MINUS:
            if isinstance(operand.type, ir.DoubleType):
                return self.builder.fsub(ir.Constant(self.double, 0.0), operand, name="negtmp")
            elif isinstance(operand.type, ir.IntType):
                return self.builder.sub(ir.Constant(self.i32, 0), operand, name="negtmp")
        # Add more unary operations as needed
        raise Exception(f"Unsupported unary operation: {node.op}")
