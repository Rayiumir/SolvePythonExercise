# 20. عدد n از کاربر بگیرد و مجموع ارقام آن محاسبه کنید.

def calculate_s_condition(n, d_list): # S = sum(d_i) را برای i از 1 تا n محاسبه می کند اگر d_i < n باشد.
    return sum(di for di in d_list if di < n)

# نمونه استفاده:
d_values = [1, 2, 3, 4, 5]
n = 4
result = calculate_s_condition(n, d_values)
print(f"S = {result}")

# Output > S = 6