def pascal_triangle(n):
  """Generates Pascal's Triangle up to n rows."""
  triangle = []
  for i in range(n):
    row = [1] * (i + 1)
    if i > 1:
      for j in range(1, i):
        row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    triangle.append(row)
  return triangle

# Let's generate the first 5 rows
num_rows = 5
pt = pascal_triangle(num_rows)
for row in pt:
  print(row)