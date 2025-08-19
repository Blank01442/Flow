# Foreign Function Interface (FFI)

Flow provides a Foreign Function Interface (FFI) that allows you to call functions from shared libraries (DLLs on Windows, .so files on Linux, .dylib on macOS).

## FFI Built-in Functions

### `ffi_load(lib_path)`
Load a shared library.

**Parameters:**
- `lib_path` (string): Path to the shared library

**Returns:**
- Library handle

### `ffi_register(lib_path, func_name, return_type, arg_types...)`
Register a function signature from a loaded library.

**Parameters:**
- `lib_path` (string): Path to the shared library
- `func_name` (string): Name of the function
- `return_type` (string): Return type ("int", "float", "double", "void", "string", "bool")
- `arg_types` (strings): Argument types

### `ffi_call(lib_path, func_name, args...)`
Call a function from a loaded library.

**Parameters:**
- `lib_path` (string): Path to the shared library
- `func_name` (string): Name of the function
- `args` (any): Function arguments

**Returns:**
- Function result

## Example

```flow
# Load a system library
let lib = ffi_load("msvcrt.dll")  # Windows example

# Register a function signature
ffi_register("msvcrt.dll", "abs", "int", ["int"])

# Call a function
let result = ffi_call("msvcrt.dll", "abs", -5)
print "Absolute value of -5:", result
```

Note: FFI support is experimental and may have platform-specific behavior.