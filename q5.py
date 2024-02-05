import numpy as np
import re # import regex module

# read input_question_5.txt
grid = []
with open("input_question_5.txt", "r") as f:
  for line in f.readlines():
    # use regex to split the line by non-digit characters
    grid.append(list(map(int, re.split(r'\D+', line.strip()))))

def greatest_product_in_grid(grid):
  max_product = 0
  rows = len(grid)
  cols = len(grid[0])

  # Check horizontal products:
  for i in range(rows):
    for j in range(cols - 3):
      product = grid[i][j] * grid[i][j + 1] * grid[i][j + 2] * grid[i][j + 3]
      max_product = max(max_product, product)

  # Check vertical products:
  for i in range(rows - 3):
    for j in range(cols):
      product = grid[i][j] * grid[i + 1][j] * grid[i + 2][j] * grid[i + 3][j]
      max_product = max(max_product, product)

  # Check diagonal products (downward):
  for i in range(rows - 3):
    for j in range(cols - 3):
      product = grid[i][j] * grid[i + 1][j + 1] * grid[i + 2][j + 2] * grid[i + 3][j + 3]
      max_product = max(max_product, product)

  # Check diagonal products (upward):
  for i in range(3, rows):
    for j in range(cols - 3):
      product = grid[i][j] * grid[i - 1][j + 1] * grid[i - 2][j + 2] * grid[i - 3][j + 3]
      max_product = max(max_product, product)

  return max_product

np.savetxt('output_question_5.txt', np.array([greatest_product_in_grid(grid)]), fmt='%d', delimiter=' ')