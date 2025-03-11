# 9. لیست دو بعدی: مقادیر سلول میانگین سطر و ستون است

def avg_matrix(rows, cols):
    matrix = [[(i + j) / 2 for j in range(cols)] for i in range(rows)]
    return matrix

# نمونه استفاده:
rows, cols = 3, 4
print("List:", avg_matrix(rows, cols))

# Output > List: [[0.0, 0.5, 1.0, 1.5], [0.5, 1.0, 1.5, 2.0], [1.0, 1.5, 2.0, 2.5]]