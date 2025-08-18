# Performance Features

Flow includes several built-in performance features to help you write fast, efficient programs. These tools allow you to analyze, optimize, and cache your code for better execution speed.

## Profiling

Flow's built-in profiler helps you identify performance bottlenecks in your programs by measuring how much time is spent in each function.

### Using the Profiler

To run your program with profiling enabled, use the `--profile` flag:

```bash
python -m flow.flow_cli program.flow --profile
```

### Profiler Output

The profiler will display a report showing:
1. The time spent in each function
2. The number of times each function was called
3. The average time per function call

Example profiler output:
```
Profiling Results:
Function 'fibonacci' called 2972 times, total time: 0.023s (0.000008s per call)
Function 'main' called 1 time, total time: 0.001s (0.001s per call)
```

### Interpreting Profiler Results

- **High call count**: Functions called many times might benefit from optimization
- **High total time**: Functions taking the most total time are good optimization targets
- **High time per call**: Functions that are slow individually should be examined

### Profiling Example

Let's profile a simple program:

```flow
func fibonacci(n) {
    if n < 2 {
        return n
    }
    return fibonacci(n - 1) + fibonacci(n - 2)
}

func main() {
    let result = fibonacci(20)
    print "Fibonacci(20) =", result
}

main()
```

Run with:
```bash
python -m flow.flow_cli fibonacci.flow --profile
```

## JIT Caching

Flow automatically caches compiled functions to improve startup time for subsequent runs. This Just-In-Time (JIT) compilation means that after the first execution, functions will load faster from cache.

### How JIT Caching Works

1. Flow compiles functions to optimized bytecode on first execution
2. Compiled functions are stored in the cache directory
3. On subsequent runs, Flow loads pre-compiled functions from cache
4. Only modified functions are recompiled

### Cache Location

The JIT cache is stored in the `cache/jit/` directory in your Flow installation.

### Cache Benefits

- Faster startup times for repeated executions
- Improved performance for frequently used functions
- Automatic cache invalidation when source code changes

### Cache Management

Flow automatically manages the JIT cache, but you can manually clear it if needed:

```bash
# Remove cache directory to force recompilation
rm -rf cache/jit/
```

## Optimization Techniques

### 1. Use Built-in Functions

Built-in functions are implemented in optimized code and are faster than equivalent Flow implementations:

```flow
# Slow: Custom implementation
func sumList(list) {
    let total = 0
    for item in list {
        total = total + item
    }
    return total
}

# Fast: Built-in function
let total = sum(list)
```

### 2. Minimize Function Calls in Loops

Function call overhead can add up in loops:

```flow
# Less efficient
for i in range(1000) {
    let result = expensiveFunction(i)
    # process result
}

# More efficient (if possible)
let data = prepareData()
for i in range(1000) {
    let result = processData(data, i)
    # process result
}
```

### 3. Use Appropriate Data Structures

Choose the right data structure for your use case:

```flow
# For frequent lookups, consider using a map/dictionary if implemented
# For sequential access, lists are appropriate
# For unique items, consider a set if implemented
```

### 4. Avoid Unnecessary Work

Move calculations outside of loops when possible:

```flow
# Inefficient
for i in range(1000) {
    let result = complexCalculation() * i
    # process result
}

# More efficient
let baseValue = complexCalculation()
for i in range(1000) {
    let result = baseValue * i
    # process result
}
```

## Performance Comparison

Flow's performance significantly exceeds Python while being slower than C. Current benchmarks show Flow is approximately 5x faster than Python and 20x slower than C for compute-intensive tasks. Flow prioritizes simplicity, safety, and ease of use over maximum performance. See the [Performance Comparison](performance-comparison.md) document for detailed benchmarks.

## Best Practices

1. **Profile first**: Use the profiler to identify actual bottlenecks before optimizing
2. **Focus on hot paths**: Optimize code that runs frequently or takes significant time
3. **Use built-ins**: Leverage Flow's optimized built-in functions
4. **Cache wisely**: Take advantage of Flow's automatic JIT caching
5. **Measure improvements**: Always measure the impact of optimizations

## Advanced Profiling

For more detailed analysis, you can create custom timing functions:

```flow
func timeFunction(func, ...args) {
    let startTime = time()
    let result = func(...args)
    let endTime = time()
    print "Function took", endTime - startTime, "seconds"
    return result
}
```

## Next Steps

After learning about performance features, explore:

1. [Performance Comparison](performance-comparison.md) for benchmarks against other languages
2. [Built-in Functions](built-in-functions.md) to learn about optimized functions
3. [Examples](examples.md) to see performance features in practice