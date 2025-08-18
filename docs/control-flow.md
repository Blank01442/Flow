# Control Flow

## If Statements

```flow
let age = 18

if age >= 18 {
    print "You are an adult"
} else {
    print "You are a minor"
}

# Multiple conditions
if age < 13 {
    print "Child"
} else if age < 20 {
    print "Teenager"
} else {
    print "Adult"
}
```

## While Loops

```flow
# Simple counter
let i = 0
while i < 5 {
    print "Count:", i
    i = i + 1
}

# More complex loop
let sum = 0
let n = 1
while n <= 10 {
    sum = sum + n
    n = n + 1
}
print "Sum:", sum
```