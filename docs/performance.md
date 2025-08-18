# Performance Features

## Profiling

Flow includes a built-in profiler to analyze program performance:

```bash
python -m flow.flow_cli program.flow --profile
```

This will show:
- Total execution time
- Memory usage
- Function call statistics

## JIT Caching

Flow automatically caches compiled functions to improve startup time for repeated executions.