import time

def fibonacci_iterative(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

if __name__ == "__main__":
    n = 35 # Consistent value for benchmarking
    start_time = time.time()
    result = fibonacci_iterative(n)
    end_time = time.time()

    print(f"Fibonacci({n}) = {result}")
    print(f"Python execution time: {end_time - start_time} seconds")