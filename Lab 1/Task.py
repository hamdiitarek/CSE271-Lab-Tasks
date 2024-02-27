students = []
num_students = int(input("Enter the number of students: "))

for i in range(num_students):
    name = input("Enter student name: ")
    id = input("Enter student ID: ")
    
    student_info = {"Name": name, "ID": id}
    
    students.append(student_info)

for student in students:
    print("Name:", student["Name"])
    print("ID:", student["ID"])