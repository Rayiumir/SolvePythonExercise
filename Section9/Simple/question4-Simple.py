# 4. یک فایل متنی حاوی اطلاعات محصول ایجاد کنید و سپس آن را به صورت خط به خط بخوانید و چاپ کنید.

products = ["Laptop - 30000\n", "Phone - 20000\n", "Tablet - 15000\n"]

with open("products.txt", "w", encoding="utf-8") as file:
    file.writelines(products)

with open("products.txt", "r", encoding="utf-8") as file:
    print(file.read())
