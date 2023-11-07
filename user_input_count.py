# Climbing Stairs with user input

def countWays(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    else:
        return countWays(n-1) + countWays(n-2)

# prompt user for input
steps = int(input("Enter number of steps: "))
ways = countWays(steps)
print("Number of ways = ", ways)
