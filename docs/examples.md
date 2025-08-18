# Examples

## Hello World

```flow
print "Hello, World!"
```

## Calculator

```flow
func calculate(a, b, operation) {
    if operation == "add" {
        return a + b
    } else if operation == "subtract" {
        return a - b
    } else if operation == "multiply" {
        return a * b
    } else if operation == "divide" {
        return a / b
    } else {
        return "Unknown operation"
    }
}

let result = calculate(10, 5, "add")
print "10 + 5 =", result
```

## Fibonacci Sequence

```flow
func fibonacci(n) {
    if n < 2 {
        return n
    }
    return fibonacci(n - 1) + fibonacci(n - 2)
}

let fib10 = fibonacci(10)
print "Fibonacci(10) =", fib10
```

## File Processing

```flow
# Read and process a file
let content = read_file("data.txt")
let lines = split(content, "\n")
let lineCount = len(lines)
print "File has", lineCount, "lines"
```

## Working with Lists

```flow
# Create and manipulate a list
let scores = [85, 92, 78, 96, 88]
let average = sum(scores) / len(scores)
let highest = max(scores)
let lowest = min(scores)

print "Average:", average
print "Highest:", highest
print "Lowest:", lowest
```

## Match Statements

```flow
# Pattern matching example
let value = 2
match value {
    case 1:
        print "Value is one"
    case 2:
        print "Value is two"
    case 3:
        print "Value is three"
    default:
        print "Value is something else"
}
```

## Walrus Operator

```flow
# Assignment expressions example
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