# 3. یک دیکشنری شامل رشته ها و تعداد تکرار آنها از یک متن بسازید و پرکاربردترین کلمه را پیدا کنید.

text = "apple banana apple orange banana apple"
words = text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

most_used_word = max(word_count, key=word_count.get)
print(f"Most used word: {most_used_word} ({word_count[most_used_word]} times)")

# Output > Most used word: apple (3 times)


