class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def fractional_knapsack(W, items):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=lambda item: item.value / item.weight, reverse=True)

    total_value = 0.0  # Total value in the knapsack
    for item in items:
        if W >= item.weight:  # Take the full item if it fits
            total_value += item.value
            W -= item.weight
        else:  # Take a fraction of the item that fits
            total_value += item.value * (W / item.weight)
            break

    return total_value

# Input knapsack capacity and items
W = int(input("Enter knapsack capacity: "))
n = int(input("Enter number of items: "))
items = []
print("Enter weight and value of each item:")
for _ in range(n):
    weight, value = map(int, input().split())
    items.append(Item(weight, value))

# Calculate the maximum value and print the result
max_value = fractional_knapsack(W, items)
print("Maximum value in knapsack =", max_value)
