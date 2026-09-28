#ROLL NO.:CH.AI.U4AID25028
# 0/1 Knapsack using Dynamic Programming

def knapsack(weights, profits, n, capacity):
    # Create the DP table
    dp = [[0 for _ in range(capacity + 1)]
          for _ in range(n + 1)]

    # Fill the DP table
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):

            # Check if the current item can fit
            if weights[i - 1] <= w:

                # Include or exclude the current item
                include = profits[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]

                dp[i][w] = max(include, exclude)

            else:
                # Item cannot be included
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]


# Read input
n = int(input("Enter the number of items: "))

weights = list(map(int, input("Enter the weights: ").split()))

profits = list(map(int, input("Enter the profits: ").split()))

capacity = int(input("Enter the maximum capacity: "))

# Calculate maximum profit
maximum_profit = knapsack(weights, profits, n, capacity)

# Display result
print("\n0/1 Knapsack Result:")
print("Maximum profit:", maximum_profit)
print("Optimal solution found successfully.")