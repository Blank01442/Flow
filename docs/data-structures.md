# Data Structures

Flow provides several built-in data structures to help you organize and manipulate data efficiently. The primary data structure in Flow is the list, which is similar to arrays in other languages.

## Lists

Lists are ordered collections that can hold any type of value, including other lists.

### Creating Lists

```flow
# Empty list
let emptyList = []

# List with values
let numbers = [1, 2, 3, 4, 5]
let mixed = ["text", 42, true, 3.14]

# List of lists (nested lists)
let matrix = [[1, 2], [3, 4], [5, 6]]
```

### Accessing List Elements

List elements are accessed using zero-based indexing:

```flow
let fruits = ["apple", "banana", "cherry"]
let first = fruits[0]   # "apple"
let second = fruits[1]  # "banana"
let last = fruits[2]    # "cherry"
```

### Modifying List Elements

You can change the value of a list element by assigning to its index:

```flow
let fruits = ["apple", "banana", "cherry"]
fruits[0] = "orange"  # fruits is now ["orange", "banana", "cherry"]
```

### List Functions

Flow provides several built-in functions for working with lists:

#### Adding Elements

```flow
let numbers = [1, 2, 3]
append(numbers, 4)     # numbers is now [1, 2, 3, 4]
```

#### Removing Elements

```flow
let numbers = [1, 2, 3, 4]
let last = pop(numbers)  # last = 4, numbers is now [1, 2, 3]
```

#### Getting List Length

```flow
let items = ["a", "b", "c"]
let count = len(items)  # count = 3
```

#### Creating Ranges

```flow
let range1 = range(5)         # [0, 1, 2, 3, 4]
let range2 = range(2, 8)      # [2, 3, 4, 5, 6, 7]
let range3 = range(0, 10, 2)  # [0, 2, 4, 6, 8]
```

### Iterating Over Lists

You can iterate over lists using for loops:

```flow
let fruits = ["apple", "banana", "cherry"]
for fruit in fruits {
    print "Fruit:", fruit
}
```

### List Comprehensions

While Flow doesn't have traditional list comprehensions, you can achieve similar results using loops:

```flow
# Create a list of squares
let numbers = [1, 2, 3, 4, 5]
let squares = []
for num in numbers {
    append(squares, num * num)
}
# squares is now [1, 4, 9, 16, 25]
```

### Common List Operations

#### Filtering

```flow
# Filter even numbers
let numbers = [1, 2, 3, 4, 5, 6]
let evens = []
for num in numbers {
    if num % 2 == 0 {
        append(evens, num)
    }
}
# evens is now [2, 4, 6]
```

#### Mapping

```flow
# Double each number
let numbers = [1, 2, 3, 4, 5]
let doubled = []
for num in numbers {
    append(doubled, num * 2)
}
# doubled is now [2, 4, 6, 8, 10]
```

#### Finding Elements

```flow
# Find first even number
func findFirstEven(numbers) {
    for num in numbers {
        if num % 2 == 0 {
            return num
        }
    }
    return null
}

let numbers = [1, 3, 4, 5, 7]
let firstEven = findFirstEven(numbers)  # firstEven = 4
```

## Working with Nested Lists

Lists can contain other lists, creating multi-dimensional structures:

```flow
# 2D list (matrix)
let matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements
let element = matrix[1][2]  # element = 6 (row 1, column 2)

# Iterating over a 2D list
for row in matrix {
    for element in row {
        print element
    }
}
```

## Performance Considerations

1. **Access by index** is very fast (O(1))
2. **Appending to the end** is generally fast (O(1) amortized)
3. **Inserting or removing from the middle** can be slow (O(n)) as elements need to be shifted
4. **Searching for an element** requires iterating through the list (O(n))

## Best Practices

1. **Use meaningful variable names** for lists and their elements
2. **Initialize lists with known values** when possible rather than starting with empty lists and appending
3. **Use `len()`** to check list length instead of maintaining separate counter variables
4. **Consider using `range()`** for simple numeric sequences
5. **Be careful with nested lists** - make sure to access the correct dimensions

## Examples

Here are some practical examples of working with data structures:

### Student Grades

```flow
# This example would use dictionaries/objects if they were implemented
# For now, you might represent structured data using lists with known indices:
# [name, grade1, grade2, grade3]
let students = [
    ["Alice", 85, 92, 78],
    ["Bob", 90, 88, 95],
    ["Charlie", 70, 82, 75]
]

# Calculate average grade for each student
for student in students {
    let name = student[0]
    let sum = student[1] + student[2] + student[3]
    let average = sum / 3
    print name, "average:", average
}
```

### Shopping Cart

```flow
# This example would use dictionaries/objects if they were implemented
# For now, you might represent structured data using lists with known indices:
# [item_name, price, quantity]
let cart = [
    ["apple", 0.5, 3],
    ["banana", 0.3, 5],
    ["orange", 0.7, 2]
]

let total = 0
for item in cart {
    let itemTotal = item[1] * item[2]  # price * quantity
    total = total + itemTotal
    print item[2], item[0], "at $", item[1], "each = $", itemTotal
}

print "Total: $", total
```

## Next Steps

After learning about data structures, explore:

1. [Built-in Functions](built-in-functions.md) for more functions to manipulate lists
2. [Examples](examples.md) to see data structures used in practice
3. [Performance Features](performance.md) to learn how to optimize your data structure usage