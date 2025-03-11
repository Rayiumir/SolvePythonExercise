# 7. مقادیر مشترک در دو لیست

def common_elements(list1, list2):
    return list(set(list1) & set(list2))

# نمونه استفاده:
list1 = [1, 2, 3]
list2 = [3, 4, 5]
print("List New:", common_elements(list1, list2))

# Output > List New: [3]