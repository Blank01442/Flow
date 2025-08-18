# Best Practices

## Use descriptive variable names

```flow
# Good
let studentCount = 25
let totalPrice = calculateTotal()

# Avoid
let x = 25
let t = calculateTotal()
```

## Comment your code

```flow
# Calculate the area of a circle
let area = 3.14159 * radius * radius
```

## Break complex logic into functions

```flow
# Good
func isEven(number) {
    return number % 2 == 0
}

if isEven(42) {
    print "42 is even"
}
```

## Use built-in functions when available

```flow
# Good
let total = sum(numbers)

# Avoid
let total = 0
let i = 0
while i < len(numbers) {
    total = total + numbers[i]
    i = i + 1
}
```