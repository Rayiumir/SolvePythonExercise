# تعریف لیست از اعداد
numbers = [5, 12, 3, 19, 8, 2, 7]

# پیدا کردن بزرگترین و کوچکترین عدد
max_num = max(numbers)
min_num = min(numbers)

# جابجایی بزرگترین و کوچکترين عدد
max_index = numbers.index(max_num)
min_index = numbers.index(min_num)

# جایگزینی مقادیر
numbers[max_index], numbers[min_index] = min_num, max_num

# نمایش لیست تغییر یافته
print("لیست پس از جابجایی بزرگترین و کوچکترين عدد:", numbers)

# --------------------------
# خروجی:
# لیست پس از جابجایی بزرگترین و کوچکترين عدد: [5, 2, 3, 19, 8, 12, 7]
# --------------------------
