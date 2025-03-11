# 16. معکوس یک عدد بدون استفاده از رشته

def reverse_integer(number): # یک عدد صحیح را بدون استفاده از تبدیل رشته معکوس می کند.
    reversed_number = 0
    sign = -1 if number < 0 else 1
    number = abs(number)

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10

    return reversed_number * sign


# نمونه استفاده
number = 12345
reversed_num = reverse_integer(number)
print(f"The reversed number is: {reversed_num}")

number = -12345
reversed_num = reverse_integer(number)
print(f"The reversed number is: {reversed_num}")

# Output
# The reversed number is: 54321
# The reversed number is: -54321

