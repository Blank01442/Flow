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

## Variables and Types

### Variable Declaration

Variables are declared using the `let` keyword for immutable variables:

```flow
let name = "Flow"
let age = 5
let pi = 3.14159
```

For mutable variables, use the `mut` keyword:

```flow
mut counter = 0
counter = counter + 1
```

### Tuples

Flow supports tuples for grouping multiple values together:

```flow
# Creating a tuple
let point = (10, 20, 30)
print "Point:", point

# Accessing tuple elements
let x = point[0]
let y = point[1]
let z = point[2]
print "X:", x, "Y:", y, "Z:", z

# Tuple destructuring
let (a, b, c) = point
print "Destructured:", a, b, c
```

### Pattern Matching

Flow has powerful pattern matching capabilities using the `match` statement:

```flow
let value = 2
match value {
    case 0:
        print "Zero"
    case 1:
        print "One"
    case 2:
        print "Two"
    default:
        print "Other"
}
```

## Functions

Functions are declared using the `func` keyword:

```flow
func add(x, y) {
    return x + y
}

let result = add(5, 3)
print "Result:", result
```

### Generic-like Functions

Flow supports generic-like function syntax:

```flow
fn add[T](a: T, b: T) -> T {
    return a + b
}

let int_result = add[int](5, 3)
let float_result = add[float](3.14, 2.86)
```

## Control Flow

### If Statements

```flow
let temperature = 25

if temperature > 30 {
    print "It's hot!"
} else if temperature < 10 {
    print "It's cold!"
} else {
    print "It's pleasant."
}
```

### While Loops

```flow
mut i = 0
while i < 5 {
    print "Iteration:", i
    i = i + 1
}
```

### For Loops

```flow
# Range-based for loops
for i in range(5) {
    print "Index:", i
}

# For loops with lists
let fruits = ["apple", "banana", "cherry"]
for fruit in fruits {
    print "Fruit:", fruit
}
```

## Data Structures

### Lists

```flow
# Creating lists
let numbers = [1, 2, 3, 4, 5]
let empty_list = []

# List operations
append(numbers, 6)
let first = numbers[0]
numbers[0] = 10
```

### Dictionaries/Maps

```flow
# Creating dictionaries
let person = {"name": "Alice", "age": 30}
let empty_dict = {}

# Dictionary operations
person["city"] = "New York"
let name = person["name"]
```

## Memory Safety

Flow provides several memory safety features:

### Bounds Checking

```flow
let arr = [1, 2, 3]
# This will safely check bounds at runtime
let value = arr[5]  # Will raise an error instead of crashing
```

### Immutable by Default

```flow
let immutable_value = 42
# immutable_value = 43  # This would be a compile error

mut mutable_value = 42
mutable_value = 43  # This is allowed
```

## Error Handling

Flow provides safe error handling mechanisms:

```flow
# Pattern matching for error handling
match result {
    case Ok(value):
        print "Success:", value
    case Err(error):
        print "Error:", error
}
```

## Advanced Features

### Walrus Operator

The walrus operator `:=` allows assignment within expressions:

```flow
if (x := calculate_value()) > 10 {
    print "Value is large:", x
}
```

### Bitwise Operations

```flow
let a = 5  # Binary: 101
let b = 3  # Binary: 011
let and_result = a & b  # 1 (Binary: 001)
let or_result = a | b   # 7 (Binary: 111)
let xor_result = a ^ b  # 6 (Binary: 110)
```

## Built-in Functions

Flow includes a rich standard library with built-in functions:

```flow
# Mathematical functions
let root = sqrt(16)
let power = pow(2, 3)
let absolute = abs(-5)

# String functions
let length = len("Hello")
let parts = split("a,b,c", ",")

# List functions
let numbers = range(10)
let sum_result = sum(numbers)
```

## Performance Features

### Profiling

```bash
python -m flow.flow_cli program.flow --profile
```

### JIT Caching

Flow automatically caches compiled functions for faster startup on subsequent executions.