from elements.student import Student

student = Student(name="Andrei", address="Fabricii")
print(student)
student.add_course_grade("Chemistry", 8)
student.add_course_grade("Math", 9)
print(student.get_average())
print(student.print_grades())