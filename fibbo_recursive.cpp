#include <iostream>
using namespace std;

// Recursive function to find the nth Fibonacci number
int fibonacciRecursive(int n) {
    if (n <= 1)
        return n;
    return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
}

// Function to print Fibonacci sequence up to n terms
void printFibonacciSeries(int n) {
    for (int i = 0; i < n; i++) {
        cout << fibonacciRecursive(i) << " ";
    }
    cout << endl;
}

int main() {
    int n;
    cout << "Enter the number of terms in the Fibonacci series: ";
    cin >> n;

    cout << "Fibonacci series up to " << n << " terms: ";
    printFibonacciSeries(n);

    return 0;
}
