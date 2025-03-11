# 6. فایلی بسازید که شامل اسامی ۵ نفر باشد و سپس اسامی به ترتیب حروف الفبا مرتب کرده و در فایل ذخیره کنید.

# مرحله ۱ : نوشتن ۵ اسامی در یک فایل
names = ["زهرا", "احمد", "علی", "محمد", "سارا"]

with open("names.txt", "w", encoding="utf-8") as file:
    file.writelines("\n".join(names))

# مرحله ۲ : خواندن اسامی ها در یک فایل
with open("names.txt", "r", encoding="utf-8") as file:
    names_list = file.readlines()

# مرحله ۳ :  مرتب سازی براساس حروف الفبا
sorted_names = sorted([name.strip() for name in names_list])

# مرحله ۴ :  نوشتن اسامی ها براساس حروف الفبا در یک فایل جدید
with open("names_sorted.txt", "w", encoding="utf-8") as file:
    file.writelines("\n".join(sorted_names))

print("نام‌ها با موفقیت به ترتیب حروف الفبا مرتب و ذخیره شدند.")

