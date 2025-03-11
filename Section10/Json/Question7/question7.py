import json

# آدرس فایل JSON که شامل لیست اعداد است
file_path = 'numbers.json'

# خواندن داده‌ها از فایل JSON
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# استخراج لیست اعداد از داده‌ها
numbers = data.get("numbers", [])

# محاسبه میانگین اعداد
if numbers:
    avg = sum(numbers) / len(numbers)
else:
    avg = 0

# اضافه کردن میانگین به داده‌های خوانده شده
data["average"] = avg

# ذخیره داده‌های به‌روز شده در همان فایل JSON
with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# نمایش نتیجه
print("میانگین اعداد:", avg)
print("داده‌های به‌روز شده:", data)


# نمونه محتویات اولیه فایل numbers.json:
# {
#     "numbers": [10, 20, 30, 40, 50]
# }
#
# نمونه خروجی پس از اجرای برنامه:
# میانگین اعداد: 30.0
# داده‌های به‌روز شده: {'numbers': [10, 20, 30, 40, 50], 'average': 30.0}

