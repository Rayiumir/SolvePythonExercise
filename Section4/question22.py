# ترسیم مربع
def draw_square(size):
    print("مربع:")
    for i in range(size):
        print("* " * size)


# ترسیم مستطیل
def draw_rectangle(width, height):
    print("مستطیل:")
    for i in range(height):
        print("* " * width)


# ترسیم مثلث متساوی‌الاضلاع توپر
def draw_equilateral_triangle_filled(height):
    print("مثلث متساوی الساقین (توپر):")
    for i in range(1, height + 1):
        print(" " * (height - i) + "* " * i)


# ترسیم مثلث متساوی‌الاضلاع توخالی
def draw_equilateral_triangle_empty(height):
    print("مثلث متساوی الساقین (توخالی):")
    for i in range(1, height + 1):
        if i == 1:
            print(" " * (height - i) + "*")
        elif i == height:
            print("* " * i)
        else:
            print(" " * (height - i) + "* " + " " * (2 * i - 3) + "*")


# ترسیم متوازی‌الاضلاع
def draw_parallelogram(width, height):
    print("متوازی‌الاضلاع:")
    for i in range(height):
        print(" " * (height - i - 1) + "* " * width)


# انتخاب نوع شکل و اندازه‌ها
shape = (
    input(
        "کدام شکل را می‌خواهید رسم کنید؟ (مربع، مستطیل، مثلث توپر، مثلث توخالی، متوازی‌الاضلاع): "
    )
    .strip()
    .lower()
)

if shape == "مربع":
    size = int(input("اندازه مربع را وارد کنید: "))
    draw_square(size)

elif shape == "مستطیل":
    width = int(input("عرض مستطیل را وارد کنید: "))
    height = int(input("ارتفاع مستطیل را وارد کنید: "))
    draw_rectangle(width, height)

elif shape == "مثلث توپر":
    height = int(input("ارتفاع مثلث توپر را وارد کنید: "))
    draw_equilateral_triangle_filled(height)

elif shape == "مثلث توخالی":
    height = int(input("ارتفاع مثلث توخالی را وارد کنید: "))
    draw_equilateral_triangle_empty(height)

elif shape == "متوازی‌الاضلاع":
    width = int(input("عرض متوازی‌الاضلاع را وارد کنید: "))
    height = int(input("ارتفاع متوازی‌الاضلاع را وارد کنید: "))
    draw_parallelogram(width, height)

else:
    print("شکل وارد شده نامعتبر است.")

# --------------------------
# نمونه ورودی:
# کدام شکل را می‌خواهید رسم کنید؟ مثلث توپر
# ارتفاع مثلث توپر را وارد کنید: 5
# --------------------------

# نمونه خروجی:
# مثلث متساوی الساقین (توپر):
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
# --------------------------
