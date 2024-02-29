students = []
num_students = int(input("Enter the number of students: "))


for i in range(num_students):
    firstname = input("Enter student First name: ")
    lastnames = input("Enter student Last name: ")
    id = input("Enter student ID: ")
    
    
    student_info = {"First Name": firstname, "Last Name": lastnames ,"ID": id}
    
    students.append(student_info)

for student in students:
    print("First Name:", student["First Name"])
    print("Last Name:", student["Last Name"])
    print("ID:", student["ID"])
    