# 4. دریافت یک رشته و یک عدد از ورودی و نمایش پیغام رشته کوتاه است

text = input("Enter a string: ")
number = int(input("Enter a number: "))

if len(text) < number:
    print("The string is short")

# Output
# Enter a string: Hi 
# Enter a number: 3 
# The string is short