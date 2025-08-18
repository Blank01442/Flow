# Language Basics

## Basic Syntax

Flow uses a clean, C-like syntax that's easy to read and write:

```flow
# This is a comment
print "Hello, World!"  # Print to console

# Variables
let name = "Flow"
let age = 5
let pi = 3.14159

# Basic operations
let result = 10 + 5 * 2  # 20
let isEqual = 10 < 20    # true
```

## Data Types

Flow supports several fundamental data types:

### Numbers
```flow
let integer = 42
let float = 3.14
let negative = -10
```

### Strings
```flow
let singleQuote = "Hello"
let multiWord = "Hello, World!"
```

### Booleans
```flow
let isTrue = true
let isFalse = false
```

### Lists
```flow
let emptyList = []
let numbers = [1, 2, 3, 4, 5]
let mixed = [1, "hello", 3.14]
```

## Variables

Variables in Flow are declared with the `let` keyword:

```flow
let name = "Flow"
let age = 5
let isActive = true

# Variables can be reassigned
name = "Flow Language"
```