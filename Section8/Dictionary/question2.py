# ایجاد دی‌کشنری از محصولات و قیمت‌های آنها
products_prices = {
    "Laptop": 1000,
    "Phone": 800,
    "Tablet": 600,
    "Headphones": 200,
    "Smartwatch": 250
}

# محاسبه میانگین قیمت‌ها
average_price = sum(products_prices.values()) / len(products_prices)

# یافتن محصولاتی که قیمت آنها بیشتر از میانگین است
expensive_products = {product: price for product, price in products_prices.items() if price > average_price}

# نمایش نتایج
print("میانگین قیمت‌ها:", average_price)
print("محصولاتی که قیمت آنها بیشتر از میانگین است:", expensive_products)

# نمونه خروجی:
# میانگین قیمت‌ها: 570.0
# محصولاتی که قیمت آنها بیشتر از میانگین است: {'Laptop': 1000, 'Phone': 800}
