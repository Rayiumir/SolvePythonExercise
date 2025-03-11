# ایجاد tuple از اعداد
numbers = (10, 20, 30, 40, 50)

# محاسبه میانگین اعداد
average = sum(numbers) / len(numbers)

# ذخیره مقادیر بزرگتر از میانگین
greater_than_average = tuple(num for num in numbers if num > average)

# نمایش نتیجه
print("میانگین اعداد:", average)
print("مقادیر بزرگتر از میانگین:", greater_than_average)

# نمونه خروجی:
# میانگین اعداد: 30.0
# مقادیر بزرگتر از میانگین: (40, 50)
