# 15. دو عدد را به عنوان ورودی بگیرد و بررسی کند که آیا هر دو عدد علامت یکسانی دارند (مثبت یا منفی).

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if (num1 > 0 and num2 > 0) or (num1 < 0 and num2 < 0):
    print("Both numbers have the same sign.")
else:
    print("The numbers have different signs.")

# Output
# Enter the first number: 5
# Enter the second number: 9
# Both numbers have the same sign.