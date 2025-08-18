# Error Handling

Flow provides basic error handling through clear error messages:

```flow
# This will produce an error if the file doesn't exist
let content = read_file("nonexistent.txt")

# This will produce an error for undefined variables
print undefined_variable
```