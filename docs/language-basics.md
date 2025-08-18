# Language Basics

This document covers the fundamental concepts of the Flow programming language.

## Syntax Overview

Flow has a clean, C-like syntax that's designed to be easy to read and write. Here's a quick example:

```flow
# This is a comment
let name = "Flow"  # Variable declaration
let version = 1.0

# Function definition
func greet(person) {
    return "Hello, " + person + "!"
}

# Function call
let message = greet(name)
print message
```

## Variables

In Flow, variables are declared using the `let` keyword:

```flow
let name = "Flow"
let age = 5
let pi = 3.14159
let isFast = true
```

Variables in Flow are dynamically typed, meaning you don't need to declare their type explicitly. The type is inferred from the value assigned to the variable.

### Data Types

Flow supports several built-in data types:

1. **Numbers**: Both integers and floating-point numbers
   ```flow
   let integer = 42
   let float = 3.14159
   ```

2. **Strings**: Text enclosed in double quotes
   ```flow
   let greeting = "Hello, World!"
   ```

3. **Booleans**: Logical values `true` or `false`
   ```flow
   let isActive = true
   let isComplete = false
   ```

4. **Lists**: Ordered collections of values
   ```flow
   let numbers = [1, 2, 3, 4, 5]
   let mixed = ["text", 42, true]
   ```

### Operators

Flow supports common operators for mathematical and logical operations:

#### Arithmetic Operators
- `+` : Addition
- `-` : Subtraction
- `*` : Multiplication
- `/` : Division
- `%` : Modulo (remainder)
- `**` : Exponentiation

#### Comparison Operators
- `==` : Equal to
- `!=` : Not equal to
- `<` : Less than
- `<=` : Less than or equal to
- `>` : Greater than
- `>=` : Greater than or equal to

#### Logical Operators
- `and` : Logical AND
- `or` : Logical OR
- `not` : Logical NOT

### Bitwise Operators
- `&` : Bitwise AND
- `|` : Bitwise OR
- `^` : Bitwise XOR

### Assignment Expression Operator (Walrus Operator)
- `:=` : Assignment within expressions

### Examples
```flow
let sum = 5 + 3        # 8
let isEqual = 5 == 3   # false
let isTrue = true and false  # false

# Bitwise operations
let a = 5  # Binary: 101
let b = 3  # Binary: 011
let andResult = a & b  # 1 (Binary: 001)
let orResult = a | b   # 7 (Binary: 111)
let xorResult = a ^ b  # 6 (Binary: 110)

# Walrus operator
if (x := 5) > 3 {
    print "x is", x, "which is greater than 3"
}
```

## Control Flow

Flow provides standard control flow structures:

### If Statements
```flow
if condition {
    # code executed if condition is true
} else if otherCondition {
    # code executed if otherCondition is true
} else {
    # code executed if neither condition is true
}
```

### While Loops
```flow
while condition {
    # code executed repeatedly while condition is true
}
```

### For Loops
```flow
for item in list {
    # code executed for each item in the list
}

# With range
for i in range(5) {
    # code executed 5 times with i = 0, 1, 2, 3, 4
}
```

### Match Statements (Pattern Matching)
```flow
match value {
    case 1:
        # code executed if value equals 1
    case 2:
        # code executed if value equals 2
    default:
        # code executed if no case matches
}
```

## Functions

Functions in Flow are defined using the `func` keyword:

```flow
func functionName(parameter1, parameter2) {
    # function body
    return value
}
```

Functions can return values using the `return` statement. If no return statement is executed, the function returns `null`.

### Function Calls
```flow
let result = functionName(arg1, arg2)
```

## Lists

Lists are ordered collections that can hold any type of value:

```flow
# Creating lists
let emptyList = []
let numbers = [1, 2, 3, 4, 5]
let mixed = ["text", 42, true]

# Accessing elements
let first = numbers[0]  # 1 (0-based indexing)

# Modifying elements
numbers[0] = 10  # numbers is now [10, 2, 3, 4, 5]

# List functions
append(numbers, 6)  # Add element to end
let length = len(numbers)  # Get list length
```

## Comments

Comments in Flow start with the `#` character and continue to the end of the line:

```flow
# This is a single-line comment

let x = 5  # This is also a comment

# Multi-line comments are just multiple
# single-line comments
```

## Program Structure

```flow
# Global variables
let globalVar = "value"

# Functions
func myFunction() {
    # function body
}

# Main code
print "Program starts here"
```

## Next Steps

After understanding these basics, you should explore:

1. [Control Flow](control-flow.md) for more detailed information on if statements and loops
2. [Functions](functions.md) for advanced function concepts
3. [Built-in Functions](built-in-functions.md) for the complete list of available functions
4. [Examples](examples.md) to see these concepts in practice