# Function to solve the 0/1 Knapsack problem
def knapsack_01(W, weights, values, n):
    # Create a 2D DP table to store maximum values for subproblems
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    # Build the DP table
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][W]  # The maximum value for capacity W with n items


W = int(input("Enter the knapsack capacity: ")) 
n = int(input("Enter the total number of items: "))

weights = []
values = []

print("Enter weight and value of each item:")
for _ in range(n):
    weight, value = map(int, input().split())
    weights.append(weight)
    values.append(value)

# Calculate the maximum value that can be stored in the knapsack
max_value = knapsack_01(W, weights, values, n)
print("\nMaximum value in knapsack is:", max_value)
