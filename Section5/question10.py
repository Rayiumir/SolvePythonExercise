# 10. بزرگترین عامل یک عدد را پیدا کنید:

def largest_factor(num): # بزرگترین عامل یک عدد (به استثنای خود عدد) را پیدا می کند.
    for i in range(num // 2, 0, -1):  # از num/2 به سمت پایین تکرار می کند
        if num % i == 0:
            return i
    return 1  # اگر هیچ عامل دیگری یافت نشد، 1 بزرگترین عامل است

# نمونه استفاده
number = 28
largest_factor_num = largest_factor(number)
print(f"The largest factor of {number} is {largest_factor_num}")

# Output > The largest factor of 28 is 14
