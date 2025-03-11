# 7. یک ست شامل رشته ها ایجاد کنید و تمام کلماتی که با یک حرف خاص شروع می شوند را در یک ست جدید ذخیره کنید

words = {"apple", "banana", "cherry", "avocado", "blueberry", "apricot"}
target_letter = "a"

filtered_words = {word for word in words if word.startswith(target_letter)}
print(filtered_words)

# Output > {'avocado', 'apple', 'apricot'}