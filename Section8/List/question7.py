# تعریف دو لیست
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

# یافتن مقادیر مشترک
common_elements = list(set(list1) & set(list2))

# یافتن مقادیر غیرمشترک
unique_elements = list(set(list1) ^ set(list2))

# ترکیب مقادیر مشترک و غیرمشترک در یک لیست جدید
merged_list = common_elements + unique_elements

# نمایش نتیجه
print("مقادیر مشترک:", common_elements)
print("مقادیر غیرمشترک:", unique_elements)
print("لیست نهایی:", merged_list)

# نمونه خروجی:
# مقادیر مشترک: [4, 5, 6]
# مقادیر غیرمشترک: [1, 2, 3, 7, 8, 9]
# لیست نهایی: [4, 5, 6, 1, 2, 3, 7, 8, 9]
