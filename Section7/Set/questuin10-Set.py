# 10. یک ست از رشته ها را ایجاد کنید و رشته ای را که بیشترین کاراکتر را دارد را پیدا کند

words = {"elephant", "dog", "hippopotamus", "cat", "giraffe"}

longest_word = max(words, key=len)
print(longest_word)

# Output > hippopotamus