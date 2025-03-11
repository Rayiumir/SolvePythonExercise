# 8. فایل متنی شامل نام و سن ۵ نفر باشد و سپس آن را به صورت خط به خط بخوانید و چاپ کنید.

with open("text_file.txt", "r", encoding="utf-8") as file:
    for line in file:
        for word in line.split():
            print(word)
