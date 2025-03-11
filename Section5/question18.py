# 18. تبدیل گرمای بدن انسان براساس دمای داده شده طبق یک فرمول

def calculate_f(c): # F را بر اساس فرمول داده شده محاسبه می کند: F = (9/5) * C + 32.
    return (9/5) * c + 32

# نمونه استفاده:
temperature_c = 25
temperature_f = calculate_f(temperature_c)
print(f"{temperature_c}C is {temperature_f}F.")

# Output > 25C is 77.0F.
