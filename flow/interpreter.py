
from .parser import PrintNode, StringNode

class Interpreter:
    def __init__(self):
        self.symbol_table = {}
        self._method_cache = {}  # Cache for visitor methods

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

    def visit_PrintNode(self, node):
        value = self.visit(node.value)
        print(value)

    def visit_StringNode(self, node):
        return node.value

    def interpret(self, ast):
        for node in ast:
            self.visit(node)

    def get_symbol(self, name):
        """Get symbol value with error handling"""
        if name not in self.symbol_table:
            raise NameError(f"Name '{name}' is not defined")
        return self.symbol_table[name]

    def set_symbol(self, name, value):
        """Set symbol value"""
        self.symbol_table[name] = value

    def clear_symbols(self):
        """Clear all symbols"""
        self.symbol_table.clear()

    def get_symbols(self):
        """Get all symbol names"""
        return list(self.symbol_table.keys())
