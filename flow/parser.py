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


# Generic/Template nodes
class LambdaExpressionNode(ASTNode):
    def __init__(self, params, body):
        self.params = params
        self.body = body

class MapFunctionNode(ASTNode):
    def __init__(self, func, iterable):
        self.func = func
        self.iterable = iterable

class FilterFunctionNode(ASTNode):
    def __init__(self, func, iterable):
        self.func = func
        self.iterable = iterable

class ReduceFunctionNode(ASTNode):
    def __init__(self, func, iterable, initial=None):
        self.func = func
        self.iterable = iterable
        self.initial = initial

# Generic/Template nodes
class GenericTypeNode(ASTNode):
    def __init__(self, base_type, type_params):
        self.base_type = base_type
        self.type_params = type_params


class GenericFunctionDeclarationNode(ASTNode):
    def __init__(self, name, type_params, params, body):
        self.name = name
        self.type_params = type_params  # List of type parameter names
        self.params = params
        self.body = body

class AsyncFunctionDeclarationNode(ASTNode):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

class AwaitExpressionNode(ASTNode):
    def __init__(self, expression):
        self.expression = expression

class SpawnExpressionNode(ASTNode):
    def __init__(self, expression):
        self.expression = expression

class ChannelDeclarationNode(ASTNode):
    def __init__(self, identifier, data_type=None):
        self.identifier = identifier
        self.data_type = data_type

class SendStatementNode(ASTNode):
    def __init__(self, channel, value):
        self.channel = channel
        self.value = value

class ReceiveStatementNode(ASTNode):
    def __init__(self, channel, variable):
        self.channel = channel
        self.variable = variable

class BinOpNode(ASTNode):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right
        self.op = op
        self.right = right


class PipelineNode(ASTNode):
    def __init__(self, left, right):
        self.left = left
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

class MatchNode(ASTNode):
    def __init__(self, expression, cases, default_case=None):
        self.expression = expression
        self.cases = cases
        self.default_case = default_case


class CaseNode(ASTNode):
    def __init__(self, pattern, block):
        self.pattern = pattern
        self.block = block


# Enhanced pattern matching nodes
class PatternNode(ASTNode):
    pass


class LiteralPatternNode(PatternNode):
    def __init__(self, value):
        self.value = value


class VariablePatternNode(PatternNode):
    def __init__(self, name):
        self.name = name


class TuplePatternNode(PatternNode):
    def __init__(self, elements):
        self.elements = elements


class ConstructorPatternNode(PatternNode):
    def __init__(self, constructor, args):
        self.constructor = constructor
        self.args = args

class AssignmentExpressionNode(ASTNode):
    def __init__(self, identifier, value):
        self.identifier = identifier
        self.value = value

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
    def __init__(self, name, params, return_type=None, lib_path=None):
        self.name = name
        self.params = params
        self.return_type = return_type
        self.lib_path = lib_path

class BuiltinFunctionCallNode(ASTNode):
    def __init__(self, name, args):
        self.name = name
        self.args = args

# New AST nodes for syntactic sugar
class ListNode(ASTNode):
    def __init__(self, elements):
        self.elements = elements


class TupleNode(ASTNode):
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


# Memory management nodes
class AllocNode(ASTNode):
    def __init__(self, type_name, size=None):
        self.type_name = type_name
        self.size = size  # For arrays


class FreeNode(ASTNode):
    def __init__(self, expression):
        self.expression = expression


class RefNode(ASTNode):
    def __init__(self, expression):
        self.expression = expression


class DerefNode(ASTNode):
    def __init__(self, expression):
        self.expression = expression


# Immutable/mutable declarations
class MutableDeclarationNode(ASTNode):
    def __init__(self, identifier, value):
        self.identifier = identifier
        self.value = value


class ImmutableDeclarationNode(ASTNode):
    def __init__(self, identifier, value):
        self.identifier = identifier
        self.value = value


# Macro nodes
class MacroDefinitionNode(ASTNode):
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body


class MacroCallNode(ASTNode):
    def __init__(self, name, args):
        self.name = name
        self.args = args


class CompileTimeEvalNode(ASTNode):
    def __init__(self, expression):
        self.expression = expression


# Attribute/annotation nodes
class AnnotatedNode(ASTNode):
    def __init__(self, annotations, node):
        self.annotations = annotations  # List of annotation strings
        self.node = node

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
        elif self.current_token.type == TokenType.MUT:
            return self.parse_mutable_declaration()
        elif self.current_token.type == TokenType.FUNC or self.current_token.type == TokenType.FN:
            return self.parse_function_declaration()
        elif self.current_token.type == TokenType.ASYNC:
            return self.parse_async_function_declaration()
        elif self.current_token.type == TokenType.IF:
            return self.parse_if_statement()
        elif self.current_token.type == TokenType.WHILE:
            return self.parse_while_statement()
        elif self.current_token.type == TokenType.FOR:
            return self.parse_for_statement()
        elif self.current_token.type == TokenType.MATCH:
            return self.parse_match_statement()
        elif self.current_token.type == TokenType.RETURN:
            self.advance()
            value = self.parse_expression()
            return ReturnNode(value)
        elif self.current_token.type == TokenType.EXTERN:
            return self.parse_extern_function_declaration()
        elif self.current_token.type == TokenType.CHANNEL:
            return self.parse_channel_declaration()
        elif self.current_token.type == TokenType.SEND:
            return self.parse_send_statement()
        elif self.current_token.type == TokenType.RECEIVE:
            return self.parse_receive_statement()
        elif self.current_token.type == TokenType.ALLOC:
            return self.parse_alloc_statement()
        elif self.current_token.type == TokenType.FREE:
            return self.parse_free_statement()
        elif self.current_token.type == TokenType.MACRO:
            return self.parse_macro_definition()
        elif self.current_token.type == TokenType.AT:
            return self.parse_annotated_statement()
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
        return ImmutableDeclarationNode(identifier, value)

    def parse_mutable_declaration(self):
        self.advance() # Consume 'mut'
        identifier = self.current_token.value
        self.advance() # Consume identifier
        self.advance() # Consume '='
        value = self.parse_expression()
        return MutableDeclarationNode(identifier, value)

    def parse_alloc_statement(self):
        self.advance() # Consume 'alloc'
        type_name = self.current_token.value
        self.advance() # Consume type name
        
        size = None
        if self.current_token.type == TokenType.LBRACKET:
            self.advance() # Consume '['
            size = self.parse_expression()
            self.advance() # Consume ']'
            
        return AllocNode(type_name, size)

    def parse_free_statement(self):
        self.advance() # Consume 'free'
        expression = self.parse_expression()
        return FreeNode(expression)

    def parse_macro_definition(self):
        self.advance() # Consume 'macro'
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
        return MacroDefinitionNode(name, params, body)

    def parse_annotated_statement(self):
        annotations = []
        while self.current_token.type == TokenType.AT:
            self.advance() # Consume '@'
            if self.current_token.type == TokenType.IDENTIFIER:
                annotations.append(self.current_token.value)
                self.advance()
            else:
                raise Exception("Expected identifier after @ for annotation")
        
        # Parse the actual statement
        statement = self.parse_statement()
        return AnnotatedNode(annotations, statement)

    def parse_function_declaration(self):
        self.advance() # Consume 'func' or 'fn'
        name = self.current_token.value
        self.advance() # Consume identifier
        
        # Check for generic type parameters
        type_params = []
        if self.current_token.type == TokenType.LESS_THAN:
            self.advance() # Consume '<'
            while self.current_token.type != TokenType.GREATER_THAN:
                if self.current_token.type == TokenType.TYPE_NAME:
                    type_params.append(self.current_token.value)
                    self.advance()
                    if self.current_token.type == TokenType.COMMA:
                        self.advance()
                else:
                    break
            self.advance() # Consume '>'
        
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
        
        if type_params:
            return GenericFunctionDeclarationNode(name, type_params, params, body)
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

    def parse_match_statement(self):
        """Parse match statements like 'match value { case pattern: ... default: ... }'"""
        self.advance() # Consume 'match'
        
        # Parse the expression to match against
        expression = self.parse_expression()
        
        # Parse the opening brace
        if self.current_token.type != TokenType.LBRACE:
            raise Exception("Expected '{' after match expression")
        self.advance()
        
        # Parse cases
        cases = []
        default_case = None
        
        while self.current_token and self.current_token.type != TokenType.RBRACE:
            if self.current_token.type == TokenType.CASE:
                self.advance() # Consume 'case'
                
                # Parse the pattern
                pattern = self.parse_pattern()
                
                # Parse the colon
                if self.current_token.type != TokenType.COLON:
                    raise Exception("Expected ':' after case pattern")
                self.advance()
                
                # Parse statements until we hit another case, default, or closing brace
                statements = []
                while (self.current_token and 
                       self.current_token.type != TokenType.CASE and
                       self.current_token.type != TokenType.DEFAULT and
                       self.current_token.type != TokenType.RBRACE):
                    statements.append(self.parse_statement())
                
                cases.append(CaseNode(pattern, BlockNode(statements)))
                
            elif self.current_token.type == TokenType.DEFAULT:
                self.advance() # Consume 'default'
                
                # Parse the colon
                if self.current_token.type != TokenType.COLON:
                    raise Exception("Expected ':' after default")
                self.advance()
                
                # Parse statements until we hit the closing brace
                statements = []
                while (self.current_token and 
                       self.current_token.type != TokenType.CASE and
                       self.current_token.type != TokenType.DEFAULT and
                       self.current_token.type != TokenType.RBRACE):
                    statements.append(self.parse_statement())
                
                default_case = BlockNode(statements)
                
            else:
                raise Exception(f"Unexpected token in match statement: {self.current_token}")
        
        # Consume the closing brace
        if self.current_token.type != TokenType.RBRACE:
            raise Exception("Expected '}' to close match statement")
        self.advance()
        
        return MatchNode(expression, cases, default_case)

    def parse_pattern(self):
        """Parse a pattern for match statements"""
        if self.current_token.type == TokenType.INTEGER:
            value = int(self.current_token.value)
            self.advance()
            return LiteralPatternNode(value)
        elif self.current_token.type == TokenType.STRING:
            value = self.current_token.value
            self.advance()
            return LiteralPatternNode(value)
        elif self.current_token.type == TokenType.IDENTIFIER:
            # This could be a variable pattern or a constructor pattern
            name = self.current_token.value
            self.advance()
            
            # If followed by '(', it's a constructor pattern
            if self.current_token and self.current_token.type == TokenType.LPAREN:
                self.advance() # Consume '('
                args = []
                if self.current_token.type != TokenType.RPAREN:
                    args.append(self.parse_pattern())
                    while self.current_token.type == TokenType.COMMA:
                        self.advance()
                        args.append(self.parse_pattern())
                self.advance() # Consume ')'
                return ConstructorPatternNode(name, args)
            
            # Otherwise, it's a variable pattern
            return VariablePatternNode(name)
        elif self.current_token.type == TokenType.LPAREN:
            # Tuple pattern
            self.advance() # Consume '('
            elements = []
            if self.current_token.type != TokenType.RPAREN:
                elements.append(self.parse_pattern())
                while self.current_token.type == TokenType.COMMA:
                    self.advance()
                    elements.append(self.parse_pattern())
            self.advance() # Consume ')'
            return TuplePatternNode(elements)
        else:
            raise Exception(f"Unexpected token in pattern: {self.current_token}")

    def parse_block(self):
        self.advance() # Consume '{'
        statements = []
        while self.current_token and self.current_token.type != TokenType.RBRACE:
            statements.append(self.parse_statement())
        self.advance() # Consume '}'
        return BlockNode(statements)

    def parse_expression(self):
        # Check for lambda expression
        if self.current_token and self.current_token.type == TokenType.LAMBDA:
            return self.parse_lambda_expression()
        
        # Check for map function
        if self.current_token and self.current_token.type == TokenType.MAP:
            return self.parse_map_function()
        
        # Check for filter function
        if self.current_token and self.current_token.type == TokenType.FILTER:
            return self.parse_filter_function()
        
        # Check for reduce function
        if self.current_token and self.current_token.type == TokenType.REDUCE:
            return self.parse_reduce_function()
        
        # Check for spawn expression
        if self.current_token and self.current_token.type == TokenType.SPAWN:
            return self.parse_spawn_expression()
        
        # Check for await expression
        if self.current_token and self.current_token.type == TokenType.AWAIT:
            return self.parse_await_expression()
        
        # Check for assignment expression (walrus operator)
        # Look ahead to see if we have an identifier followed by :=
        if (self.current_token and self.current_token.type == TokenType.IDENTIFIER and
            self.pos + 1 < len(self.tokens) and 
            self.tokens[self.pos + 1].type == TokenType.WALRUS):
            # This is an assignment expression
            identifier = self.current_token.value
            self.advance()  # Consume identifier
            self.advance()  # Consume :=
            value = self.parse_expression()
            return AssignmentExpressionNode(identifier, value)
        
        # Parse pipeline expressions (lowest precedence)
        node = self.parse_logical_or()
        while self.current_token and self.current_token.type == TokenType.PIPELINE:
            self.advance()
            right = self.parse_logical_or()
            node = PipelineNode(node, right)
        return node

    def parse_logical_or(self):
        # Parse logical OR expressions
        node = self.parse_logical_and()
        while self.current_token and self.current_token.type == TokenType.OR:
            op = self.current_token.type
            self.advance()
            right = self.parse_logical_and()
            node = BinOpNode(node, op, right)
        return node

    def parse_logical_or(self):
        # Parse logical OR expressions
        node = self.parse_logical_and()
        while self.current_token and self.current_token.type == TokenType.OR:
            op = self.current_token.type
            self.advance()
            right = self.parse_logical_and()
            node = BinOpNode(node, op, right)
        return node

    def parse_logical_and(self):
        # Parse comparison expressions
        node = self.parse_term()
        while self.current_token and self.current_token.type in (TokenType.LESS_THAN, TokenType.GREATER_THAN, TokenType.EQUAL_EQUAL, TokenType.NOT_EQUALS, TokenType.LESS_EQUAL, TokenType.GREATER_EQUAL):
            op = self.current_token.type
            self.advance()
            right = self.parse_term()
            node = BinOpNode(node, op, right)
        return node

    def parse_term(self):
        node = self.parse_factor()
        while self.current_token and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            op = self.current_token.type
            self.advance()
            right = self.parse_factor()
            node = BinOpNode(node, op, right)
        return node

    def parse_factor(self):
        node = self.parse_power()
        while self.current_token and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE, TokenType.MODULO):
            op = self.current_token.type
            self.advance()
            right = self.parse_power()
            node = BinOpNode(node, op, right)
        return node

    def parse_power(self):
        # Handle exponentiation (highest precedence)
        node = self.parse_unary()
        # Note: We're not implementing power operator in this version
        return node

    def parse_unary(self):
        token = self.current_token
        if token.type == TokenType.MINUS:  # Handle unary minus
            self.advance()
            factor = self.parse_unary()
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
        elif token.type == TokenType.LBRACKET or token.type == TokenType.LPAREN:  # List or tuple literal
            return self.parse_list_literal()
        elif token.type == TokenType.LPAREN:
            self.advance()
            # Check if this is an assignment expression
            # Look ahead to see if we have an identifier followed by :=
            if (self.current_token and self.current_token.type == TokenType.IDENTIFIER and
                self.pos + 1 < len(self.tokens) and 
                self.tokens[self.pos + 1].type == TokenType.WALRUS):
                # This is an assignment expression within parentheses
                node = self.parse_expression()
                if self.current_token.type != TokenType.RPAREN:
                    raise Exception("Expected ')' after assignment expression")
                self.advance() # Consume RPAREN
                return node
            else:
                # Normal parenthesized expression
                node = self.parse_expression()
                if self.current_token.type != TokenType.RPAREN:
                    raise Exception("Expected ')' after expression")
                self.advance() # Consume RPAREN
                return node
        raise Exception(f"Invalid syntax at token {token}")

    def parse_list_literal(self):
        """Parse a list literal like [1, 2, 3] or tuple like (1, 2, 3)"""
        if self.current_token.type == TokenType.LBRACKET:
            # List literal
            self.advance() # Consume '['
            elements = []
            if self.current_token and self.current_token.type != TokenType.RBRACKET:
                elements.append(self.parse_expression())
                while self.current_token and self.current_token.type == TokenType.COMMA:
                    self.advance()
                    elements.append(self.parse_expression())
            self.advance() # Consume ']'
            return ListNode(elements)
        elif self.current_token.type == TokenType.LPAREN:
            # Tuple literal
            self.advance() # Consume '('
            elements = []
            if self.current_token and self.current_token.type != TokenType.RPAREN:
                elements.append(self.parse_expression())
                while self.current_token and self.current_token.type == TokenType.COMMA:
                    self.advance()
                    elements.append(self.parse_expression())
            self.advance() # Consume ')'
            return TupleNode(elements)

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
        
        # Check for library specification
        lib_path = None
        if self.current_token.type == TokenType.STRING:
            lib_path = self.current_token.value
            self.advance() # Consume string
        
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
        
        # Check for return type specification
        return_type = None
        if self.current_token.type == TokenType.COLON:
            self.advance() # Consume ':'
            if self.current_token.type == TokenType.IDENTIFIER:
                return_type = self.current_token.value
                self.advance()
        
        return ExternFunctionDeclarationNode(name, params, return_type, lib_path)

    def parse_lambda_expression(self):
        """Parse lambda expressions"""
        self.advance() # Consume 'lambda'
        
        # Parse parameters
        params = []
        if self.current_token and self.current_token.type == TokenType.LPAREN:
            self.advance() # Consume '('
            if self.current_token and self.current_token.type != TokenType.RPAREN:
                params.append(self.current_token.value)
                self.advance()
                while self.current_token and self.current_token.type == TokenType.COMMA:
                    self.advance()
                    params.append(self.current_token.value)
                    self.advance()
            self.advance() # Consume ')'
        
        # Parse arrow (->)
        if self.current_token and self.current_token.type == TokenType.MINUS:
            self.advance() # Consume '-'
            if self.current_token and self.current_token.type == TokenType.GREATER_THAN:
                self.advance() # Consume '>'
        
        # Parse body
        body = self.parse_expression()
        return LambdaExpressionNode(params, body)

    def parse_map_function(self):
        """Parse map function calls"""
        self.advance() # Consume 'map'
        self.advance() # Consume '('
        func = self.parse_expression()
        self.advance() # Consume ','
        iterable = self.parse_expression()
        self.advance() # Consume ')'
        return MapFunctionNode(func, iterable)

    def parse_filter_function(self):
        """Parse filter function calls"""
        self.advance() # Consume 'filter'
        self.advance() # Consume '('
        func = self.parse_expression()
        self.advance() # Consume ','
        iterable = self.parse_expression()
        self.advance() # Consume ')'
        return FilterFunctionNode(func, iterable)

    def parse_reduce_function(self):
        """Parse reduce function calls"""
        self.advance() # Consume 'reduce'
        self.advance() # Consume '('
        func = self.parse_expression()
        self.advance() # Consume ','
        iterable = self.parse_expression()
        
        # Check for initial value
        initial = None
        if self.current_token and self.current_token.type == TokenType.COMMA:
            self.advance() # Consume ','
            initial = self.parse_expression()
            
        self.advance() # Consume ')'
        return ReduceFunctionNode(func, iterable, initial)

    def parse_async_function_declaration(self):
        """Parse async function declarations"""
        self.advance() # Consume 'async'
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
        return AsyncFunctionDeclarationNode(name, params, body)

    def parse_await_expression(self):
        """Parse async function declarations"""
        self.advance() # Consume 'async'
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
        return AsyncFunctionDeclarationNode(name, params, body)

    def parse_await_expression(self):
        """Parse await expressions"""
        self.advance() # Consume 'await'
        expression = self.parse_expression()
        return AwaitExpressionNode(expression)

    def parse_spawn_expression(self):
        """Parse spawn expressions"""
        self.advance() # Consume 'spawn'
        expression = self.parse_expression()
        return SpawnExpressionNode(expression)

    def parse_channel_declaration(self):
        """Parse channel declarations"""
        self.advance() # Consume 'channel'
        identifier = self.current_token.value
        self.advance() # Consume identifier
        
        # Check for data type specification
        data_type = None
        if self.current_token and self.current_token.type == TokenType.COLON:
            self.advance() # Consume ':'
            if self.current_token and self.current_token.type == TokenType.IDENTIFIER:
                data_type = self.current_token.value
                self.advance()
        
        return ChannelDeclarationNode(identifier, data_type)

    def parse_send_statement(self):
        """Parse send statements"""
        self.advance() # Consume 'send'
        channel = self.parse_expression()
        if self.current_token.type != TokenType.COMMA:
            raise Exception("Expected ',' after channel in send statement")
        self.advance() # Consume ','
        value = self.parse_expression()
        return SendStatementNode(channel, value)

    def parse_receive_statement(self):
        """Parse receive statements"""
        self.advance() # Consume 'receive'
        channel = self.parse_expression()
        if self.current_token and self.current_token.type == TokenType.COMMA:
            self.advance() # Consume ','
            if self.current_token and self.current_token.type == TokenType.IDENTIFIER:
                variable = self.current_token.value
                self.advance() # Consume identifier
                return ReceiveStatementNode(channel, variable)
            else:
                raise Exception("Expected identifier after ',' in receive statement")
        else:
            raise Exception("Expected ',' after channel in receive statement")

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