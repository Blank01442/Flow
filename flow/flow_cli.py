import sys
import os
from pathlib import Path
import llvmlite.binding as llvm

from .lexer import Lexer
from .parser import Parser
from . import builtins
from .vm import VM  # Use VM instead of LLVM compiler for testing new features
from .profiler import global_profiler

CACHE_DIR = Path(__file__).parent.parent / "cache"
CACHE_DIR.mkdir(exist_ok=True)

def run_code(code, file_path=None, profile=False):
    # Start profiling if requested
    if profile:
        global_profiler.start()
    lexer = Lexer(code)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    ast = parser.parse()

    # Use VM for execution
    vm = VM()
    vm.run(ast.statements, [])  # Pass empty constants for now
        
    # Stop and report profiling if requested
    if profile:
        results = global_profiler.stop()
        print("\n=== Profiling Results ===")
        print(f"Total execution time: {results['total_time']:.4f} seconds")
        print(f"Initial memory usage: {results['initial_memory_mb']:.2f} MB")
        print(f"Final memory usage: {results['final_memory_mb']:.2f} MB")
        print(f"Memory delta: {results['memory_delta_mb']:.2f} MB")
        
        if results['function_calls']:
            print("\nFunction calls:")
            for func, count in sorted(results['function_calls'].items(), key=lambda x: x[1], reverse=True):
                print(f"  {func}: {count} calls")
                
        if results['function_times']:
            print("\nFunction times:")
            for func, time_spent in sorted(results['function_times'].items(), key=lambda x: x[1], reverse=True):
                print(f"  {func}: {time_spent:.4f} seconds")

def repl():
    print("Flow REPL (LLVM JIT enabled)") # Update REPL message
    print("Type 'exit' to quit")
    
    while True:
        try:
            line = input(">>> ")
            if line.strip() == "exit":
                break
            run_code(line)
        except EOFError:
            break
        except Exception as e:
            print(f"Error: {e}")

def main():
    # Check for profiling flag
    profile = False
    args = sys.argv[1:]
    
    if "--profile" in args:
        profile = True
        args.remove("--profile")
    
    if len(args) > 0:
        file_path = args[0]
        try:
            with open(file_path, 'r') as f:
                code = f.read()
            run_code(code, file_path=file_path, profile=profile)
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found")
        except Exception as e:
            print(f"Error: {e}")
    else:
        repl()

if __name__ == "__main__":
    main()