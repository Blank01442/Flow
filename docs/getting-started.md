# Getting Started with Flow

This guide will help you install and start using the Flow programming language.

## Prerequisites

Before installing Flow, ensure you have the following:

1. Python 3.7 or higher installed on your system
2. Git (for cloning the repository)
3. A text editor or IDE of your choice

## Installation

1. Clone the Flow repository:
   ```bash
   git clone https://github.com/Blank01442/Flow.git
   cd Flow
   ```

2. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Flow Programs

Flow programs have the `.flow` file extension. To run a Flow program:

```bash
python -m flow.flow_cli program.flow
```

For example, to run the included hello world example:
```bash
python -m flow.flow_cli examples/hello.flow
```

## Command Line Options

Flow supports several command line options:

- `--profile`: Run with profiling enabled to analyze performance
  ```bash
  python -m flow.flow_cli program.flow --profile
  ```

- `--help`: Display help information
  ```bash
  python -m flow.flow_cli --help
  ```

## Using the REPL

Flow includes a Read-Eval-Print Loop (REPL) for interactive programming:

```bash
python -m flow.flow_cli
```

In the REPL, you can:
- Type Flow expressions and see immediate results
- Define variables and functions
- Test code snippets

To exit the REPL, type `exit()` or press Ctrl+C.

## Hello World Example

Create a new file called `hello.flow` with the following content:

```flow
print "Hello, World!"
print "Welcome to Flow Programming!"
```

Run it with:
```bash
python -m flow.flow_cli hello.flow
```

You should see the output:
```
Hello, World!
Welcome to Flow Programming!
```

## Next Steps

After successfully running your first Flow program, explore:

1. The [tutorial](tutorial.md) for a comprehensive introduction to Flow
2. The [examples directory](../examples/) for sample programs
3. The [quick reference](quick-reference.md) for syntax reminders
4. The [built-in functions documentation](built-in-functions.md) for available functions

## Troubleshooting

If you encounter issues:

1. Ensure Python 3.7+ is installed and in your PATH
2. Verify all dependencies were installed with `pip install -r requirements.txt`
3. Check that you're running Flow from the correct directory

If you continue to have problems, please [open an issue](https://github.com/Blank01442/Flow/issues) on GitHub.