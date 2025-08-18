# Getting Started with Flow

## Installation

To run Flow programs, you need Python 3.9+ and the required dependencies:

```bash
pip install -r requirements.txt
```

## Running Flow Programs

```bash
# Run a Flow program
python -m flow.flow_cli program.flow

# Run with profiling
python -m flow.flow_cli program.flow --profile

# Start REPL
python -m flow.flow_cli
```

## Hello World

Create a file called `hello.flow`:

```flow
print "Hello, World!"
```

Run it:

```bash
python -m flow.flow_cli hello.flow
```