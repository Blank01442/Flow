# Functions

Functions are reusable blocks of code that perform specific tasks. In Flow, functions help organize your code, reduce repetition, and make your programs more modular.

## Defining Functions

Functions in Flow are defined using the `func` keyword:

```flow
func functionName(parameter1, parameter2, ...) {
    # function body
    # code to execute
    return value  # optional
}
```

### Simple Function

```flow
func greet() {
    print "Hello, World!"
}
```

### Function with Parameters

```flow
func greet(name) {
    print "Hello,", name
}
```

### Function with Return Value

```flow
func add(a, b) {
    return a + b
}
```

## Calling Functions

To execute a function, you call it by its name followed by parentheses:

```flow
# Call function without parameters
greet()

# Call function with parameters
greet("Flow")

# Call function and use return value
let sum = add(5, 3)
print "Sum:", sum
```

## Parameters and Arguments

Parameters are variables defined in the function declaration. Arguments are the actual values passed to the function when calling it.

### Multiple Parameters

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
print "Result:", result
```

### Default Parameters

Flow doesn't currently support default parameter values. All parameters must be provided when calling a function.

## Return Values

Functions can return values using the `return` statement. If no return statement is executed, the function returns `null`.

### Returning Different Types

```flow
func processNumber(n) {
    if n > 0 {
        return "positive"
    } else if n < 0 {
        return "negative"
    } else {
        return "zero"
    }
}

let result = processNumber(5)
print result  # "positive"
```

### Early Returns

You can use `return` to exit a function early:

```flow
func findFirstEven(numbers) {
    for num in numbers {
        if num % 2 == 0 {
            return num
        }
    }
    return null  # Return null if no even number found
}
```

## Scope

Variables defined inside a function are local to that function and cannot be accessed from outside:

```flow
func example() {
    let localVar = "I'm local"
    print localVar
}

example()
# print localVar  # This would cause an error
```

Variables defined outside functions are global and can be accessed from anywhere:

```flow
let globalVar = "I'm global"

func example() {
    print globalVar  # This works
}

example()
print globalVar  # This also works
```

## Nested Functions

Flow supports defining functions inside other functions:

```flow
func outerFunction() {
    func innerFunction() {
        print "I'm an inner function"
    }
    
    innerFunction()
}

outerFunction()
# innerFunction()  # This would cause an error as innerFunction is not accessible here
```

## Recursion

Functions can call themselves, which is known as recursion:

```flow
func factorial(n) {
    if n <= 1 {
        return 1
    }
    return n * factorial(n - 1)
}

let result = factorial(5)
print "5! =", result  # 5! = 120
```

## Higher-Order Functions

Functions can be passed as arguments to other functions:

```flow
func applyOperation(a, b, operation) {
    return operation(a, b)
}

func add(x, y) {
    return x + y
}

func multiply(x, y) {
    return x * y
}

let sum = applyOperation(5, 3, add)
let product = applyOperation(5, 3, multiply)

print "Sum:", sum       # Sum: 8
print "Product:", product  # Product: 15
```

## Best Practices

1. **Use descriptive names**: Function names should clearly indicate what the function does.

2. **Keep functions focused**: Each function should have a single, well-defined purpose.

3. **Limit parameters**: Functions with too many parameters can be difficult to use. Consider grouping related parameters into objects or lists.

4. **Use comments**: For complex functions, add comments explaining what the function does, its parameters, and its return value.

5. **Handle edge cases**: Consider what should happen with invalid inputs or edge cases.

6. **Avoid side effects**: Functions should ideally only depend on their parameters and not modify global variables when possible.

## Examples

Here are some practical examples of functions:

### Validation Function

```flow
func isValidEmail(email) {
    # Simple email validation
    return len(email) > 0 and email contains "@"
}

let email = "user@example.com"
if isValidEmail(email) {
    print "Valid email"
} else {
    print "Invalid email"
}
```

### Utility Function

```flow
func calculateArea(length, width) {
    return length * width
}

let area = calculateArea(10, 5)
print "Area:", area
```

## Next Steps

After learning about functions, explore:

1. [Built-in Functions](built-in-functions.md) for the rich set of functions that come with Flow
2. [Examples](examples.md) to see functions used in practice
3. [Error Handling](error-handling.md) to learn how to handle errors in functions