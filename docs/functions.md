# Functions

Functions are declared with the `func` keyword:

```flow
# Simple function
func greet(name) {
    return "Hello, " + name + "!"
}

let message = greet("Flow")
print message

# Function with multiple parameters
func add(a, b) {
    return a + b
}

let result = add(5, 3)
print "5 + 3 =", result

# Function with no return value
func sayHello() {
    print "Hello, World!"
}

sayHello()
```