import os
import math
import time
import json
from functools import lru_cache

# Import FFI module
from . import ffi

BUILTINS = [
    'read_file', 'write_file', 'os_system', 'len', 'str', 'int', 'float', 
    'abs', 'min', 'max', 'sum', 'range', 'append', 'pop', 'split', 'join',
    'time', 'sleep', 'sqrt', 'pow', 'log', 'sin', 'cos', 'tan', 'json_parse',
    'json_stringify', 'floor', 'ceil', 'round', 'type', 'ord', 'chr', 'hex', 'bin',
    'input', 'exit', 'random', 'randint', 'shuffle', 'sort', 'reverse', 'contains',
    'ffi_load', 'ffi_call', 'ffi_register',
    'map', 'filter', 'reduce'
]

# Cache for file operations to avoid repeated file system calls
_file_cache = {}

@lru_cache(maxsize=128)
def read_file(path):
    """Read file with caching for better performance"""
    try:
        if path in _file_cache:
            return _file_cache[path]
        
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
            _file_cache[path] = content
            return content
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{path}' not found")
    except Exception as e:
        raise Exception(f"Error reading file '{path}': {e}")

def write_file(path, content):
    """Write file with cache invalidation"""
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Invalidate cache for this file
        if path in _file_cache:
            del _file_cache[path]
            
    except Exception as e:
        raise Exception(f"Error writing file '{path}': {e}")

def os_system(command):
    """Execute system command with better error handling"""
    try:
        return os.system(command)
    except Exception as e:
        raise Exception(f"Error executing command '{command}': {e}")

def clear_cache():
    """Clear the file cache"""
    global _file_cache
    _file_cache.clear()

def get_cache_info():
    """Get information about the current cache state"""
    return {
        'cached_files': list(_file_cache.keys()),
        'cache_size': len(_file_cache)
    }

# String functions
def len(obj):
    """Get the length of a string or list"""
    return __builtins__['len'](obj)

def str(obj):
    """Convert object to string"""
    return __builtins__['str'](obj)

def split(string, delimiter=' '):
    """Split a string by delimiter"""
    return string.split(delimiter)

def join(separator, iterable):
    """Join an iterable with a separator"""
    return separator.join(iterable)

# Numeric functions
def int(obj):
    """Convert object to integer"""
    return __builtins__['int'](obj)

def float(obj):
    """Convert object to float"""
    return __builtins__['float'](obj)

def abs(num):
    """Get absolute value"""
    return __builtins__['abs'](num)

def min(*args):
    """Get minimum value"""
    # Handle case where a single list is passed
    if len(args) == 1 and isinstance(args[0], list):
        return __builtins__['min'](args[0])
    return __builtins__['min'](args)

def max(*args):
    """Get maximum value"""
    # Handle case where a single list is passed
    if len(args) == 1 and isinstance(args[0], list):
        return __builtins__['max'](args[0])
    return __builtins__['max'](args)

def sum(iterable):
    """Sum all values in an iterable"""
    return __builtins__['sum'](iterable)

def sqrt(num):
    """Calculate square root"""
    return math.sqrt(num)

def pow(base, exponent):
    """Calculate power"""
    return __builtins__['pow'](base, exponent)

def log(num):
    """Calculate natural logarithm"""
    return math.log(num)

def sin(num):
    """Calculate sine"""
    return math.sin(num)

def cos(num):
    """Calculate cosine"""
    return math.cos(num)

def tan(num):
    """Calculate tangent"""
    return math.tan(num)

# List functions
def append(lst, item):
    """Append item to list"""
    lst.append(item)
    return lst

def pop(lst):
    """Remove and return last item from list"""
    return lst.pop()

def range(start, stop=None, step=1):
    """Generate a range of numbers"""
    if stop is None:
        return list(__builtins__['range'](start))
    return list(__builtins__['range'](start, stop, step))

# Time functions
def time():
    """Get current time in seconds since epoch"""
    return __builtins__['time']()

def sleep(seconds):
    """Sleep for specified seconds"""
    __builtins__['time.sleep'](seconds)

# Additional Math functions
def floor(num):
    """Round number down to nearest integer"""
    return math.floor(num)

def ceil(num):
    """Round number up to nearest integer"""
    return math.ceil(num)

def round(num, ndigits=0):
    """Round number to nearest integer or to specified decimal places"""
    return __builtins__['round'](num, ndigits)

# Type functions
def type(obj):
    """Get the type of an object"""
    return __builtins__['type'](obj).__name__

# String functions
def ord(char):
    """Get ASCII value of character"""
    return __builtins__['ord'](char)

def chr(num):
    """Get character from ASCII value"""
    return __builtins__['chr'](num)

def hex(num):
    """Convert number to hexadecimal string"""
    return __builtins__['hex'](num)

def bin(num):
    """Convert number to binary string"""
    return __builtins__['bin'](num)

# Input/Output functions
def input(prompt=""):
    """Get input from user"""
    return __builtins__['input'](prompt)

def exit(code=0):
    """Exit the program with optional exit code"""
    __builtins__['exit'](code)

# Random functions
import random as _random

def random():
    """Generate random float between 0.0 and 1.0"""
    return _random.random()

def randint(a, b):
    """Generate random integer between a and b (inclusive)"""
    return _random.randint(a, b)

def shuffle(lst):
    """Shuffle list in place"""
    _random.shuffle(lst)
    return lst

# List functions
def sort(lst, reverse=False):
    """Sort list in place"""
    lst.sort(reverse=reverse)
    return lst

def reverse(lst):
    """Reverse list in place"""
    lst.reverse()
    return lst

def contains(sequence, item):
    """Check if item is in sequence"""
    return item in sequence

# JSON functions
def json_parse(string):
    """Parse JSON string"""
    return __builtins__['json.loads'](string)

def json_stringify(obj):
    """Convert object to JSON string"""
    return __builtins__['json.dumps'](obj)

# FFI functions
def ffi_load(lib_path):
    """Load a shared library"""
    return ffi.ffi_load(lib_path)

def ffi_call(lib_path, func_name, *args):
    """Call a function from a loaded library"""
    return ffi.ffi_call(lib_path, func_name, *args)

def ffi_register(lib_path, func_name, return_type, *arg_types):
    """Register a function signature"""
    return ffi.ffi_register(lib_path, func_name, return_type, arg_types)

# Functional programming functions
def map(func, iterable):
    """Apply function to each element in iterable"""
    if callable(func):
        return [func(item) for item in iterable]
    else:
        # If func is not callable, it might be a Flow function
        # In a full implementation, we would handle Flow functions properly
        # For now, we'll return the iterable as a placeholder
        return [item for item in iterable]

def filter(func, iterable):
    """Filter elements in iterable using function"""
    if callable(func):
        return [item for item in iterable if func(item)]
    else:
        # If func is not callable, it might be a Flow function
        # In a full implementation, we would handle Flow functions properly
        # For now, we'll return the iterable as a placeholder
        return [item for item in iterable]

def reduce(func, iterable, initial=None):
    """Reduce elements in iterable using function"""
    if not iterable:
        return initial
    
    if initial is None:
        result = iterable[0]
        items = iterable[1:]
    else:
        result = initial
        items = iterable
    
    if callable(func):
        for item in items:
            result = func(result, item)
        return result
    else:
        # If func is not callable, it might be a Flow function
        # In a full implementation, we would handle Flow functions properly
        # For now, we'll return a placeholder
        return result