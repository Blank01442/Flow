import os
import math
import time
import json
from functools import lru_cache

BUILTINS = [
    'read_file', 'write_file', 'os_system', 'len', 'str', 'int', 'float', 
    'abs', 'min', 'max', 'sum', 'range', 'append', 'pop', 'split', 'join',
    'time', 'sleep', 'sqrt', 'pow', 'log', 'sin', 'cos', 'tan', 'json_parse',
    'json_stringify'
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

# JSON functions
def json_parse(string):
    """Parse JSON string"""
    return __builtins__['json.loads'](string)

def json_stringify(obj):
    """Convert object to JSON string"""
    return __builtins__['json.dumps'](obj)