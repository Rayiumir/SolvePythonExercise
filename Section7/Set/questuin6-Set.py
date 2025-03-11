# 6. یک ست ایجاد کنید و مقادیر کوچکتر از یک عدد داده شده را پیدا کنید

numbers = {3, 8, 12, 5, 7, 2, 10, 15}
threshold = 8

small_values = {num for num in numbers if num < threshold}
print(small_values)

# Output > {2, 3, 5, 7}
