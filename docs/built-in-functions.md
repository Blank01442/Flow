# Built-in Functions

Flow comes with a rich set of built-in functions:

## String Functions

```flow
let text = "Hello, Flow!"
let length = len(text)        # 12
let numStr = str(42)          # "42"
let words = split("a,b,c", ",")  # ["a", "b", "c"]
let joined = join("-", ["a", "b", "c"])  # "a-b-c"

# Additional string functions
let asciiVal = ord("A")       # 65
let char = chr(65)            # "A"
let hexStr = hex(255)         # "0xff"
let binStr = bin(10)          # "0b1010"
```

## Mathematical Functions

```flow
let absolute = abs(-42)       # 42
let minimum = min(10, 5, 8)   # 5
let maximum = max(10, 5, 8)   # 10
let total = sum([1, 2, 3])    # 6
let root = sqrt(16)           # 4.0
let power = pow(2, 3)         # 8
let logarithm = log(2.718)    # ~1.0
let sine = sin(3.14159/2)     # ~1.0

# Additional math functions
let floored = floor(3.7)      # 3
let ceiled = ceil(3.2)        # 4
let rounded = round(3.14159, 2)  # 3.14
```

## List Functions

```flow
let numbers = [1, 2, 3]
append(numbers, 4)            # numbers is now [1, 2, 3, 4]
let last = pop(numbers)       # 4, numbers is now [1, 2, 3]

let range1 = range(5)         # [0, 1, 2, 3, 4]
let range2 = range(2, 8)      # [2, 3, 4, 5, 6, 7]
let range3 = range(0, 10, 2)  # [0, 2, 4, 6, 8]

# Additional list functions
let items = [3, 1, 4, 1, 5]
sort(items)                   # items is now [1, 1, 3, 4, 5]
reverse(items)                # items is now [5, 4, 3, 1, 1]
let hasFive = contains(items, 5)  # true
```

## Time Functions

```flow
let now = time()              # Current timestamp
sleep(2)                      # Pause for 2 seconds
```

## File I/O Functions

```flow
# Read a file
let content = read_file("example.txt")

# Write to a file
write_file("output.txt", "Hello, File!")

# Execute system commands
os_system("echo Hello from system")
```

## Random Functions

```flow
let randomFloat = random()        # Random float between 0.0 and 1.0
let randomInt = randint(1, 10)    # Random integer between 1 and 10
let items = [1, 2, 3, 4, 5]
shuffle(items)                    # Shuffle the list in place
```

## Type and Conversion Functions

```flow
let typeName = type(42)           # "int"
let typeName2 = type("text")      # "str"
let intValue = int("42")          # 42
let floatValue = float("3.14")    # 3.14
```

## Input/Output Functions

```flow
let userInput = input("Enter your name: ")
print "Hello,", userInput
exit(0)  # Exit program with code 0
```