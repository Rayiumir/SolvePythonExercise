# تعریف لیست دو بعدی
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# محاسبه مجموع هر سطر
row_sums = [sum(row) for row in matrix]

# محاسبه مجموع هر ستون
column_sums = [sum(matrix[row][col] for row in range(len(matrix))) for col in range(len(matrix[0]))]

# نمایش نتایج
print("مجموع هر سطر:", row_sums)
print("مجموع هر ستون:", column_sums)

# --------------------------
# خروجی:
# مجموع هر سطر: [6, 15, 24]
# مجموع هر ستون: [12, 15, 18]
# --------------------------
