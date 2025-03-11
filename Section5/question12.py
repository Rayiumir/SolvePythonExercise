# 12. تفاوت های بین یک عدد و عدد دیگر را بشمارید

def count_differences(a, b): # تفاوت بین دو عدد را می شمارد.
    return abs(a - b)

# نمونه استفاده:
num1 = 10
num2 = 5
print(f"The difference between {num1} and {num2} is {count_differences(num1, num2)}.")

# Output > The difference between 10 and 5 is 5.
