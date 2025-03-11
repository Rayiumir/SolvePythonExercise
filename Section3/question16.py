# 16. عددی را به عنوان ورودی می گیرد و بررسی می کند که آیا عدد بر 3 یا 5 بخش پذیر است یا خیر.

number = int(input("Enter a number: "))

if number % 3 == 0 or number % 5 == 0:
    print("The number is divisible by 3 or 5.")
else:
    print("The number is not divisible by 3 or 5.")

# Output
# Enter a number: 20
# The number is divisible by 3 or 5.