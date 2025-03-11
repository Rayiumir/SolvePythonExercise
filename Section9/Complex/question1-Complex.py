# 1. یک فایل با نام دانش آموزان و نمرات آنها ایجاد کنید، سپس دانش آموزان با بالاترین امتیاز را چاپ کنید.

# نوشتن دیتای ساده
students = [
    "Ali - 85\n",
    "Sara - 90\n",
    "Reza - 78\n",
    "Mina - 95\n",
    "Omid - 95\n"
]

with open("students.txt", "w", encoding="utf-8") as file:
    file.writelines(students)

# خواندن و یافتن بالاترین نمره
with open("students.txt", "r", encoding="utf-8") as file:
    data = [line.strip().split(" - ") for line in file]

# تبدیل نمرات به اعداد صحیح
data = [(name, int(score)) for name, score in data]

# بالاترین امتیاز را پیدا می کند
max_score = max(data, key=lambda x: x[1])[1]

# چاپ دانش آموزان با بالاترین نمره
print("دانش‌آموزانی که بالاترین نمره را دارند:")
for name, score in data:
    if score == max_score:
        print(name)
