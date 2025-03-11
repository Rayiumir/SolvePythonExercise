# 2. یک فایل متنی ایجاد کنید که شامل اسامی شهرها باشد و سپس اسامی شهرهایی که در آن حرف A وجود دارد را در فایل جداگانه ذخیره کند.

# لیستی از اسامی شهرها
cities = [
    "Tehran",
    "Mashhad",
    "Isfahan",
    "Shiraz",
    "Tabriz",
    "Kerman",
    "Yazd",
    "Ahvaz",
    "Qom",
]

# ایجاد و نوشتن اسامی شهرها در فایل
with open("cities.txt", "w") as file:
    for city in cities:
        file.write(city + "\n")

# خواندن اسامی شهرها از فایل
with open("cities.txt", "r") as file:
    city_list = file.readlines()

# فیلتر کردن شهرهایی که در نامشان حرف "A" وجود دارد
cities_with_A = [city.strip() for city in city_list if "A" in city.upper()]

# ذخیره اسامی شهرهایی که حرف "A" دارند در فایل جداگانه
with open("cities_with_A.txt", "w") as file:
    for city in cities_with_A:
        file.write(city + "\n")

# چاپ اسامی شهرهایی که حرف "A" دارند
print("شهرهایی که حرف A در نامشان وجود دارد:")
for city in cities_with_A:
    print(city)
