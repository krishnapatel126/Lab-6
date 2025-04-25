n = int(input("Enter number of students: "))
students = []

for _ in range(n):
    roll = int(input("Enter roll number: "))
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    students.append((roll, name, age))

roll_nos = [student[0] for student in students]
names = [student[1] for student in students]
ages = [student[2] for student in students]

print("Roll Numbers:", roll_nos)
print("Names:", names)
print("Ages:", ages)
