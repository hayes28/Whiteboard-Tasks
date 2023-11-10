# Image Smoother Matrix
from math import floor

def image_smoother(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[List[int]]
    """
    # Get the dimensions of the matrix
    rows = len(matrix)
    cols = len(matrix[0])
    # Create a new matrix to store the smoothed values
    smoothed = [[0 for r in range(cols)] for c in range(rows)]
    # Iterate through the matrix
    for r in range(rows):
        for c in range(cols):
            # Get the sum of the surrounding values
            sum_values = 0
            count = 0
            for nr in range(r-1, r+2): # nr = neighber row
                for nc in range(c-1, c+2): # nc = neighbor column
                    if nr >= 0 and nr < rows and nc >= 0 and nc < cols:
                        sum_values += matrix[nr][nc]
                        count += 1
            # Get the average of the surrounding values
            smoothed[r][c] = floor(sum_values/count)
    # Return the smoothed matrix
    return smoothed

# Test Cases - Image to be smoothed
# 1. 3x3 matrix - can change the values to test
original_matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

# 2. 4x4 matrix
# original_matrix = [
#     [120, 140, 150, 100],
#     [156, 0, 174, 200],
#     [118, 192, 17, 180],
#     [100, 200, 150, 80]
# ]

# 3. 5x5 matrix
# original_matrix = [
#     [120, 140, 150, 100, 90],
#     [156, 0, 174, 200, 120],
#     [118, 192, 17, 180, 100],
#     [100, 200, 150, 80, 120],
#     [120, 140, 150, 100, 90]
# ]

# Call the function and print the result
smoothed_matrix = image_smoother(original_matrix)
print(smoothed_matrix)
