import json

# آدرس فایل JSON
file_path = "cities.json"

# خواندن داده‌ها از فایل JSON
with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

# استخراج شهرهایی که جمعیتشان بیشتر از ۵۰۰۰۰۰ است
extracted_cities = [city["name"] for city in data["cities"] if city["population"] > 500000]

# نمایش نتیجه
print("شهرهایی که جمعیتشان بیشتر از ۵۰۰۰۰۰ است:")
for city in extracted_cities:
    print(city)

# --------------------------
# محتوای نمونه فایل cities.json:
# {
#     "cities": [
#         {"name": "تهران", "population": 9000000},
#         {"name": "اصفهان", "population": 2000000},
#         {"name": "شیراز", "population": 1500000},
#         {"name": "مشهد", "population": 3000000},
#         {"name": "تبریز", "population": 1600000},
#         {"name": "یزد", "population": 300000},
#         {"name": "کرمان", "population": 500000},
#         {"name": "بندرعباس", "population": 400000},
#         {"name": "رشت", "population": 500000},
#         {"name": "اردبیل", "population": 600000}
#     ]
# }
#
# نمونه خروجی:
# شهرهایی که جمعیتشان بیشتر از ۵۰۰۰۰۰ است:
# تهران
# اصفهان
# شیراز
# مشهد
# تبریز
# اردبیل
# --------------------------
