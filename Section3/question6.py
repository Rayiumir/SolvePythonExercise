# 6. گرفتن نام دانشجو از عنوان ورودی و اگر تعداد حروف نام او زوج باشد، پیام «تعداد حروف زوج است»نمایش دهد.

name = input("Enter student's name: ")
if len(name) % 2 == 0:
    print("The number of letters is even")

# Output
# Enter student's name: Raymond Baghumian Raymond Baghumian 
# The number of letters is even