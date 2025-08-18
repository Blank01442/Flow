from enum import IntEnum

class OpCode(IntEnum):
    LOAD_CONST = 0
    STORE_NAME = 1
    LOAD_NAME = 2
    BINARY_ADD = 3
    BINARY_SUBTRACT = 4
    BINARY_MULTIPLY = 5
    BINARY_DIVIDE = 6
    PRINT = 7
    JUMP_IF_FALSE = 8
    JUMP = 9
    RETURN_VALUE = 10
    CALL_FUNCTION = 11
    CALL_BUILTIN = 22
    POP_TOP = 12
    COMPARE_OP = 13
    BINARY_MODULO = 14
    BINARY_POWER = 15
    UNARY_NEGATIVE = 16
    UNARY_NOT = 17
    LOAD_FAST = 18  # Fast local variable access
    STORE_FAST = 19  # Fast local variable storage
    LOAD_GLOBAL = 20  # Fast global variable access
    STORE_GLOBAL = 21  # Fast global variable storage

class CompareOp(IntEnum):
    LESS_THAN = 0
    LESS_EQUAL = 1
    EQUAL = 2
    NOT_EQUAL = 3
    GREATER_THAN = 4
    GREATER_EQUAL = 5
    GREATER_THAN_OR_EQUAL = 6  # Alias for compatibility
    LESS_THAN_OR_EQUAL = 7     # Alias for compatibility

# Cache for frequently used opcodes
OPCODE_CACHE = {opcode: opcode for opcode in OpCode}
COMPARE_CACHE = {opcode: opcode for opcode in CompareOp}
