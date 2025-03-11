# ایجاد یک set از اعداد
numbers_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# محاسبه مجموع اعداد زوج
even_sum = sum(num for num in numbers_set if num % 2 == 0)

# محاسبه مجموع اعداد فرد
odd_sum = sum(num for num in numbers_set if num % 2 != 0)

# نمایش نتیجه
print("مجموع اعداد زوج:", even_sum)
print("مجموع اعداد فرد:", odd_sum)

# نمونه خروجی:
# مجموع اعداد زوج: 30
# مجموع اعداد فرد: 25
