# 2. یک دیکشنری از محصولات و قیمت آنها ایجاد کنید، سپس میانگین قیمت را محاسبه کنید

products = {
    "Laptop": 1500,
    "Phone": 800,
    "Tablet": 600,
    "Monitor": 300
}

avg_price = sum(products.values()) / len(products)
print(f"Average price: {avg_price}")

# Output > Average price: 800.0