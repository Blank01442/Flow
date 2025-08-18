# Flow Programming Language

Flow is a simple, fast, and easy-to-learn programming language that compiles to efficient machine code using LLVM. It's designed to be intuitive for beginners while powerful enough for complex applications.

## Features

- **Simple Syntax**: Clean, C-like syntax that's easy to read and write
- **Fast Execution**: Compiles to optimized machine code via LLVM
- **Rich Standard Library**: Built-in functions for strings, math, lists, file I/O, and more
- **Performance Tools**: Built-in profiler and JIT caching for optimization
- **Cross-Platform**: Runs on Windows, macOS, and Linux

## Quick Start

### Installation
```bash
pip install -r requirements.txt
```

### Hello World
Create a file called `hello.flow`:
```flow
print "Hello, World!"
```

Run it:
```bash
python -m flow.flow_cli hello.flow
```

## Documentation

- [Documentation Index](docs/README.md) - Main documentation index
- [Getting Started](docs/getting-started.md) - Installation and basic usage
- [Performance Comparison](docs/performance-comparison.md) - C, Python, and Flow comparison
- [Quick Reference](docs/quick-reference.md) - Syntax cheat sheet
- [Examples](examples/) - Sample programs

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
```

## Performance Features

### Profiling
Analyze your program's performance:
```bash
python -m flow.flow_cli program.flow --profile
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

You can also view the [examples documentation](docs/examples.md) for detailed explanations of each example.

## Running Programs

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