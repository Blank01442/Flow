# Functional Programming

Flow provides built-in support for functional programming paradigms including first-class functions, closures, and higher-order functions.

## Built-in Functional Functions

### `map(func, iterable)`
Apply a function to each element in an iterable.

**Parameters:**
- `func` (function): Function to apply to each element
- `iterable` (list): List of elements to transform

**Returns:**
- New list with function applied to each element

### `filter(func, iterable)`
Filter elements in an iterable using a predicate function.

**Parameters:**
- `func` (function): Predicate function that returns true/false
- `iterable` (list): List of elements to filter

**Returns:**
- New list with only elements that satisfy the predicate

### `reduce(func, iterable, initial)`
Reduce elements in an iterable to a single value using a function.

**Parameters:**
- `func` (function): Function that takes two arguments and returns a single value
- `iterable` (list): List of elements to reduce
- `initial` (any, optional): Initial value for reduction

**Returns:**
- Single reduced value

## Lambda Expressions

Lambda expressions provide a concise way to create anonymous functions.

```flow
# Syntax: lambda(params) -> expression
let square = lambda(x) -> x * x
let result = square(5)  # 25
```

## Examples

```flow
# Create a list of numbers
let numbers = [1, 2, 3, 4, 5]

# Define functions
func square(x) {
    return x * x
}

func is_even(x) {
    return x % 2 == 0
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

# Using lambda expressions
let doubled = map(lambda(x) -> x * 2, numbers)
print "Doubled:", doubled
```

Note: Functional programming features are experimental and may have limited functionality.