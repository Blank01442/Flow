# Flow Programming Language Quick Reference

This quick reference guide provides a concise overview of Flow's syntax and features.

## Hello World

```flow
print "Hello, World!"
```

## Variables

```flow
let name = "Flow"        # String (immutable)
mut age = 5              # Integer (mutable)
let pi = 3.14159         # Float
let isFast = true        # Boolean
let items = [1, 2, 3]     # List
let point = (10, 20)     # Tuple
```

## Functions

```flow
# Basic function
func greet(name) {
    return "Hello, " + name + "!"
}

# Function with multiple parameters
func add(x, y) {
    return x + y
}

# Generic-like function
fn multiply[T](a: T, b: T) -> T {
    return a * b
}
```

## Control Flow

### If Statements

```flow
if condition {
    # code
} else if other_condition {
    # code
} else {
    # code
}
```

### While Loops

```flow
mut i = 0
while i < 10 {
    print i
    i = i + 1
}
```

### For Loops

```flow
# Range-based for loop
for i in range(5) {
    print i
}

# List iteration
let fruits = ["apple", "banana", "cherry"]
for fruit in fruits {
    print fruit
}
```

## Pattern Matching

```flow
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

# Tuple pattern matching
match point {
    case (0, 0):
        print "Origin"
    case (x, 0):
        print "On X-axis:", x
    case (0, y):
        print "On Y-axis:", y
    case (x, y):
        print "Point:", x, y
}
```

## Data Structures

### Lists

```flow
let numbers = [1, 2, 3, 4, 5]
append(numbers, 6)     # Add element
let first = numbers[0] # Access element
numbers[0] = 10        # Modify element
let count = len(numbers) # Get length
```

### Tuples

```flow
let point = (10, 20, 30)
let x = point[0]
let (a, b, c) = point  # Destructuring
```

### Dictionaries

```flow
let person = {"name": "Alice", "age": 30}
person["city"] = "New York"
let name = person["name"]
```

## Operators

### Arithmetic
```flow
+  # Addition
-  # Subtraction
*  # Multiplication
/  # Division
%  # Modulo
** # Power
```

### Comparison
```flow
==  # Equal
!=  # Not equal
<   # Less than
<=  # Less than or equal
>   # Greater than
>=  # Greater than or equal
```

### Logical
```flow
and  # Logical AND
or   # Logical OR
not  # Logical NOT
```

### Bitwise
```flow
&  # Bitwise AND
|  # Bitwise OR
^  # Bitwise XOR
~  # Bitwise NOT
<< # Left shift
>> # Right shift
```

## Built-in Functions

### Mathematical
```flow
let root = sqrt(16)      # Square root
let power = pow(2, 3)    # Power
let absolute = abs(-5)   # Absolute value
let minimum = min(1, 2)  # Minimum
let maximum = max(1, 2)  # Maximum
let rounded = round(3.14) # Round
```

### String and List
```flow
let length = len("text")     # Length
let parts = split("a,b,c", ",") # Split string
let joined = join("-", ["a", "b", "c"]) # Join list
let range_list = range(5)    # Generate range
```

### I/O
```flow
let input_text = input("Enter text: ")  # Read input
let file_content = read_file("data.txt") # Read file
write_file("output.txt", "Hello")       # Write file
```

### Utility
```flow
let current_time = time()        # Current timestamp
sleep(1.5)                       # Sleep for 1.5 seconds
let random_float = random()      # Random float 0.0-1.0
let random_int = randint(1, 10)  # Random integer 1-10
```

## Memory Safety Features

### Immutable by Default
```flow
let immutable_value = 42  # Cannot be changed
mut mutable_value = 42     # Can be changed
```

### Bounds Checking
```flow
let arr = [1, 2, 3]
let safe_access = arr[5]  # Runtime bounds check
```

## Advanced Syntax

### Walrus Operator
```flow
if (x := calculate_value()) > 10 {
    print "Large value:", x
}
```

### Match Expressions
```flow
let result = match value {
    case 0: "zero"
    case 1: "one"
    default: "other"
}
```

## Command Line Usage

```bash
# Run a Flow program
python -m flow.flow_cli program.flow

# Run with profiling
python -m flow.flow_cli program.flow --profile

# Start REPL
python -m flow.flow_cli
```

## Performance Optimizations

- **JIT Caching**: Functions are cached for faster execution on subsequent runs
- **Profiling**: Built-in profiler for performance analysis
- **LLVM Backend**: Optional LLVM compilation for maximum speed (experimental)