# 6. یک دیکشنری شامل کلمات و تکرار آنها بسازید و برای شامل کلمات با تکرار بالای ۵ دیکشنری جدید ایجاد کنید.

text = "apple banana apple orange banana apple orange"
words = text.split()

word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

repeated_words = {word: count for word, count in word_count.items() if count > 1}
print(repeated_words)

# Output > {'apple': 3, 'banana': 2, 'orange': 2}
