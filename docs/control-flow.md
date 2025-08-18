# Control Flow

Control flow structures allow you to control the execution path of your Flow programs. Flow provides conditional statements and loops to implement complex logic.

## If Statements

If statements allow you to execute code conditionally based on whether a condition is true or false.

### Basic If Statement

```flow
if condition {
    # code executed if condition is true
}
```

### If-Else Statement

```flow
if condition {
    # code executed if condition is true
} else {
    # code executed if condition is false
}
```

### If-Else If-Else Statement

```flow
if condition1 {
    # code executed if condition1 is true
} else if condition2 {
    # code executed if condition2 is true
} else {
    # code executed if neither condition is true
}
```

### Examples

```flow
let age = 20

if age >= 18 {
    print "You are an adult"
} else {
    print "You are a minor"
}

let score = 85

if score >= 90 {
    print "Grade: A"
} else if score >= 80 {
    print "Grade: B"
} else if score >= 70 {
    print "Grade: C"
} else {
    print "Grade: F"
}
```

### Nested If Statements

You can nest if statements inside other if statements:

```flow
let temperature = 75
let isSunny = true

if temperature > 70 {
    if isSunny {
        print "Perfect weather for outdoor activities!"
    } else {
        print "Nice temperature but cloudy"
    }
} else {
    print "It's a bit chilly today"
}
```

## Loops

Loops allow you to execute code repeatedly.

### While Loops

While loops continue executing as long as a condition is true:

```flow
while condition {
    # code executed repeatedly while condition is true
}
```

#### Examples

```flow
# Print numbers 1 to 5
let i = 1
while i <= 5 {
    print "Number:", i
    i = i + 1
}

# Calculate factorial
let n = 5
let factorial = 1
let counter = 1

while counter <= n {
    factorial = factorial * counter
    counter = counter + 1
}

print n, "! =", factorial
```

### For Loops

For loops iterate over elements in a list:

```flow
for item in list {
    # code executed for each item in the list
}
```

#### Examples

```flow
# Print each element in a list
let fruits = ["apple", "banana", "cherry"]
for fruit in fruits {
    print "Fruit:", fruit
}

# Calculate sum of numbers
let numbers = [1, 2, 3, 4, 5]
let total = 0
for num in numbers {
    total = total + num
}
print "Sum:", total

# Using range to create a loop
let rangeList = range(5)  # [0, 1, 2, 3, 4]
for i in rangeList {
    print "Index:", i
}
```

### Breaking Out of Loops

You can use the `break` statement to exit a loop early:

```flow
let i = 0
while true {
    if i >= 5 {
        break
    }
    print "Number:", i
    i = i + 1
}
```

### Skipping Iterations

You can use the `continue` statement to skip the rest of the current iteration and move to the next one:

```flow
# Print odd numbers only
let i = 0
while i < 10 {
    i = i + 1
    if i % 2 == 0 {
        continue
    }
    print "Odd number:", i
}
```

## Combining Control Structures

You can combine different control structures to implement complex logic:

```flow
# Find prime numbers
func isPrime(n) {
    if n < 2 {
        return false
    }
    
    let i = 2
    while i * i <= n {
        if n % i == 0 {
            return false
        }
        i = i + 1
    }
    return true
}

# Print prime numbers up to 20
let num = 2
while num <= 20 {
    if isPrime(num) {
        print num, "is prime"
    }
    num = num + 1
}
```

## Best Practices

1. **Keep conditions simple**: Complex conditions can be hard to read and debug. Consider breaking them into multiple simpler conditions.

2. **Use meaningful variable names**: In loops, use descriptive names like `index`, `counter`, or `item` instead of single letters when possible.

3. **Avoid deep nesting**: Deeply nested control structures can be difficult to follow. Consider refactoring complex nested structures into functions.

4. **Use for loops when possible**: When iterating over lists, for loops are generally more readable than while loops.

5. **Be careful with infinite loops**: Make sure your loop conditions will eventually become false, or use `break` to exit intentionally.

## Next Steps

After mastering control flow, explore:

1. [Functions](functions.md) to organize your code into reusable blocks
2. [Built-in Functions](built-in-functions.md) for useful functions that can simplify your control flow logic
3. [Examples](examples.md) to see control flow in practice