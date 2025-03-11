# 7. گرفتن عدد از عنوان ورودی و  بررسی می کند که آیا اولین رقم آن عدد بین 1 تا 10 است یا خیر.

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

number = input("Enter a number: ") # Taking input as string to easily access the first digit
first_digit = int(number[0])

if 1 <= first_digit <= 10:
    if is_prime(first_digit):
        print("The first digit is a prime number between 1 and 10")
    else:
        print("The first digit is not a prime number between 1 and 10")
else:
    print("The first digit is not between 1 and 10")

# Output
# Enter a number: 200
# The first digit is a prime number between 1 and 10