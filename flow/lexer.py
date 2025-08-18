import re
from enum import Enum

class TokenType(Enum):
    # Keywords
    PRINT = r'print'
    IF = r'if'
    ELSE = r'else'
    WHILE = r'while'
    LET = r'let'
    FUNC = r'func'
    RETURN = r'return'
    EXTERN = r'extern'

    # Data types
    IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'
    FLOAT = r'\d+\.\d+'
    INTEGER = r'\d+'
    STRING = r'"(?:\\.|[^\\"])*"'
    BOOLEAN = r'true|false'

    # Operators
    EQUALS = r'='
    PLUS = r'\+'
    MINUS = r'-'
    MULTIPLY = r'\*'
    DIVIDE = r'/'
    LPAREN = r'\('
    RPAREN = r'\)'
    LBRACKET = r'\['
    RBRACKET = r'\]'
    LBRACE = r'\{'
    RBRACE = r'\}'
    COMMA = r','
    LESS_THAN = r'<'
    GREATER_THAN = r'>'
    NOT_EQUALS = r'!='
    EQUAL_EQUAL = r'=='
    LESS_EQUAL = r'<='
    GREATER_EQUAL = r'>='

    # Other
    NEWLINE = r'\n'
    WHITESPACE = r'[ \t]+'
    COMMENT = r'#.*'
    EOF = r'EOF'

class Token:
    __slots__ = ['type', 'value', 'line', 'column']
    
    def __init__(self, type, value, line=0, column=0):
        self.type = type
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        return f'Token({self.type.name}, {self.value!r}, line={self.line}, column={self.column})'

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens = []
        
        # Pre-compile regex patterns for better performance
        self._compile_patterns()
    
    def _compile_patterns(self):
        """Pre-compile all regex patterns for better performance"""
        self.patterns = [
            (TokenType.PRINT, re.compile(r'print')),
            (TokenType.IF, re.compile(r'if')),
            (TokenType.ELSE, re.compile(r'else')),
            (TokenType.WHILE, re.compile(r'while')),
            (TokenType.LET, re.compile(r'let')),
            (TokenType.FUNC, re.compile(r'func')),
            (TokenType.RETURN, re.compile(r'return')),
            (TokenType.EXTERN, re.compile(r'extern')),
            (TokenType.BOOLEAN, re.compile(r'true|false')),
            (TokenType.IDENTIFIER, re.compile(r'[a-zA-Z_][a-zA-Z0-9_]*')),
            (TokenType.FLOAT, re.compile(r'\d+\.\d+')),
            (TokenType.INTEGER, re.compile(r'\d+')),
            (TokenType.STRING, re.compile(r'"(?:\\.|[^\\"])*"')),
            (TokenType.NOT_EQUALS, re.compile(r'!=')),
            (TokenType.EQUAL_EQUAL, re.compile(r'==')),
            (TokenType.EQUALS, re.compile(r'=')),
            (TokenType.PLUS, re.compile(r'\+')),
            (TokenType.MINUS, re.compile(r'-')),
            (TokenType.MULTIPLY, re.compile(r'\*')),
            (TokenType.DIVIDE, re.compile(r'/')),
            (TokenType.LPAREN, re.compile(r'\(')),
            (TokenType.RPAREN, re.compile(r'\)')),
            (TokenType.LBRACKET, re.compile(r'\[')),
            (TokenType.RBRACKET, re.compile(r'\]')),
            (TokenType.LBRACE, re.compile(r'\{')),
            (TokenType.RBRACE, re.compile(r'\}')),
            (TokenType.COMMA, re.compile(r',')),
            (TokenType.LESS_EQUAL, re.compile(r'<=')),
            (TokenType.GREATER_EQUAL, re.compile(r'>=')),
            (TokenType.LESS_THAN, re.compile(r'<')),
            (TokenType.GREATER_THAN, re.compile(r'>')),
            (TokenType.NEWLINE, re.compile(r'\n')),
            (TokenType.WHITESPACE, re.compile(r'[ \t]+')),
            (TokenType.COMMENT, re.compile(r'#.*')),
        ]

    def tokenize(self):
        """Optimized tokenization with pre-compiled patterns"""
        text_len = len(self.text)
        
        while self.pos < text_len:
            matched = False
            
            for token_type, pattern in self.patterns:
                match = pattern.match(self.text, self.pos)
                if match:
                    value = match.group(0)
                    value_len = len(value)
                    
                    # Skip whitespace, comments, and newlines
                    if token_type not in [TokenType.WHITESPACE, TokenType.COMMENT, TokenType.NEWLINE]:
                        if token_type == TokenType.STRING:
                            value = value[1:-1]  # Remove quotes
                        self.tokens.append(Token(token_type, value, self.line, self.column))
                    
                    self.pos += value_len
                    
                    # Update line and column tracking
                    if token_type == TokenType.NEWLINE:
                        self.line += 1
                        self.column = 1
                    else:
                        self.column += value_len
                    
                    matched = True
                    break
            
            if not matched:
                raise Exception(f"Unexpected character: {self.text[self.pos]} at line {self.line}, column {self.column}")

        self.tokens.append(Token(TokenType.EOF, None, self.line, self.column))
        return self.tokens