# 11. دو عدد را به عنوان ورودی بگیرد و بررسی کند که مجموع آنها زوج است یا خیر.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

sum_of_numbers = num1 + num2

if sum_of_numbers % 2 == 0:
    print("The sum is even.")
else:
    print("The sum is odd.")

# Output
# Enter the first number: 20
# Enter the second number: 30
# The sum is even.