# 14. برنامه ای بنویسید که یک عدد صحیح را به عنوان ورودی بگیرد و اگر عدد فرد باشد آن را به عدد زوج بعدی تبدیل کرده و نمایش دهد.

number = int(input("Enter an integer: "))

if number % 2 != 0:  # بررسی می کند که آیا عدد فرد است یا خیر
    next_even = number + 1
    print("The next even number is:", next_even)
else:
    print("The number is already even.")

# Output
# Enter an integer: 1
# The next even number is: 2
