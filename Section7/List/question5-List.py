# 5. اعداد شاخص های فرد را مرتب کنید

def sort_odd_indexed(data):
    odd_indexed = data[1::2]
    odd_indexed.sort()
    return odd_indexed

# نمونه استفاده:
data = [1, 2, 3, 4, 5, 6]
print("Sorted odd-indexed elements:", sort_odd_indexed(data))

# Output > Sorted odd-indexed elements: [2, 4, 6]