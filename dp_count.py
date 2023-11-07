# Climbing Stairs with user input and dynamic programming

def countWays(n):
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

# prompt user for input
steps = int(input("Enter number of steps: "))
ways = countWays(steps)
print("Number of ways = ", ways)
