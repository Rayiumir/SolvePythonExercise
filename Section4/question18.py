# تابعی برای بررسی اول بودن یک عدد
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# شمارش اعداد اول
prime_count = 0
for i in range(1, 101):
    if is_prime(i):
        prime_count += 1

# نمایش تعداد اعداد اول
print("تعداد اعداد اول از 1 تا 100:", prime_count)

# --------------------------
# خروجی:
# تعداد اعداد اول از 1 تا 100: 25
# --------------------------
