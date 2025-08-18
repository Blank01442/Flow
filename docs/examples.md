# Examples

This document showcases various Flow programming examples that are verified to work correctly.

## Basic Examples

### Hello World
```flow
print "Hello, World!"
print "Welcome to Flow Programming!"
```

### Calculator
```flow
print "Simple Calculator"
let x = 10
let y = 5

print "x =", x
print "y =", y
print "x + y =", x + y
print "x - y =", x - y
print "x * y =", x * y
print "x / y =", x / y
```

## Control Flow Examples

### If Statements
```flow
let age = 18

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

### For Loops
```flow
# For loops with lists
for item in [1, 2, 3, 4, 5] {
    print "Item:", item
}

# Range-based for loops
for i in range(5) {
    print "Index:", i
}
```

## Data Structure Examples

### Lists
```flow
let fruits = ["apple", "banana", "cherry"]
print "Fruits:", fruits

# Accessing elements
let first = fruits[0]
print "First fruit:", first

# Modifying elements
fruits[0] = "orange"
print "Modified fruits:", fruits

# Adding elements
append(fruits, "grape")
print "Fruits with grape:", fruits
```

### Tuples
```flow
# Tuples provide a way to group multiple values
let point = (10, 20, 30)
print "Point:", point

# Accessing tuple elements
let x = point[0]
let y = point[1]
let z = point[2]
print "X:", x, "Y:", y, "Z:", z
```

## Function Examples

### Basic Functions
```flow
func greet(name) {
    return "Hello, " + name + "!"
}

let message = greet("Flow")
print message

func add(x, y) {
    return x + y
}

let sum = add(5, 3)
print "Sum:", sum
```

## Built-in Function Examples

### Math Functions
```flow
let value = 3.7
print "Original value:", value
print "floor(value):", floor(value)
print "ceil(value):", ceil(value)
print "round(value, 1):", round(value, 1)

let pi = 3.14159
print "Pi:", pi
print "round(pi, 2):", round(pi, 2)

let numbers = range(10)
print "Numbers:", numbers
let total = sum(numbers)
print "Sum of all numbers:", total
```

### String Functions
```flow
let char = "A"
print "Character:", char
print "Character for ASCII 65:", chr(65)

let number = 255
print "Number:", number
print "Hex representation:", hex(number)
print "Binary representation:", bin(number)
```

## Advanced Features

### Match Statements
```flow
# Match with integers
let value = 42
match value {
    case 0:
        print "Zero"
    case 1:
        print "One"
    case 42:
        print "The Answer to Life, the Universe, and Everything"
    default:
        print "Some other value"
}

# Match with strings
let status = "success"
match status {
    case "pending":
        print "Request is pending"
    case "success":
        print "Request succeeded"
    case "error":
        print "Request failed"
    default:
        print "Unknown status"
}
```

### Walrus Operator
```flow
# Simple assignment expression
if (x := 5) > 3 {
    print "x is", x, "which is greater than 3"
}

# Walrus operator with built-in functions
let text = "Hello, Flow!"
if (length := len(text)) > 10 {
    print "Text has", length, "characters, which is more than 10"
}
```

### Value Swapping
```flow
# Value swapping using a temporary variable
mut a = 10
mut b = 20
print "Before swap: a=", a, "b=", b
mut temp = a
a = b
b = temp
print "After swap: a=", a, "b=", b
```

### File I/O
```flow
# Write to file
write_file("test.txt", "Hello, Flow!\nThis is a test file.\nIt has multiple lines.")

# Read from file
let content = read_file("test.txt")
print "File content:"
print content
```

## Performance Examples

### Profiling
```flow
# Example function to profile
func fibonacci(n) {
    if n <= 1 {
        return n
    }
    return fibonacci(n - 1) + fibonacci(n - 2)
}

let result = fibonacci(10)
print "Fibonacci(10) =", result

# Run with --profile flag to see performance metrics:
# python -m flow.flow_cli program.flow --profile
```

These examples demonstrate Flow's features while maintaining simplicity and readability. All examples have been verified to parse and run correctly.