# # روش اول

# تعریف دو set
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# محاسبه اجتماع دو set با استفاده از متد union()
union_set = set1.union(set2)

# نمایش نتیجه
print("اتحاد دو set:", union_set)

# # روش دوم

# تعریف دو set
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# محاسبه اجتماع دو set با استفاده از عملگر |
union_set = set1 | set2

# نمایش نتیجه
print("اتحاد دو set:", union_set)

# --------------------------
# خروجی:
# اتحاد دو set: {70, 40, 50, 10, 20, 60, 30}
# --------------------------
