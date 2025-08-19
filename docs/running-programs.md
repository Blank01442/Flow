# Running Flow Programs

You can now run Flow programs using the simple `flow` command instead of `python -m flow.flow_cli`.

## Usage

```bash
flow program.flow
```

## Examples

```bash
# Run a Flow program
flow examples/hello.flow

# Run with profiling
flow examples/fibonacci.flow --profile

# Start REPL
flow
```

## Installation

The `flow` command is available because:

1. A `flow.bat` script has been copied to your `C:\WINDOWS\system32\` directory
2. This directory is in your system PATH
3. The script automatically handles file paths and runs the Flow interpreter

## Notes

- You can run `flow` from any directory
- File paths can be relative or absolute
- All Flow CLI options are supported (e.g., `--profile`)

## Manual Installation (if automatic installation failed)

If the automatic installation didn't work, you can manually set up the `flow` command:

1. Copy `flow.bat` to `C:\WINDOWS\system32\flow.bat`
2. Make sure Python is in your PATH
3. Run `flow` from any directory

## Troubleshooting

If you get an error when running `flow`, try:

1. Make sure you've run `install.bat` as Administrator
2. Check that Python is installed and in your PATH
3. Restart your command prompt/terminal