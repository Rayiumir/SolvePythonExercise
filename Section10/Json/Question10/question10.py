import json

# آدرس فایل JSON
file_path = 'strings.json'

# بارگذاری داده‌ها از فایل JSON
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# محاسبه طول هر رشته
lengths = [len(string) for string in data['رشته‌ها']]

# اضافه کردن طول رشته‌ها به داده‌ها
data['طول رشته‌ها'] = lengths

# ذخیره داده‌های به‌روز شده به فایل JSON
with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

# نمایش نتیجه (خروجی برای کاربر)
print("داده‌ها با موفقیت به‌روز شدند:")
print(data)
