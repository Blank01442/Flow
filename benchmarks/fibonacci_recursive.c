#include <stdio.h>
#include <time.h>

long long fibonacci_recursive(int n) {
    if (n <= 1)
        return n;
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2);
}

int main() {
    int n = 30; // Use smaller number for recursive version
    clock_t start, end;
    double cpu_time_used;

    start = clock();
    long long result = fibonacci_recursive(n);
    end = clock();

    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;

    printf("Fibonacci(%d) = %lld\n", n, result);
    printf("C execution time: %f seconds\n", cpu_time_used);

    return 0;
}