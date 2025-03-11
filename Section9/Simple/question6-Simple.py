# 6. یک فایل متنی ایجاد کنید و سپس آن را به صورت خط به خط بخوانید و چاپ کنید.

user_text = input("متن خود را وارد کنید: ")

with open("user_input.txt", "w", encoding="utf-8") as file:
    file.write(user_text)

