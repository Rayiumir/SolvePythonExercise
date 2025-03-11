# تعریف دی‌کشنری با محصولات و تعداد موجودی
inventory = {
    "Laptop": 10,
    "Phone": 0,
    "Tablet": 5,
    "Headphones": 0,
    "Charger": 3
}

# پیدا کردن محصولاتی که موجودی آن‌ها صفر است
out_of_stock = {product: quantity for product, quantity in inventory.items() if quantity == 0}

# نمایش محصولات با موجودی صفر
print("محصولات با موجودی صفر:", out_of_stock)

# نمونه خروجی:
# محصولات با موجودی صفر: {'Phone': 0, 'Headphones': 0}
