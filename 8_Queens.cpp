#include <iostream>
using namespace std;

const int N = 8;
int board[N][N] = {0};

bool isSafe(int row, int col) {
    // Check this row on left side
    for (int i = 0; i < col; i++)
        if (board[row][i])
            return false;

    // Check upper diagonal on left side
    for (int i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j])
            return false;

    // Check lower diagonal on left side
    for (int i = row, j = col; i < N && j >= 0; i++, j--)
        if (board[i][j])
            return false;

    return true;
}

bool solveNQueens(int col) {
    // If all queens are placed, return true
    if (col >= N)
        return true;

    for (int i = 0; i < N; i++) {
        if (isSafe(i, col)) {
            board[i][col] = 1; // Place queen

            if (solveNQueens(col + 1)) // Recur to place rest of the queens
                return true;

            board[i][col] = 0; // Backtrack
        }
    }
    return false;
}

void printBoard() {
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++)
            cout << (board[i][j] ? "Q " : ". ");
        cout << endl;
    }
}

int main() {
    if (solveNQueens(0)) {
        printBoard();
    } else {
        cout << "No solution exists";
    }
    return 0;
}
