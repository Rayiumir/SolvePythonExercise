# ایجاد دی‌کشنری شامل کلمات و تعداد تکرار آنها
word_counts = {
    "apple": 3,
    "banana": 6,
    "cherry": 2,
    "date": 7,
    "elderberry": 1,
    "fig": 8,
    "grape": 5
}

# فیلتر کردن کلمات با تعداد تکرار بیش از ۵
filtered_words = {word: count for word, count in word_counts.items() if count > 5}

# نمایش کلمات با تعداد تکرار بیشتر از ۵
print("کلمات با تعداد تکرار بیشتر از ۵:", filtered_words)

# نمونه خروجی:
# کلمات با تعداد تکرار بیشتر از ۵: {'banana': 6, 'date': 7, 'fig': 8}
