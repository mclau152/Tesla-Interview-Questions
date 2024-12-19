# Function to solve 0/1 Knapsack problem
def knapsack(weights, values, capacity):
    n = len(weights)
    
    # DP table where dp[i][j] represents the maximum value we can get with i items and j capacity
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            # If the current item can be included in the knapsack
            if weights[i - 1] <= w:
                # Choose the maximum between including or excluding the item
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                # Exclude the item if it's too heavy
                dp[i][w] = dp[i - 1][w]
    
    # The maximum value that can be carried in the knapsack
    return dp[n][capacity]

# Example
weights = [10, 20, 30]  # Weights of the items
values = [60, 100, 120]  # Values of the items
capacity = 50  # Capacity of the suitcase

max_value = knapsack(weights, values, capacity)
print("Maximum value that can be carried:", max_value)
