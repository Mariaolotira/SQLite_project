from main import Student

try:
    student_name = input("Enter Name \n")
    student_age = input("Enter Age \n")
    student_Id = input("Enter Id \n")
    student_stream = input("Enter Stream \n")
    student_gender = input("Enter Gender \n")

    Student.create(name=student_name, age=student_age, id=student_Id, stream=student_stream, gender=student_gender)
    print("Student created successfully")

except'':
    print("Failed to create student, try again")
