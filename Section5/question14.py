# 14. n و m محاسبه کرده و در اعداد را از یک لیست چاپ کنید

def min_max(numbers):
    return min(numbers), max(numbers)

# نمونه استفاده:
num_list = [3, 1, 4, 1, 5, 9]
minimum, maximum = min_max(num_list)
print(f"The smallest number is {minimum}, and the largest is {maximum}.")

# Output > The smallest number is 1, and the largest is 9.