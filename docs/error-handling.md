# Error Handling

Error handling in Flow allows you to gracefully handle unexpected situations in your programs. Flow provides a try/catch mechanism to manage errors and prevent your programs from crashing when issues occur.

## Try/Catch Blocks

Flow uses try/catch blocks to handle errors:

```flow
try {
    # Code that might cause an error
} catch error {
    # Code to handle the error
}
```

### Basic Error Handling

```flow
try {
    let result = 10 / 0
    print "Result:", result
} catch error {
    print "An error occurred:", error
}
```

### Handling Specific Errors

You can check the type or content of the error to handle different errors differently:

```flow
try {
    let content = read_file("nonexistent.txt")
    print content
} catch error {
    if error contains "not found" {
        print "File not found - using default content"
        let content = "Default content"
        print content
    } else {
        print "An unexpected error occurred:", error
    }
}
```

## Common Error Types

Flow can encounter several types of errors:

### 1. Division by Zero

```flow
try {
    let result = 10 / 0
} catch error {
    print "Cannot divide by zero"
}
```

### 2. File Not Found

```flow
try {
    let content = read_file("missing.txt")
} catch error {
    print "Could not read file:", error
}
```

### 3. Invalid List Index

```flow
try {
    let list = [1, 2, 3]
    let item = list[10]  # Index out of bounds
} catch error {
    print "Invalid list index"
}
```

### 4. Type Errors

```flow
try {
    let result = "text" + 5  # Type mismatch
} catch error {
    print "Type error:", error
}
```

## Throwing Errors

Currently, Flow doesn't have a built-in mechanism for throwing custom errors, but invalid operations will automatically result in errors that can be caught.

### Automatic Error Throwing

```flow
# These operations will automatically throw errors:
# - Division by zero
# - Accessing invalid list indices
# - Calling functions with incorrect parameters
# - File operations that fail
```

## Error Handling Best Practices

### 1. Handle Expected Errors

Handle errors that you anticipate might occur:

```flow
func safeDivide(a, b) {
    try {
        return a / b
    } catch error {
        print "Division error:", error
        return null
    }
}
```

### 2. Provide Meaningful Error Messages

Give users clear information about what went wrong:

```flow
func readFile(filename) {
    try {
        return read_file(filename)
    } catch error {
        print "Failed to read file '" + filename + "': " + error
        return null
    }
}
```

### 3. Fail Gracefully

When an error occurs, try to continue with alternative approaches:

```flow
let configFile = "config.txt"
let config = null

try {
    config = read_file(configFile)
} catch error {
    print "Config file not found, using defaults"
    config = "default_setting=true"
}
```

### 4. Log Errors

For debugging purposes, consider logging errors:

```flow
try {
    # Some operation
    let result = riskyOperation()
} catch error {
    # Log the error
    write_file("error.log", time() + ": " + error + "\n")
    # Handle the error
    print "Operation failed, using fallback"
}
```

## Nested Try/Catch

You can nest try/catch blocks to handle errors at different levels:

```flow
try {
    try {
        let result = 10 / 0
    } catch error {
        print "Inner catch:", error
        # Re-throw or handle differently
        throw error  # This would be a future feature
    }
} catch error {
    print "Outer catch:", error
}
```

## Error Handling in Functions

Functions should handle errors appropriately, either by:

1. Handling the error internally
2. Returning an error indicator
3. Allowing the error to propagate

```flow
# Function that handles errors internally
func safeSqrt(n) {
    try {
        return sqrt(n)
    } catch error {
        print "Cannot calculate square root of negative number"
        return null
    }
}

# Function that allows errors to propagate
func calculateRatio(a, b) {
    # If b is zero, the division error will propagate to the caller
    return a / b
}
```

## Validation Before Operations

Preventing errors is often better than handling them:

```flow
func divide(a, b) {
    if b == 0 {
        print "Error: Division by zero"
        return null
    }
    return a / b
}
```

## Error Handling in Loops

Handle errors that might occur during loop iterations:

```flow
let filenames = ["file1.txt", "file2.txt", "missing.txt"]
let contents = []

for filename in filenames {
    try {
        let content = read_file(filename)
        append(contents, content)
    } catch error {
        print "Could not read " + filename + ", skipping..."
    }
}
```

## Future Error Handling Features

In future versions of Flow, we plan to add:

1. Custom error throwing:
   ```flow
   # Future syntax (not yet implemented)
   if condition {
       throw "Custom error message"
   }
   ```

2. Finally blocks:
   ```flow
   # Future syntax (not yet implemented)
   try {
       # code
   } catch error {
       # handle error
   } finally {
       # cleanup code
   }
   ```

## Examples

Here's a complete example of error handling in a file processing application:

```flow
func processFile(filename) {
    print "Processing file:", filename
    
    try {
        # Try to read the file
        let content = read_file(filename)
        
        # Process the content
        let lines = split(content, "\n")
        let lineCount = len(lines)
        
        print "File has", lineCount, "lines"
        
        # Try to write to output file
        let output = "Processed: " + filename + " (" + str(lineCount) + " lines)\n"
        appendToFile("processed.log", output)
        
        return true
    } catch error {
        print "Error processing " + filename + ": " + error
        return false
    }
}

func appendToFile(filename, content) {
    try {
        let existing = read_file(filename)
        if existing == null {
            existing = ""
        }
        write_file(filename, existing + content)
    } catch error {
        print "Could not write to log file:", error
    }
}

# Process multiple files
let files = ["data1.txt", "data2.txt", "missing.txt"]
let successCount = 0

for file in files {
    if processFile(file) {
        successCount = successCount + 1
    }
}

print "Successfully processed", successCount, "out of", len(files), "files"
```

## Next Steps

After learning about error handling, explore:

1. [Examples](examples.md) to see error handling in practice
2. [Best Practices](best-practices.md) for overall coding guidelines
3. [Performance Features](performance.md) to learn about profiling and optimization