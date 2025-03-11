# 1. یک فایل متنی با نام ها و شهرها ایجاد کنید، سپس آنها را به صورت خط به خط بخوانید و برای هر فرد یه جمله چاپ کنید.

# نوشتن نام و شهر و سن هادر یک فایل
data = ["Ali - Tehran - 30\n", "Sara - Mashhad - 20\n", "Reza - Shiraz -25\n"]

with open("people.txt", "w", encoding="utf-8") as file:
    file.writelines(data)

# خواندن و چاپ به صورت خط به خط
with open("people.txt", "r", encoding="utf-8") as file:
    for line in file:
        parts = line.strip().split(" - ")
        
        if len(parts) == 2:  # فقط نام و شهر وجود دارد
            name, city = parts
            print(f"{name} در شهر {city} زندگی می‌کند.")
        elif len(parts) == 3:  # نام, شهر, , سن وجود دارد
            name, city, age = parts
            print(f"{name} در شهر {city} زندگی می‌کند و {age} سال دارد.")
        else:
            print("فرمت خط نامعتبر است:", line)
