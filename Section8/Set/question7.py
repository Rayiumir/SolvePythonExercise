# ایجاد یک set از مقادیر رشته‌ای
words_set = {"apple", "banana", "cat", "dog", "elephant", "kiwi"}

# فیلتر کردن رشته‌هایی که طول آنها بیشتر از ۴ حرف است
filtered_words_set = {word for word in words_set if len(word) > 4}

# نمایش نتیجه
print("Set اولیه:", words_set)
print("Set بعد از فیلتر:", filtered_words_set)

# نمونه خروجی:
# Set اولیه: {'banana', 'apple', 'cat', 'elephant', 'kiwi', 'dog'}
# Set بعد از فیلتر: {'banana', 'apple', 'elephant'}
