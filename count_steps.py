# Climbing Stairs

def countWays(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return countWays(n-1) + countWays(n-2)

steps = 5
ways = countWays(steps)
print("Number of ways = ", countWays(steps))
