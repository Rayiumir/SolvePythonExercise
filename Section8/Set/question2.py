import random

# ایجاد یک set با مقادیر تصادفی
my_set = {random.randint(1, 100) for _ in range(10)}

# تبدیل set به لیست و مرتب کردن آن
sorted_list = sorted(list(my_set))

# نمایش نتیجه
print("Set اصلی:", my_set)
print("لیست مرتب شده:", sorted_list)

# نمونه خروجی:
# Set اصلی: {1, 3, 5, 7, 9, 11, 13, 15, 17, 19}
# لیست مرتب شده: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
