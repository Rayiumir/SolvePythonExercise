# 1. یک دیکشنری از نام دانش آموزان و نمرات آنها ایجاد کنید، سپس دانش آموزی را که بالاترین نمره را دارد پیدا کنید

students = {
    "Ali": 85,
    "Sara": 92,
    "Reza": 78,
    "Mina": 88
}

top_student = max(students, key=students.get)
print(f"Top student: {top_student} with grade {students[top_student]}")

# Output > Top student: Sara with grade 92