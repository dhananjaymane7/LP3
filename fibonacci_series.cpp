#include <iostream>
using namespace std;

int main() {
    int n;
    cout << "\nEnter number of terms in the Fibonacci series: ";
    cin >> n;

    // Initial two Fibonacci numbers
    int n1 = 0;
    int n2 = 1;

    // Handle edge cases for n == 1 and n == 2
    if (n == 1) {
        cout << n1 << endl;
    } else if (n >= 2) {
        cout << n1 << " " << n2 << " ";

        // Print remaining terms for n > 2
        for (int i = 3; i <= n; i++) {
            int n3 = n1 + n2;
            cout << n3 << " ";
            n1 = n2;
            n2 = n3;
        }
        cout << endl;  // End the line after printing the series
    }

    return 0;
}
