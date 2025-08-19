import ctypes
import os

class FFIManager:
    def __init__(self):
        self.loaded_libraries = {}
        self.function_signatures = {}
        
    def load_library(self, lib_path):
        """Load a shared library"""
        if lib_path in self.loaded_libraries:
            return self.loaded_libraries[lib_path]
            
        try:
            # Try to load the library
            lib = ctypes.CDLL(lib_path)
            self.loaded_libraries[lib_path] = lib
            return lib
        except OSError as e:
            raise Exception(f"Failed to load library {lib_path}: {e}")
    
    def register_function(self, lib_path, func_name, return_type, arg_types):
        """Register a function signature from a library"""
        key = f"{lib_path}:{func_name}"
        self.function_signatures[key] = {
            'return_type': return_type,
            'arg_types': arg_types
        }
    
    def call_function(self, lib_path, func_name, args):
        """Call a function from a loaded library"""
        # Load library if not already loaded
        lib = self.load_library(lib_path)
        
        # Get function from library
        try:
            func = getattr(lib, func_name)
        except AttributeError:
            raise Exception(f"Function {func_name} not found in library {lib_path}")
        
        # Apply signature if registered
        key = f"{lib_path}:{func_name}"
        if key in self.function_signatures:
            sig = self.function_signatures[key]
            func.restype = sig['return_type']
            func.argtypes = sig['arg_types']
        
        # Call function
        try:
            return func(*args)
        except Exception as e:
            raise Exception(f"Error calling {func_name}: {e}")

# Global FFI manager instance
ffi_manager = FFIManager()

# Built-in FFI functions
def ffi_load(lib_path):
    """Load a shared library"""
    return ffi_manager.load_library(lib_path)

def ffi_call(lib_path, func_name, *args):
    """Call a function from a loaded library"""
    return ffi_manager.call_function(lib_path, func_name, args)

def ffi_register(lib_path, func_name, return_type, arg_types):
    """Register a function signature"""
    # Map string types to ctypes
    type_map = {
        'int': ctypes.c_int,
        'float': ctypes.c_float,
        'double': ctypes.c_double,
        'void': None,
        'string': ctypes.c_char_p,
        'bool': ctypes.c_bool
    }
    
    # Convert string types to ctypes
    rt = type_map.get(return_type, ctypes.c_int)
    at = [type_map.get(arg, ctypes.c_int) for arg in arg_types]
    
    ffi_manager.register_function(lib_path, func_name, rt, at)