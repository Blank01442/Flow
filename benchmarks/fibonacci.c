#include <stdio.h>
#include <time.h>

long long fibonacci_iterative(int n) {
    if (n <= 1)
        return n;
    long long a = 0, b = 1, next;
    for (int i = 2; i <= n; i++) {
        next = a + b;
        a = b;
        b = next;
    }
    return b;
}

int main() {
    int n = 35; // Consistent value for benchmarking
    clock_t start, end;
    double cpu_time_used;

    start = clock();
    long long result = fibonacci_iterative(n);
    end = clock();

    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

    printf("Fibonacci(%d) = %lld\n", n, result);
    printf("C execution time: %f seconds\n", cpu_time_used);

    return 0;
}