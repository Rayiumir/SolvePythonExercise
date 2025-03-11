# تعریف دی‌کشنری شامل نام کتاب‌ها و قیمت آنها
book_prices = {
    "book1": 45000,
    "book2": 60000,
    "book3": 70000,
    "book4": 30000,
    "book5": 55000
}

# پیدا کردن کتاب‌هایی با قیمت بیشتر از ۵۰ هزار تومان
expensive_books = {book: price for book, price in book_prices.items() if price > 50000}

# نمایش کتاب‌های گران‌تر از ۵۰ هزار تومان
print("کتاب‌های با قیمت بیشتر از ۵۰ هزار تومان:")
for book, price in expensive_books.items():
    print(f"{book}: {price} تومان")

# نمونه خروجی:
# کتاب‌های با قیمت بیشتر از ۵۰ هزار تومان:
# book2: 60000 تومان
# book3: 70000 تومان
# book5: 55000 تومان
