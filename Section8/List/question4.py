# تابع برای بررسی اول بودن یک عدد
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# ایجاد لیستی از اعداد ۱ تا ۱۰۰
numbers = list(range(1, 101))

# فیلتر کردن اعداد اول
prime_numbers = [num for num in numbers if is_prime(num)]

# نمایش لیست اعداد اول
print("اعداد اول بین ۱ تا ۱۰۰:", prime_numbers)

# --------------------------
# خروجی:
# اعداد اول بین ۱ تا ۱۰۰: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# --------------------------
