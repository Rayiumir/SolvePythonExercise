# 8. بالاترین میانگین نمرات دانشجویان

def above_average(students):
    grades = [student[1] for student in students]
    avg = sum(grades) / len(grades)
    above_avg = [student[0] for student in students if student[1] > avg]
    return above_avg

# نمونه استفاده:
students = [("Alice", 85), ("Bob", 70), ("Charlie", 92)]
print("Students:", above_average(students))

# Output > Students: ['Alice', 'Charlie']