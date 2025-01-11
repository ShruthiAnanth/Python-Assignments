"""This is my traversals.py code"""

# Iterates over a 2D list from left to right, then top to bottom
# and returning the coordinates (row, column).
def row_major_traversal(grid):
    coordinates = []
    values = []
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            coordinates.append((row, col))
            values.append(grid[row][col])
    values = [grid[row][col] for row, col in coordinates]
    for val in values:
        print(val, end=" ")
    print()
    return []


# Iterates over a 2D list from left to right, then top to bottom
# and returning the coordinates (row, column).
def column_major_traversal(grid):
    coordinates = []
    values = []
    for col in range(len(grid[0])):
        for row in range(len(grid)):
            coordinates.append((row, col))
            values.append(grid[row][col])
    values = [grid[row][col] for row, col in coordinates]
    for val in values:
        print(val, end=" ")
    print()
    return []


# Iterates over a 2D list from top to bottom then left to right
# and returning the coordinates (row, column).
def row_zigzag_traversal(grid):
    coordinates = []
    values = []
    for row in range(len(grid)):
        if row % 2 == 0:
            for col in range(len(grid[0])):
                coordinates.append((row, col))
                values.append(grid[row][col])
        else:
            for col in range(len(grid[0]) - 1, -1, -1):
                coordinates.append((row, col))
                values.append(grid[row][col])
    values = [grid[row][col] for row, col in coordinates]
    for val in values:
        print(val, end=" ")
    print()
    return []


# Iterates over a 2D list by alternating between iterating
# left to right and right to left, going from top to bottom
# and returning the coordinates (row, column).
def column_zigzag_traversal(grid):
    coordinates = []
    values = []
    for col in range(len(grid[0])):
        if col % 2 == 0:
            for row in range(len(grid)):
                coordinates.append((row, col))
                values.append(grid[row][col])
        else:
            for row in range(len(grid) - 1, -1, -1):
                coordinates.append((row, col))
                values.append(grid[row][col])
    values = [grid[row][col] for row, col in coordinates]
    for val in values:
        print(val, end=" ")
    print()
    return []


# Iterates over a 2D list from the top-right to the bottom-left
# in the direction of the main diagonal and returning the
# coordinates (row, column).
def main_diagonal_traversal(grid):
    coordinates = []
    values = []
    for s in range(len(grid) + len(grid[0]) - 1):
        for row in range(len(grid)):
            col = row - (s - len(grid[0]) + 1)
            if 0 <= col < len(grid[0]):
                coordinates.append((row, col))
                values.append(grid[row][col])
    values = [grid[row][col] for row, col in coordinates]
    for val in values:
        print(val, end=" ")
    print()
    return []


# Iterates over a 2D list from the top-left to the bottom-right
# in the direction of the secondary diagonal and returning the
# coordinates (row, column).
def secondary_diagonal_traversal(grid):
    coordinates = []
    values = []
    for s in range(len(grid) + len(grid[0]) - 1):
        for row in range(len(grid)):
            col = s - row
            if 0 <= col < len(grid[0]):
                coordinates.append((row, col))
                values.append(grid[row][col])
    values = [grid[row][col] for row, col in coordinates]
    for val in values:
        print(val, end=" ")
    print()
    return []


# Iterates over a 2D list in spiral order and returning the
# coordinates (row, column).
def spiral_traversal(grid):
    values = []
    while grid:
        values += grid.pop(0)
        if grid and grid[0]:
            for row in grid:
                values.append(row.pop())
        if grid:
            values += grid.pop()[::-1]
        if grid and grid[0]:
            for row in grid[::-1]:
                values.append(row.pop(0))
    for val in values:
        print(val, end=" ")
    print()
    return []
