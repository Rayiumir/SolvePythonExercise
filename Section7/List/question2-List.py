# 2. تعداد تکرار هر عدد در یک لیست

from collections import Counter

def count_occurrences(data):
    return dict(Counter(data))

# نمونه استفاده:
data = [1, 2, 2, 3, 3, 3]
print("Output: ", count_occurrences(data))

# Output > Output:  {1: 1, 2: 2, 3: 3}