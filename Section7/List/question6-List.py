# 6. مجموع مقادیر عددی در یک لیست مقادیر متنی و عددی

def sum_numeric(data):
    numeric_sum = 0
    for item in data:
        if isinstance(item, (int, float)):
            numeric_sum += item
    return numeric_sum

# نمونه استفاده:
data = [1, "a", 2, "b", 3.14]
print("Sum of numeric values:", sum_numeric(data))

# Output > Sum of numeric values: 6.140000000000001