# 7. یک فایل با سری اعداد ایجاد کنید، بزرگترین و کوچکترین اعداد را استخراج کنید.

# مرحله ۱: یک سری اعداد را در یک فایل بنویسید
numbers = [34, 12, 89, 56, 7, 99, 23, 45]

with open("numbers.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(map(str, numbers)))  # اعداد را به عنوان رشته، یک در هر خط ذخیره می کند

# مرحله ۲: اعداد را از فایل بخوانید
with open("numbers.txt", "r", encoding="utf-8") as file:
    numbers_list = [int(line.strip()) for line in file]  # هر خط را به یک عدد صحیح تبدیل می کند

# مرحله ۳: کوچکترین و بزرگترین اعداد را پیدا کنید
min_number = min(numbers_list)
max_number = max(numbers_list)

# Step 4: Print results
print(f"بزرگترین عدد: {max_number}")
print(f"کوچکترین عدد: {min_number}")

