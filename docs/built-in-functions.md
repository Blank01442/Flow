# Built-in Functions

Flow comes with a rich set of built-in functions:

## String Functions

```flow
let text = "Hello, Flow!"
let length = len(text)        // 12
let numStr = str(42)          // "42"
let words = split("a,b,c", ",")  // ["a", "b", "c"]
let joined = join("-", ["a", "b", "c"])  // "a-b-c"

// Additional string functions
let asciiVal = ord("A")       // 65
let char = chr(65)            // "A"
let hexStr = hex(255)         // "0xff"
let binStr = bin(10)          // "0b1010"
```

## Mathematical Functions

```flow
let absolute = abs(-5)        // 5
let minimum = min(1, 2, 3)    // 1
let maximum = max(1, 2, 3)    // 3
let total = sum([1, 2, 3])    // 6
let numbers = range(5)       // [0, 1, 2, 3, 4]
let numbers_range = range(1, 6)  // [1, 2, 3, 4, 5]
let root = sqrt(16)          // 4.0
let power = pow(2, 3)         // 8
let logarithm = log(10)        // Natural log
let sine = sin(1.57)          // Sine of 1.57 radians
let cosine = cos(1.57)       // Cosine of 1.57 radians
let tangent = tan(1.57)       // Tangent of 1.57 radians
let floor_val = floor(3.7)   // 3
let ceil_val = ceil(3.2)     // 4
let rounded = round(3.14159, 2)  // 3.14
```

## List Functions

```flow
let fruits = ["apple", "banana"]
append(fruits, "cherry")     // fruits = ["apple", "banana", "cherry"]
let last = pop(fruits)        // "cherry", fruits = ["apple", "banana"]
let shuffled = shuffle([1, 2, 3, 4, 5])  // Randomly shuffled list
sort(fruits)                 // Sorts list in place
reverse(fruits)              // Reverses list in place
let has_item = contains(fruits, "apple")  // true/false
```

## I/O Functions

```flow
let content = read_file("data.txt")     // Read file content
write_file("output.txt", "Hello")       // Write to file
let userInput = input("Enter name: ")    // Read user input
let system_result = os_system("ls")      // Execute system command
```

## Time Functions

```flow
let current_time = time()    // Current timestamp
sleep(1.5)                   // Sleep for 1.5 seconds
```

## Random Functions

```flow
let random_float = random()     // Random float between 0.0 and 1.0
let random_int = randint(1, 10)  // Random integer between 1 and 10
```

## Utility Functions

```flow
let var_type = type(variable)   // Get variable type
let converted_int = int("42")     // Convert to integer
let converted_float = float("3.14")  // Convert to float
let converted_str = str(42)      // Convert to string
let parsed_json = json_parse("{\"key\": \"value\"}")  // Parse JSON
let json_str = json_stringify({"key": "value"})      // Convert to JSON
exit(0)                          // Exit program with code
```

## New Features with Recent Updates

### Tuple Support
```flow
// Tuples are supported as return values and can be destructured
let point = (10, 20)
let (x, y) = point
```

### Pattern Matching Functions
```flow
// Match statements provide powerful pattern matching
match value {
    case 0:
        print "Zero"
    case 1:
        print "One"
    default:
        print "Other"
}
```

### Memory Safety
```flow
// Bounds checking prevents buffer overflows
let arr = [1, 2, 3]
// arr[5] will raise a safe error instead of causing undefined behavior
```

### Immutable by Default
```flow
// Variables are immutable by default
let immutable_value = 42
// immutable_value = 43  // This would be prevented

// Use 'mut' for mutable variables
mut mutable_value = 42
mutable_value = 43  // This is allowed
```