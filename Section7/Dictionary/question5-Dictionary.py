# 5. یک دیکشنری از جزئیات محصول ایجاد کنید و گران ترین محصول را پیدا کنید

products = {
    "Laptop": {"price": 1500, "stock": 5},
    "Phone": {"price": 800, "stock": 10},
    "Tablet": {"price": 600, "stock": 7}
}

most_expensive = max(products, key=lambda x: products[x]["price"])
print(f"Most expensive product: {most_expensive} with price {products[most_expensive]['price']}")

# Output > Most expensive product: Laptop with price 1500