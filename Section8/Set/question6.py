# ایجاد یک set از مقادیر عددی
numbers_set = {1, 5, 10, 15, 20, 25, 30}

# عدد خاص برای فیلتر کردن
threshold = 15

# حذف مقادیر کمتر از عدد خاص
filtered_set = {num for num in numbers_set if num >= threshold}

# نمایش نتیجه
print("Set اولیه:", numbers_set)
print("Set بعد از فیلتر:", filtered_set)

# نمونه خروجی:
# Set اولیه: {1, 5, 10, 15, 20, 25, 30}
# Set بعد از فیلتر: {15, 20, 25, 30}
