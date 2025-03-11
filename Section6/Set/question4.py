# # روش اول

# تعریف دو set
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# محاسبه تفاوت set1 با set2 با استفاده از متد difference()
difference_set = set1.difference(set2)

# نمایش نتیجه
print("تفاوت set1 از set2:", difference_set)

# # روش دوم

# تعریف دو set
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# محاسبه تفاوت set1 با set2
difference_set = set1 - set2

# نمایش نتیجه
print("تفاوت set1 از set2:", difference_set)

# --------------------------
# خروجی:
# تفاوت set1 از set2: {10, 20}
# --------------------------
