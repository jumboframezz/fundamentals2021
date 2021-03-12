n = int(input())
students = {}
for _ in range(n):
    student, grade = input().split()
    grade = float(grade)
    if student not in students:
        students[student] = []
    students[student].append(grade)

for name, grades in students.items():
    grades_str = ' '.join(map(lambda g: f'{g:.2f}', grades))
    average_grade = sum(grades) / len(grades)
    print(f'{name} -> {grades_str} (avg: {average_grade:.2f})')
