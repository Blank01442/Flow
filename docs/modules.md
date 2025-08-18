# Modules and Imports

Modules in Flow allow you to organize your code into separate files and reuse functionality across different programs. This document explains how to create and use modules in Flow.

## What are Modules?

A module is a Flow file that contains functions, variables, and other code that can be reused in other Flow programs. Modules help you:

1. Organize code into logical units
2. Reuse code across multiple programs
3. Avoid naming conflicts
4. Create libraries of useful functions

## Creating Modules

Any Flow file can be used as a module. Here's an example of a simple module:

**math_utils.flow**:
```flow
# A simple math utilities module

func add(a, b) {
    return a + b
}

func subtract(a, b) {
    return a - b
}

func multiply(a, b) {
    return a * b
}

func divide(a, b) {
    if b == 0 {
        print "Error: Division by zero"
        return null
    }
    return a / b
}

# Module-level variable
let PI = 3.14159
```

## Using Modules

Currently, Flow doesn't have a built-in import system like other languages. However, you can achieve modularity through:

### 1. Copying Code

For small projects, you can copy useful functions between files as needed.

### 2. Source Code Inclusion

You can structure your programs to include common code at the beginning:

**main.flow**:
```flow
# Include common utilities
# (In a future version, this might be replaced with an import system)

func add(a, b) {
    return a + b
}

func subtract(a, b) {
    return a - b
}

# Main program code
let result = add(5, 3)
print "Result:", result
```

### 3. Library Pattern

Create a "library" file with commonly used functions:

**common.flow**:
```flow
# Common utility functions

func max(a, b) {
    if a > b {
        return a
    }
    return b
}

func min(a, b) {
    if a < b {
        return a
    }
    return b
}

func clamp(value, minVal, maxVal) {
    return min(max(value, minVal), maxVal)
}

func isEven(n) {
    return n % 2 == 0
}

func isOdd(n) {
    return n % 2 != 0
}
```

Then reference these functions in your main programs.

## Module Best Practices

### 1. Naming Conventions

- Use descriptive names for module files
- Use lowercase with underscores for multi-word names (e.g., `string_utils.flow`)
- Be consistent with naming across your project

### 2. Documentation

Document your modules with comments explaining:

```flow
# String Utilities Module
# Provides common string manipulation functions
# Author: Your Name
# Version: 1.0

func reverseString(str) {
    # Reverses the characters in a string
    # Parameters:
    #   str - the string to reverse
    # Returns:
    #   the reversed string
    let reversed = ""
    let i = len(str) - 1
    while i >= 0 {
        reversed = reversed + str[i]
        i = i - 1
    }
    return reversed
}
```

### 3. Function Organization

- Group related functions together
- Place commonly used functions at the top
- Use consistent parameter ordering
- Handle edge cases appropriately

### 4. Constants

Define constants at the module level:

```flow
# Mathematical constants
let PI = 3.14159
let E = 2.71828

# Configuration values
let MAX_RETRIES = 3
let TIMEOUT = 30
```

## Example: Creating a File Utilities Module

**file_utils.flow**:
```flow
# File Utilities Module
# Functions for common file operations

func readFileLines(filename) {
    # Read a file and return its contents as a list of lines
    let content = read_file(filename)
    if content == null {
        return null
    }
    return split(content, "\n")
}

func writeFileLines(filename, lines) {
    # Write a list of lines to a file
    let content = join("\n", lines)
    write_file(filename, content)
}

func countLines(filename) {
    # Count the number of lines in a file
    let lines = readFileLines(filename)
    if lines == null {
        return -1
    }
    return len(lines)
}

func appendToFile(filename, content) {
    # Append content to a file
    let existing = read_file(filename)
    if existing == null {
        existing = ""
    }
    write_file(filename, existing + content)
}
```

## Future Module System

In future versions of Flow, we plan to implement a proper import system that will allow:

```flow
# Future syntax (not yet implemented)
import "math_utils.flow"
import "string_utils.flow" as strutils

let result = math_utils.add(5, 3)
let reversed = strutils.reverse("hello")
```

This will make code organization and reuse much more powerful and convenient.

## Module Design Guidelines

1. **Single Responsibility**: Each module should have a clear, focused purpose
2. **Consistent Interface**: Maintain consistent function signatures and naming
3. **Clear Dependencies**: Minimize dependencies between modules
4. **Error Handling**: Handle errors gracefully and provide meaningful error messages
5. **Testing**: Include test cases for module functions

## Next Steps

After learning about modules, explore:

1. [Examples](examples.md) to see how to organize code in practice
2. [Best Practices](best-practices.md) for overall coding guidelines
3. [Built-in Functions](built-in-functions.md) to learn about the standard library