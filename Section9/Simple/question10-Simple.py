# 10. یک فایل متنی بسازید و رشته خاص درآن جسنجو کنید.

search_word = "پایتون"

with open("text_file.txt", "r", encoding="utf-8") as file:
    content = file.read()
    if search_word in content:
        print(f'کلمه "{search_word}" پیدا شد!')
    else:
        print(f'کلمه "{search_word}" پیدا نشد!')
