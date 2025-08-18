# Flow Programming Language Tutorial

Welcome to the Flow programming language tutorial! This guide will take you from complete beginner to proficient user of Flow.

## Table of Contents
1. [Introduction](#introduction)
2. [Setting Up Flow](#setting-up-flow)
3. [Hello World](#hello-world)
4. [Variables and Data Types](#variables-and-data-types)
5. [Control Flow](#control-flow)
6. [Functions](#functions)
7. [Lists](#lists)
8. [Built-in Functions](#built-in-functions)
9. [File I/O](#file-io)
10. [Error Handling](#error-handling)
11. [Performance Tips](#performance-tips)
12. [Next Steps](#next-steps)

## Introduction

Flow is a simple, fast, and easy-to-learn programming language that compiles to efficient machine code using LLVM. It's designed to be intuitive for beginners while powerful enough for complex applications.

Key features of Flow:
- Simple C-like syntax
- Fast execution through LLVM compilation
- Rich standard library
- Built-in profiler and JIT caching

## Setting Up Flow

To get started with Flow:

1. Clone the repository:
   ```bash
   git clone https://github.com/Blank01442/Flow.git
   cd Flow
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run a Flow program:
   ```bash
   python -m flow.flow_cli program.flow
   ```

## Hello World

Let's start with the traditional "Hello, World!" program:

```flow
print "Hello, World!"
```

Save this in a file called `hello.flow` and run it with:
```bash
python -m flow.flow_cli hello.flow
```

## Variables and Data Types

Flow supports several data types:

### Numbers
```flow
let integer = 42
let float = 3.14159
```

### Strings
```flow
let greeting = "Hello, Flow!"
let multiline = "This is a
multiline string"
```

### Booleans
```flow
let isTrue = true
let isFalse = false
```

### Lists
```flow
let numbers = [1, 2, 3, 4, 5]
let mixed = ["text", 42, true]
```

## Control Flow

### If Statements
```flow
let age = 20

if age >= 18 {
    print "You are an adult"
} else {
    print "You are a minor"
}
```

### While Loops
```flow
let i = 0
while i < 5 {
    print "Count:", i
    i = i + 1
}
```

### For Loops (using range)
```flow
let numbers = range(5)  # [0, 1, 2, 3, 4]
for num in numbers {
    print "Number:", num
}
```

## Functions

Define functions with the `func` keyword:

```flow
func greet(name) {
    return "Hello, " + name + "!"
}

let message = greet("Flow")
print message
```

Functions can have multiple parameters:

```flow
func add(a, b) {
    return a + b
}

let sum = add(5, 3)
print "5 + 3 =", sum
```

## Lists

Lists are ordered collections of values:

```flow
# Create a list
let fruits = ["apple", "banana", "cherry"]

# Access elements
let first = fruits[0]
print "First fruit:", first

# Modify elements
fruits[0] = "orange"

# Add elements
append(fruits, "grape")

# Get list length
let count = len(fruits)
print "Number of fruits:", count

# Iterate through a list
for fruit in fruits {
    print "Fruit:", fruit
}
```

## Built-in Functions

Flow provides many useful built-in functions:

### String Functions
```flow
let text = "Hello, World!"
let length = len(text)           # 13
let parts = split(text, ",")     # ["Hello", " World!"]
```

### Math Functions
```flow
let power = pow(2, 3)    # 8
let root = sqrt(16)      # 4.0
let absolute = abs(-5)   # 5
```

### List Functions
```flow
let numbers = [1, 2, 3, 4, 5]
let sum = sum(numbers)      # 15
let maxVal = max(numbers)   # 5
let minVal = min(numbers)   # 1
```

### Utility Functions
```flow
let rangeList = range(5)       # [0, 1, 2, 3, 4]
let currentTime = time()       # Current timestamp
```

## File I/O

Read and write files with Flow's built-in functions:

```flow
# Write to a file
let content = "Hello, Flow!\nThis is a test file.\nIt has multiple lines."
write_file("test.txt", content)

# Read from a file
let readContent = read_file("test.txt")
print "File contents:"
print readContent

# Process file content
let lines = split(readContent, "\n")
let lineCount = len(lines)
print "Number of lines:", lineCount
```

## Error Handling

Flow is working on implementing error handling features. Currently, invalid operations will cause the program to terminate with an error message.

## Performance Tips

1. Use the built-in profiler to identify bottlenecks:
   ```bash
   python -m flow.flow_cli program.flow --profile
   ```

2. Enable JIT caching for faster startup:
   Flow automatically caches compiled functions for faster execution on subsequent runs

3. Use built-in functions when possible:
   Built-in functions are optimized and faster than custom implementations

4. Try the [Performance Comparison](performance-comparison.md) to see how Flow compares to other languages

## Next Steps

1. Explore the [examples directory](../examples/) for more sample programs
2. Read the [Quick Reference](quick-reference.md) for a syntax cheat sheet
3. Check the [Built-in Functions](built-in-functions.md) documentation for a complete list of available functions
4. Try the [Performance Comparison](performance-comparison.md) to see how Flow compares to other languages

Happy coding with Flow!