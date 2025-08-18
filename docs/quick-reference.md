# Flow Programming Language Quick Reference

This quick reference guide provides a concise overview of Flow's syntax and features.

## Hello World

```flow
print "Hello, World!"
```

## Variables

```flow
let name = "Flow"        # String
let age = 5              # Integer
let pi = 3.14159         # Float
let isFast = true        # Boolean
let items = [1, 2, 3]    # List
```

## Control Flow

### If Statements

```flow
if condition {
    # code
} else if otherCondition {
    # code
} else {
    # code
}
```

### While Loops

```flow
while condition {
    # code
}
```

### For Loops

```flow
for item in list {
    # code
}

# With range
for i in range(5) {
    # code
}
```

### Match Statements (Pattern Matching)

```flow
match value {
    case pattern1:
        # code
    case pattern2:
        # code
    default:
        # code
}
```

## Functions

```flow
func functionName(param1, param2) {
    # code
    return value
}

# Call function
let result = functionName(arg1, arg2)
```

## Lists

```flow
let list = [1, 2, 3]     # Create list
let item = list[0]       # Access item
list[0] = 5              # Modify item
append(list, 4)          # Add item
let length = len(list)   # Get length
```

## Built-in Functions

### String Functions
- `len(string)` - Get string length
- `split(string, delimiter)` - Split string into list
- `substr(string, start, length)` - Extract substring
- `ord(char)` - Get ASCII value of character
- `chr(number)` - Get character from ASCII value
- `hex(number)` - Convert to hexadecimal string
- `bin(number)` - Convert to binary string

### Math Functions
- `abs(number)` - Absolute value
- `pow(base, exponent)` - Power function
- `sqrt(number)` - Square root
- `sin(number)` - Sine
- `cos(number)` - Cosine
- `tan(number)` - Tangent
- `log(number)` - Natural logarithm
- `floor(number)` - Round down
- `ceil(number)` - Round up
- `round(number, decimals)` - Round to specified decimals

### List Functions
- `len(list)` - Get list length
- `append(list, item)` - Add item to list
- `sum(list)` - Sum of numbers in list
- `max(list)` - Maximum value in list
- `min(list)` - Minimum value in list
- `range(count)` - Create list [0, 1, ..., count-1]
- `sort(list)` - Sort list in place
- `reverse(list)` - Reverse list in place
- `contains(list, item)` - Check if item is in list

### File I/O Functions
- `read_file(filename)` - Read file contents
- `write_file(filename, content)` - Write content to file

### Random Functions
- `random()` - Generate random float 0.0-1.0
- `randint(min, max)` - Generate random integer
- `shuffle(list)` - Shuffle list in place

### Type and Conversion Functions
- `type(value)` - Get type of value
- `str(value)` - Convert to string
- `int(value)` - Convert to integer
- `float(value)` - Convert to float

### Input/Output Functions
- `input(prompt)` - Get user input
- `exit(code)` - Exit program

### System Functions
- `time()` - Get current timestamp
- `os_system(command)` - Execute system command

## Operators

### Arithmetic
- `+` - Addition
- `-` - Subtraction
- `*` - Multiplication
- `/` - Division
- `%` - Modulo
- `**` - Power

### Comparison
- `==` - Equal
- `!=` - Not equal
- `<` - Less than
- `<=` - Less than or equal
- `>` - Greater than
- `>=` - Greater than or equal

### Logical
- `and` - Logical AND
- `or` - Logical OR
- `not` - Logical NOT

### Bitwise
- `&` - Bitwise AND
- `|` - Bitwise OR
- `^` - Bitwise XOR

### Assignment Expression (Walrus Operator)
- `:=` - Assignment within expressions

## Comments

```flow
# This is a single-line comment

# Multi-line comments are just multiple
# single-line comments
```

## Program Structure

```flow
# Global variables
let globalVar = "value"

# Functions
func myFunction() {
    # function body
}

# Main code
print "Program starts here"
```