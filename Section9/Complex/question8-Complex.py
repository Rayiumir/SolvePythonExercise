# 8. یک فایل متنی حاوی لیستی از اعداد ایجاد کنید، سپس هر عدد زوج را با "عدد زوج" و هر عدد فرد را با "عدد فرد" جایگزین کنید.

# ایجاد لیستی از اعداد
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# ایجاد و نوشتن لیست اعداد در فایل
with open("numbers.txt", "w") as file:
    for number in numbers:
        file.write(f"{number}\n")

# خواندن لیست اعداد از فایل
with open("numbers.txt", "r") as file:
    numbers = file.readlines()

# جایگزینی اعداد زوج و فرد
modified_numbers = []
for number in numbers:
    num = int(number.strip())  # تبدیل به عدد صحیح
    if num % 2 == 0:
        modified_numbers.append("عدد زوج\n")
    else:
        modified_numbers.append("عدد فرد\n")

# نوشتن لیست تغییر یافته در فایل
with open("numbers.txt", "a") as file:
    file.write("\nلیست تغییر یافته:\n")
    file.writelines(modified_numbers)
