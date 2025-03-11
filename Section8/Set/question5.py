# ایجاد یک set از اعداد
numbers_set = {1, 2, 3, 4, 5}

# محاسبه توان دوم هر عدد
squared_numbers = {num ** 2 for num in numbers_set}

# نمایش نتیجه
print("Set اولیه:", numbers_set)
print("Set بعد از توان دوم:", squared_numbers)

# نمونه خروجی:
# Set اولیه: {1, 2, 3, 4, 5}
# Set بعد از توان دوم: {1, 4, 9, 16, 25}
