# Flow Programming Language

Flow is a simple, fast, and easy-to-learn programming language that compiles to efficient machine code using LLVM. It's designed to be intuitive for beginners while powerful enough for complex applications.

## Features

- **Simple Syntax**: Clean, C-like syntax that's easy to read and write
- **Fast Execution**: Compiles to optimized machine code via LLVM
- **Rich Standard Library**: Built-in functions for strings, math, lists, file I/O, and more
- **Performance Tools**: Built-in profiler and JIT caching for optimization
- **Cross-Platform**: Runs on Windows, macOS, and Linux
- **Advanced Features**: Match statements, walrus operator, and more
- **Foreign Function Interface (FFI)**: Call C/C++ libraries directly
- **Concurrency Support**: Async/await, channels, and lightweight threads
- **Functional Programming**: Map, filter, reduce, and lambda expressions

## Performance

Flow offers significant performance improvements over Python:
- ~5x faster than Python for compute-intensive tasks
- Significantly slower than C (currently ~20x slower) but optimized for simplicity and safety
- Performance will improve in future versions

Recent benchmark results:
- Fibonacci(35): C (0.006s) vs Flow (0.131s) vs Python (0.067s)

## Quick Start

### Installation
```bash
pip install -r requirements.txt
```

### Easy Installation (Windows)
Run the `install.bat` script to automatically set up the `flow` command:
```bash
install.bat
```

### Hello World
Create a file called `hello.flow`:
```flow
print "Hello, World!"
```

Run it using the simple command:
```bash
flow hello.flow
```

Or using the traditional method:
```bash
python -m flow.flow_cli hello.flow
```

## Documentation

- [Documentation Index](docs/README.md) - Main documentation index
- [Getting Started](docs/getting-started.md) - Installation and basic usage
- [Performance Comparison](docs/performance-comparison.md) - C, Python, and Flow comparison
- [Quick Reference](docs/quick-reference.md) - Syntax cheat sheet
- [Examples](examples/) - Sample programs
- [Examples Documentation](docs/examples.md) - Detailed explanations of each example
- [Running Programs](docs/running-programs.md) - How to run Flow programs

## Key Language Features

### Variables
```flow
let name = "Flow"
let age = 5
let pi = 3.14159
```

### Control Flow
```flow
if age >= 18 {
    print "You are an adult"
} else {
    print "You are a minor"
}

let i = 0
while i < 5 {
    print "Count:", i
    i = i + 1
}

# For loops (new feature)
for item in [1, 2, 3, 4, 5] {
    print "Item:", item
}

# Range-based for loops (new feature)
for i in range(5) {
    print "Index:", i
}

# Match statements (new feature)
let value = 2
match value {
    case 1:
        print "One"
    case 2:
        print "Two"
    default:
        print "Other"
}
```

### Functions
```flow
func greet(name) {
    return "Hello, " + name + "!"
}

let message = greet("Flow")
print message
```

### Lists
```flow
let fruits = ["apple", "banana", "cherry"]
let first = fruits[0]
fruits[0] = "orange"
append(fruits, "grape")
```

### Built-in Functions
```flow
let length = len("Hello")        # 5
let root = sqrt(16)              # 4.0
let numbers = range(5)           # [0, 1, 2, 3, 4]
let words = split("a,b,c", ",")  # ["a", "b", "c"]

# New built-in functions
let floored = floor(3.7)         # 3
let ceiled = ceil(3.2)           # 4
let rounded = round(3.14159, 2)  # 3.14
let randomNum = random()         # Random float 0.0-1.0
```

### Bitwise Operations (new feature)
```flow
let a = 5  # Binary: 101
let b = 3  # Binary: 011
let andResult = a & b  # 1 (Binary: 001)
let orResult = a | b   # 7 (Binary: 111)
let xorResult = a ^ b  # 6 (Binary: 110)
```

### Walrus Operator (new feature)
```flow
# Assignment within expressions
if (x := 5) > 3 {
    print "x is", x, "which is greater than 3"
}

# Using walrus operator in a while loop
let data = [1, 2, 3, 4, 5]
let i = 0
while (value := data[i]) < 4 {
    print "Value is", value
    i = i + 1
}
```

### Foreign Function Interface (FFI)
```flow
# Load a system library
let lib = ffi_load("msvcrt.dll")  # Windows example

# Register a function signature
ffi_register("msvcrt.dll", "abs", "int", ["int"])

# Call a function
let result = ffi_call("msvcrt.dll", "abs", -5)
print "Absolute value of -5:", result
```

### Concurrency Features
```flow
# Async function example
async func fetch_data(url) {
    # Simulate async operation
    print "Fetching data from", url
    return "Data from " + url
}

# Await example
let data = await fetch_data("https://api.example.com")
print "Got data:", data
```

### Functional Programming
```flow
# Create a list of numbers
let numbers = [1, 2, 3, 4, 5]

# Define functions
func square(x) {
    return x * x
}

func is_even(x) {
    return x == 2 or x == 4
}

func add(acc, x) {
    return acc + x
}

# Map example - square each number
let squares = map(square, numbers)
print "Squares:", squares

# Filter example - keep only even numbers
let evens = filter(is_even, numbers)
print "Evens:", evens

# Reduce example - sum all numbers
let sum = reduce(add, numbers, 0)
print "Sum:", sum
```

## Performance Features

### Profiling
Analyze your program's performance:
```bash
flow program.flow --profile
```

### JIT Caching
Flow automatically caches compiled functions for faster startup.

## Examples

Check out the [examples directory](examples/) for sample programs:
- [Hello World](examples/hello.flow)
- [Calculator](examples/calculator.flow)
- [Fibonacci Sequence](examples/fibonacci.flow)
- [List Operations](examples/lists.flow)
- [File I/O](examples/fileio.flow)
- [Math Functions](examples/math.flow)
- [Pattern Matching](examples/match.flow)
- [Walrus Operator](examples/walrus.flow)
- [Enhanced Features](examples/enhanced.flow)
- [Comprehensive Example](examples/comprehensive.flow)
- [FFI Example](examples/ffi.flow)
- [Concurrency Example](examples/concurrency.flow)
- [Functional Programming Example](examples/functional.flow)

You can also view the [examples documentation](docs/examples.md) for detailed explanations of each example.

## Running Programs

### Simple Method (after installation)
```bash
# Run a Flow program
flow program.flow

# Run with profiling
flow program.flow --profile

# Start REPL
flow
```

### Traditional Method
```bash
# Run a Flow program
python -m flow.flow_cli program.flow

# Run with profiling
python -m flow.flow_cli program.flow --profile

# Start REPL
python -m flow.flow_cli
```

## Contributing

Flow is an open-source project. Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a pull request

## License

Flow is released under the MIT License. See LICENSE file for details.