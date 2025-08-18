# Data Structures

## Lists

Lists are ordered collections that can hold any type of data:

```flow
# Creating lists
let empty = []
let numbers = [1, 2, 3]
let mixed = [1, "hello", 3.14, true]

# Accessing elements
let first = numbers[0]        # 1
let second = numbers[1]       # 2

# Modifying elements
numbers[0] = 10               # numbers is now [10, 2, 3]

# List operations
append(numbers, 4)            # Add element
let last = pop(numbers)       # Remove and return last element
let size = len(numbers)       # Get list length
```