# 17. S را به صورت داده شده محاسبه کنید

def calculate_s(n, d_list): # S = sum(x_i) را برای i از 1 تا n محاسبه می کند.
    return sum(d_list)

# نمونه استفاده:
d_values = [1, 2, 3, 4, 5]
n = len(d_values)
result = calculate_s(n, d_values)
print(f"S = {result}")

# Output > S = 15