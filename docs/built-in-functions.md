# Built-in Functions

Flow comes with a rich set of built-in functions:

## String Functions

```flow
let text = "Hello, Flow!"
let length = len(text)        # 12
let numStr = str(42)          # "42"
let words = split("a,b,c", ",")  # ["a", "b", "c"]
let joined = join("-", ["a", "b", "c"])  # "a-b-c"
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
```

## List Functions

```flow
let numbers = [1, 2, 3]
append(numbers, 4)            # numbers is now [1, 2, 3, 4]
let last = pop(numbers)       # 4, numbers is now [1, 2, 3]

let range1 = range(5)         # [0, 1, 2, 3, 4]
let range2 = range(2, 8)      # [2, 3, 4, 5, 6, 7]
let range3 = range(0, 10, 2)  # [0, 2, 4, 6, 8]
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

## JSON Functions

```flow
# Parse JSON
let data = json_parse("{\"name\": \"Flow\", \"version\": 1.0}")

# Convert to JSON
let jsonString = json_stringify({"name": "Flow", "version": 1.0})
```