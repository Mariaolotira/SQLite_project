from main import Student

our_student = Student.select()
for student in our_student:
    print(student.name, student.age, student.id, student.stream, student.gender)
