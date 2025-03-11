import csv
import os

# نام فایل CSV
filename = "students.csv"

def load_students():
    """
    خواندن داده‌های دانش‌آموزان از فایل CSV
    """
    students = []
    if os.path.exists(filename):
        with open(filename, mode='r', encoding='utf-8', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    return students

def save_students(students):
    """
    ذخیره لیست دانش‌آموزان در فایل CSV
    """
    fieldnames = ['ID', 'Name', 'Age', 'Grade']
    with open(filename, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

def display_students(students):
    """
    نمایش لیست دانش‌آموزان
    """
    if not students:
        print("هیچ دانش‌آموزی موجود نیست.")
        return
    print("\nلیست دانش‌آموزان:")
    for student in students:
        print(f"ID: {student['ID']}, نام: {student['Name']}, سن: {student['Age']}, پایه: {student['Grade']}")

def add_student(students):
    """
    اضافه کردن دانش‌آموز جدید
    """
    # تعیین ID جدید (اگر لیست خالی باشد، از 1 شروع می‌شود)
    if students:
        new_id = max(int(s['ID']) for s in students) + 1
    else:
        new_id = 1
    name = input("نام دانش‌آموز: ")
    age = input("سن دانش‌آموز: ")
    grade = input("پایه/رده دانش‌آموز: ")
    students.append({'ID': str(new_id), 'Name': name, 'Age': age, 'Grade': grade})
    print("دانش‌آموز اضافه شد.")

def delete_student(students):
    """
    حذف دانش‌آموز بر اساس ID وارد شده
    """
    student_id = input("آیدی دانش‌آموز برای حذف: ")
    for student in students:
        if student['ID'] == student_id:
            students.remove(student)
            print("دانش‌آموز حذف شد.")
            return
    print("دانش‌آموز با این آیدی یافت نشد.")

def update_student(students):
    """
    آپدیت اطلاعات دانش‌آموز بر اساس ID وارد شده
    """
    student_id = input("آیدی دانش‌آموز برای آپدیت: ")
    for student in students:
        if student['ID'] == student_id:
            print("لطفاً اطلاعات جدید را وارد کنید (برای حفظ مقدار فعلی، ورودی را خالی بگذارید):")
            new_name = input(f"نام (فعلی: {student['Name']}): ")
            new_age = input(f"سن (فعلی: {student['Age']}): ")
            new_grade = input(f"پایه/رده (فعلی: {student['Grade']}): ")
            if new_name.strip():
                student['Name'] = new_name
            if new_age.strip():
                student['Age'] = new_age
            if new_grade.strip():
                student['Grade'] = new_grade
            print("اطلاعات دانش‌آموز به‌روز شد.")
            return
    print("دانش‌آموز با این آیدی یافت نشد.")

def main():
    students = load_students()
    while True:
        print("\n--- مدیریت دانش‌آموزان ---")
        print("1. نمایش لیست دانش‌آموزان")
        print("2. اضافه کردن دانش‌آموز")
        print("3. حذف دانش‌آموز")
        print("4. آپدیت دانش‌آموز")
        print("5. خروج")
        choice = input("انتخاب شما: ")
        if choice == "1":
            display_students(students)
        elif choice == "2":
            add_student(students)
            save_students(students)
        elif choice == "3":
            delete_student(students)
            save_students(students)
        elif choice == "4":
            update_student(students)
            save_students(students)
        elif choice == "5":
            print("خروج از برنامه.")
            break
        else:
            print("انتخاب نامعتبر. دوباره امتحان کنید.")

if __name__ == "__main__":
    main()

# نمونه
# --- مدیریت دانش‌آموزان ---
# 1. نمایش لیست دانش‌آموزان
# 2. اضافه کردن دانش‌آموز
# 3. حذف دانش‌آموز
# 4. آپدیت دانش‌آموز
# 5. خروج
# انتخاب شما: 2
# نام دانش‌آموز: علی
# سن دانش‌آموز: 15
# پایه/رده دانش‌آموز: 10
# دانش‌آموز اضافه شد.
#
# --- مدیریت دانش‌آموزان ---
# 1. نمایش لیست دانش‌آموزان
# 2. اضافه کردن دانش‌آموز
# 3. حذف دانش‌آموز
# 4. آپدیت دانش‌آموز
# 5. خروج
# انتخاب شما: 1
#
# لیست دانش‌آموزان:
# ID: 1, نام: علی, سن: 15, پایه: 10
#
# --- مدیریت دانش‌آموزان ---
# 1. نمایش لیست دانش‌آموزان
# 2. اضافه کردن دانش‌آموز
# 3. حذف دانش‌آموز
# 4. آپدیت دانش‌آموز
# 5. خروج
# انتخاب شما: 5
# خروج از برنامه.
