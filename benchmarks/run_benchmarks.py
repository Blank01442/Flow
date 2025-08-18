import subprocess
import time
import os

def run_c_benchmark():
    print("--- Running C Benchmark ---")
    c_source_path = os.path.join(r"C:\Users\Administrator\Desktop\Flow\benchmarks", "fibonacci.c")
    c_executable_path = os.path.join(r"C:\Users\Administrator\Desktop\Flow\benchmarks", "fibonacci_c.exe") # .exe for Windows

    # Check if gcc is available
    try:
        subprocess.run(["gcc", "--version"], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Error: 'gcc' not found. Please install GCC and ensure it's in your system's PATH to run the C benchmark.\n")
        return

    # Compile C code
    compile_command = ["gcc", c_source_path, "-o", c_executable_path]
    compile_process = subprocess.run(compile_command, capture_output=True, text=True)
    if compile_process.returncode != 0:
        print("C Compilation Error:")
        print(compile_process.stderr)
        return

    # Run C executable
    start_time = time.time()
    run_process = subprocess.run([c_executable_path], capture_output=True, text=True)
    end_time = time.time()

    if run_process.returncode != 0:
        print("C Execution Error:")
        print(run_process.stderr)
        return

    print(run_process.stdout)
    print(f"Actual C execution time: {end_time - start_time:.4f} seconds\n")


def run_python_benchmark():
    print("--- Running Python Benchmark ---")
    run_command = ["python", "fibonacci.py"]
    start_time = time.time()
    run_process = subprocess.run(run_command, cwd=r"C:\Users\Administrator\Desktop\Flow\benchmarks", capture_output=True, text=True)
    end_time = time.time()

    if run_process.returncode != 0:
        print("Python Execution Error:")
        print(run_process.stderr)
        return

    print(run_process.stdout)
    print(f"Actual Python execution time: {end_time - start_time:.4f} seconds\n")

def run_flow_benchmark():
    print("--- Running Flow Benchmark ---")
    # Assuming 'flow.bat' is in the parent directory
    flow_cli_path = os.path.abspath(os.path.join(r"C:\Users\Administrator\Desktop\Flow", "flow.bat"))
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    flow_file_path = os.path.join(script_dir, "fibonacci.flow")
    run_command = [flow_cli_path, flow_file_path]
    start_time = time.time()
    run_process = subprocess.run(run_command, cwd=r"C:\Users\Administrator\Desktop\Flow\benchmarks", capture_output=True, text=True)
    end_time = time.time()

    if run_process.returncode != 0:
        print("Flow Execution Error:")
        print(run_process.stderr)
        return

    print(run_process.stdout)
    print(f"Actual Flow execution time: {end_time - start_time:.4f} seconds\n")


if __name__ == "__main__":
    run_c_benchmark()
    run_python_benchmark()
    run_flow_benchmark()
