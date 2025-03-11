import json

# آدرس فایل JSON
file_path = 'countries.json'

# خواندن داده‌ها از فایل JSON
with open(file_path, 'r', encoding='utf-8') as file:
    countries_data = json.load(file)

# استخراج کشورهایی که پایتخت آنها بیش از 10 حرف دارد
extracted_countries = [country['کشور'] for country in countries_data if len(country['پایتخت']) > 10]

# نمایش نتیجه
print("کشورهایی که پایتخت آنها بیش از 10 حرف دارد:")
for country in extracted_countries:
    print(country)

# نمونه خروجی (بسته به محتوای فایل JSON):
# کشورهایی که پایتخت آنها بیش از 10 حرف دارد:
# ایالات متحده
# برزیل
