# 20. سه عدد را به عنوان ورودی بگیرد و بررسی کند که مجموع آنها بین 100 تا 200 (شامل) است یا خیر. جواب بله یا خیر بدهید.

def check_sum_range():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        c = float(input("Enter the third number: "))

        sum_abc = a + b + c

        if 100 <= sum_abc <= 200:
            print("Yes")
        else:
            print("No")

    except ValueError:
        print("Invalid input. Please enter numbers only.")
check_sum_range()

# Output
# Enter the first number: 20
# Enter the second number: 30
# Enter the third number: 50
# Yes
