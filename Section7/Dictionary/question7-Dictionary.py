# 7. یک دیکشنری ایجاد کنید که کلیدها بر اساس حروف الفبا مرتب شده اند

words = ["apple", "banana", "orange"]

sorted_letters_dict = {word: "".join(sorted(word)) for word in words}
print(sorted_letters_dict)

# Output > {'apple': 'aelpp', 'banana': 'aaabnn', 'orange': 'aegnor'}