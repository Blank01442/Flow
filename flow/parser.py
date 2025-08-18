from .lexer import TokenType
from .builtins import BUILTINS

# --- AST Nodes ---
class ASTNode:
    pass

class ProgramNode(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class PrintNode(ASTNode):
    def __init__(self, values):
        self.values = values

class StringNode(ASTNode):
    def __init__(self, value):
        self.value = value

class IntegerNode(ASTNode):
    def __init__(self, value):
        self.value = int(value)

class FloatNode(ASTNode):
    def __init__(self, value):
        self.value = float(value)

class BooleanNode(ASTNode):
    def __init__(self, value):
        self.value = value == "true"

class BinOpNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
        self.op = op
        self.right = right

class VariableDeclarationNode(ASTNode):
    def __init__(self, identifier, value):
        self.identifier = identifier
        self.value = value

class VariableAccessNode(ASTNode):
    def __init__(self, identifier):
        self.identifier = identifier

class AssignmentNode(ASTNode):
    def __init__(self, identifier, value):
        self.identifier = identifier
        self.value = value

class IfNode(ASTNode):
    def __init__(self, condition, if_block, else_block=None):
        self.condition = condition
        self.if_block = if_block
        self.else_block = else_block

class WhileNode(ASTNode):
    def __init__(self, condition, block):
        self.condition = condition
        self.block = block

class ForNode(ASTNode):
    def __init__(self, target, iterable, block):
        self.target = target
        self.iterable = iterable
        self.block = block

class FunctionDeclarationNode(ASTNode):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

class FunctionCallNode(ASTNode):
    def __init__(self, name, args):
        self.name = name
        self.args = args

class ReturnNode(ASTNode):
    def __init__(self, value):
        self.value = value

class BlockNode(ASTNode):
    def __init__(self, statements):
        self.statements = statements

class ExternFunctionDeclarationNode(ASTNode):
    def __init__(self, name, params):
        self.name = name
        self.params = params

class BuiltinFunctionCallNode(ASTNode):
    def __init__(self, name, args):
        self.name = name
        self.args = args

# New AST nodes for syntactic sugar
class ListNode(ASTNode):
    def __init__(self, elements):
        self.elements = elements

class ListComprehensionNode(ASTNode):
    def __init__(self, expression, target, iterable, condition=None):
        self.expression = expression
        self.target = target
        self.iterable = iterable
        self.condition = condition

class IndexAccessNode(ASTNode):
    def __init__(self, obj, index):
        self.obj = obj
        self.index = index

class IndexAssignmentNode(ASTNode):
    def __init__(self, obj, index, value):
        self.obj = obj
        self.index = index
        self.value = value

class UnaryOpNode(ASTNode):
    def __init__(self, op, operand):
        self.op = op
        self.operand = operand

# --- Parser ---
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    @property
    def current_token(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def advance(self):
        self.pos += 1

    def parse(self):
        statements = []
        while self.current_token and self.current_token.type != TokenType.EOF:
            statements.append(self.parse_statement())
        return ProgramNode(statements)

    def parse_statement(self):
        if self.current_token.type == TokenType.PRINT:
            self.advance()
            values = [self.parse_expression()]
            while self.current_token and self.current_token.type == TokenType.COMMA:
                self.advance()
                values.append(self.parse_expression())
            return PrintNode(values)
        elif self.current_token.type == TokenType.LET:
            return self.parse_variable_declaration()
        elif self.current_token.type == TokenType.FUNC:
            return self.parse_function_declaration()
        elif self.current_token.type == TokenType.IF:
            return self.parse_if_statement()
        elif self.current_token.type == TokenType.WHILE:
            return self.parse_while_statement()
        elif self.current_token.type == TokenType.FOR:
            return self.parse_for_statement()
        elif self.current_token.type == TokenType.RETURN:
            self.advance()
            value = self.parse_expression()
            return ReturnNode(value)
        elif self.current_token.type == TokenType.EXTERN:
            return self.parse_extern_function_declaration()
        elif self.current_token.type == TokenType.IDENTIFIER: # Check for assignment
            # Peek ahead to see if it's an assignment
            next_token = self.tokens[self.pos + 1] if self.pos + 1 < len(self.tokens) else None
            if next_token and next_token.type == TokenType.EQUALS:
                identifier = self.current_token.value
                self.advance() # Consume identifier
                self.advance() # Consume '='
                value = self.parse_expression()
                return AssignmentNode(identifier, value)
            elif next_token and next_token.type == TokenType.LBRACKET:
                # Index assignment like arr[0] = value
                obj = VariableAccessNode(self.current_token.value)
                self.advance() # Consume identifier
                index_node = self.parse_index_access(obj)
                if self.current_token and self.current_token.type == TokenType.EQUALS:
                    self.advance() # Consume '='
                    value = self.parse_expression()
                    # Extract the object and index from the index_node
                    return IndexAssignmentNode(index_node.obj, index_node.index, value)
                else:
                    return index_node
            else:
                # If not an assignment, it must be an expression statement
                return self.parse_expression()
        else:
            # Default case for expressions that are statements (e.g., function calls)
            return self.parse_expression()

    def parse_variable_declaration(self):
        self.advance() # Consume 'let'
        identifier = self.current_token.value
        self.advance() # Consume identifier
        self.advance() # Consume '='
        value = self.parse_expression()
        return VariableDeclarationNode(identifier, value)

    def parse_function_declaration(self):
        self.advance() # Consume 'func'
        name = self.current_token.value
        self.advance() # Consume identifier
        self.advance() # Consume '('
        params = []
        if self.current_token.type != TokenType.RPAREN:
            params.append(self.current_token.value)
            self.advance()
            while self.current_token.type == TokenType.COMMA:
                self.advance()
                params.append(self.current_token.value)
                self.advance()
        self.advance() # Consume ')'
        body = self.parse_block()
        return FunctionDeclarationNode(name, params, body)

    def parse_if_statement(self):
        self.advance() # Consume 'if'
        condition = self.parse_expression()
        if_block = self.parse_block()
        else_block = None
        if self.current_token and self.current_token.type == TokenType.ELSE:
            self.advance()
            # Check if it's "else if" or just "else"
            if self.current_token and self.current_token.type == TokenType.IF:
                # This is an "else if" - parse it as another if statement
                else_block = self.parse_if_statement()
            else:
                # This is a simple "else" block
                else_block = self.parse_block()
        return IfNode(condition, if_block, else_block)

    def parse_while_statement(self):
        self.advance() # Consume 'while'
        condition = self.parse_expression()
        block = self.parse_block()
        return WhileNode(condition, block)

    def parse_for_statement(self):
        """Parse for loops like 'for item in iterable { ... }'"""
        self.advance() # Consume 'for'
        
        # Parse the target variable
        if self.current_token.type != TokenType.IDENTIFIER:
            raise Exception("Expected identifier after 'for'")
        target = self.current_token.value
        self.advance()
        
        # Parse 'in' keyword
        if self.current_token.type != TokenType.IN:
            raise Exception("Expected 'in' after target variable in for loop")
        self.advance()
        
        # Parse the iterable expression
        iterable = self.parse_expression()
        
        # Parse the block
        block = self.parse_block()
        
        # Create a for loop node
        return ForNode(target, iterable, block)

    def parse_block(self):
        self.advance() # Consume '{'
        statements = []
        while self.current_token and self.current_token.type != TokenType.RBRACE:
            statements.append(self.parse_statement())
        self.advance() # Consume '}'
        return BlockNode(statements)

    def parse_expression(self):
        node = self.parse_term()
        while self.current_token and self.current_token.type in (TokenType.PLUS, TokenType.MINUS, TokenType.LESS_THAN, TokenType.GREATER_THAN, TokenType.EQUAL_EQUAL, TokenType.NOT_EQUALS, TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL):
            op = self.current_token.type
            self.advance()
            right = self.parse_term()
            node = BinOpNode(node, op, right)
        return node

    def parse_term(self):
        node = self.parse_factor()
        while self.current_token and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            op = self.current_token.type
            self.advance()
            right = self.parse_factor()
            node = BinOpNode(node, op, right)
        return node

    def parse_factor(self):
        token = self.current_token
        if token.type == TokenType.MINUS:  # Handle unary minus
            self.advance()
            factor = self.parse_factor()
            return UnaryOpNode(TokenType.MINUS, factor)
        elif token.type == TokenType.INTEGER:
            self.advance()
            return IntegerNode(token.value)
        elif token.type == TokenType.FLOAT:
            self.advance()
            return FloatNode(token.value)
        elif token.type == TokenType.STRING:
            self.advance()
            return StringNode(token.value)
        elif token.type == TokenType.BOOLEAN:
            self.advance()
            return BooleanNode(token.value)
        elif token.type == TokenType.IDENTIFIER:
            self.advance()
            # Check for function call or index access
            if self.current_token and self.current_token.type == TokenType.LPAREN:
                if token.value in BUILTINS:
                    return self.parse_builtin_function_call(token.value)
                return self.parse_function_call(token.value)
            elif self.current_token and self.current_token.type == TokenType.LBRACKET:
                # Index access like arr[0]
                obj = VariableAccessNode(token.value)
                return self.parse_index_access(obj)
            return VariableAccessNode(token.value)
        elif token.type == TokenType.LBRACKET:  # List literal
            return self.parse_list_literal()
        elif token.type == TokenType.LPAREN:
            self.advance()
            node = self.parse_expression()
            self.advance() # Consume RPAREN
            return node
        raise Exception(f"Invalid syntax at token {token}")

    def parse_list_literal(self):
        """Parse a list literal like [1, 2, 3]"""
        self.advance() # Consume '['
        elements = []
        if self.current_token and self.current_token.type != TokenType.RBRACKET:
            elements.append(self.parse_expression())
            while self.current_token and self.current_token.type == TokenType.COMMA:
                self.advance()
                elements.append(self.parse_expression())
        self.advance() # Consume ']'
        return ListNode(elements)

    def parse_index_access(self, obj):
        """Parse index access like arr[0]"""
        self.advance() # Consume '['
        index = self.parse_expression()
        self.advance() # Consume ']'
        return IndexAccessNode(obj, index)

    def parse_function_call(self, name):
        self.advance() # Consume '('
        args = []
        if self.current_token.type != TokenType.RPAREN:
            args.append(self.parse_expression())
            while self.current_token.type == TokenType.COMMA:
                self.advance()
                args.append(self.parse_expression())
        self.advance() # Consume ')'
        return FunctionCallNode(name, args)

    def parse_extern_function_declaration(self):
        self.advance() # Consume 'extern'
        self.advance() # Consume 'func'
        name = self.current_token.value
        self.advance() # Consume identifier
        self.advance() # Consume '('
        params = []
        if self.current_token.type != TokenType.RPAREN:
            params.append(self.current_token.value)
            self.advance()
            while self.current_token.type == TokenType.COMMA:
                self.advance()
                params.append(self.current_token.value)
                self.advance()
        self.advance() # Consume ')'
        return ExternFunctionDeclarationNode(name, params)

    def parse_builtin_function_call(self, name):
        self.advance() # Consume '('
        args = []
        if self.current_token.type != TokenType.RPAREN:
            args.append(self.parse_expression())
            while self.current_token.type == TokenType.COMMA:
                self.advance()
                args.append(self.parse_expression())
        self.advance() # Consume ')'
        return BuiltinFunctionCallNode(name, args)