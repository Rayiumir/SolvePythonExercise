# 5. گرفتن یک عدد از عنوان ورودی که بررسی کند که آیا آن عدد بر 5 بخش پذیر است یا خیر.

number = int(input("Enter a number: "))

if number % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

# Output
# Enter a number: 50
# Divisible by 5