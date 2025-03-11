# 13. نام کاربر را به عنوان ورودی دریافت کند و اگر نام حاوی حرف "a" (چه کوچک یا بزرگ) باشد، پیام "حرف "a" در نام شماست را چاپ کند.

name = input("Enter your name: ")

if "a" in name.lower():  # برای بررسی غیرحساس به حروف کوچک، نام را تبدیل می کند
    print("The letter 'a' is in your name")
else:
    print("The letter 'a' is not in your name")

# Output
# Enter your name: Raymond
# The letter 'a' is in your name