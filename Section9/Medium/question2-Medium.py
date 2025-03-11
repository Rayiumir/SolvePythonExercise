# 2. یک فایل متنی با 5 جمله ایجاد کنید، یک کلمه خاص را جستجو کنید و تعداد دفعات آن را بشمارید.

search_word = "پایتون"

with open("text_file.txt", "r", encoding="utf-8") as file:
    content = file.read()

count = content.count(search_word)
print(f'کلمه "{search_word}" {count} بار در فایل تکرار شده است.')