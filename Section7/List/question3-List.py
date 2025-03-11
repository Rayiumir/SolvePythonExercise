# 3. لیست دو بعدی: مجموع سطرها و ستون ها

def sum_rows_cols(matrix):
    row_sums = [sum(row) for row in matrix]
    col_sums = [sum(matrix[i][j] for i in range(len(matrix))) for j in range(len(matrix[0]))]
    return row_sums, col_sums

# نمونه استفاده:
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
row_sums, col_sums = sum_rows_cols(matrix)
print("Row sums:", row_sums)
print("Column sums:", col_sums)

# Output 
# Row sums: [6, 15, 24]
# Column sums: [12, 15, 18]