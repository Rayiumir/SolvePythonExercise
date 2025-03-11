# ایجاد یک tuple شامل اعداد
numbers = (5, 12, 8, 20, 3, 15, 7)

# مقدار مشخص برای مقایسه
threshold = 10

# شمارش تعداد اعداد بزرگتر از مقدار مشخص
count = sum(1 for num in numbers if num > threshold)

# نمایش نتیجه
print("تعداد اعداد بزرگتر از", threshold, "در tuple:", count)

# نمونه خروجی:
# تعداد اعداد بزرگتر از 10 در tuple: 4
