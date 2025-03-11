# 12. سه عدد را به عنوان ورودی گرفته و بزرگترین عدد را نمایش دهد.

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

largest_number = max(num1, num2, num3)
print("The largest number is:", largest_number)

# Output
# Enter the first number: 20
# Enter the second number: 30
# Enter the third number: 40
# The largest number is: 40.0