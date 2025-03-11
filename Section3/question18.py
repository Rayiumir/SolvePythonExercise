# 18. سن کاربر را به عنوان ورودی دریافت کند و اگر سن کاربر بین 13 تا 19 سال باشد، پیام "شما یک نوجوان هستید" را چاپ کند.

age = int(input("Enter your age: "))

if 13 <= age <= 19:
    print("You are a teenager.")
else:
    print("You are not a teenager.")

# Output
# Enter your age: 19
# You are a teenager.