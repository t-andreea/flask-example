from typing import List

from flask import Flask

from elements.person import Person

from elements.student import Student

app = Flask(__name__)
elements_list: List[Person] = []
student_list: List[Student] = []
grade_list: List[Student] = []


@app.route('/')
def index():
    return 'Congratz, it reaaaally works'


@app.route('/add/person/<username>/<address>' )
def add_person(username, address):
    a = Person(name=username, address=address)
    global elements_list
    elements_list.append(a)
    return 'I did it'


@app.route('/add/student/<course>/<grade>')
def add_student(course, grade):
    global student_list, grade_list
    student_list.append(course)
    grade_list.append(grade)
    return 'added'


@app.route('/list/person')
def list_people():
    global elements_list
    return_value: str = ''
    for each in elements_list:
        return_value = return_value + '\n' + str(each)
    return return_value


@app.route('/list/student')
def list_student():
    global student_list, grade_list
    return_student: str = ''
    for i in student_list:
        return_student = return_student + '\n' + str(i)
    return return_student


# @app.route('/list/student')
#     global student_list
#     return_value: str = ''
#     for each in st


app.run(host = '0.0.0.0')


# from elements.student import Student
#
# student = Student(name="Andrei", address="Fabricii")
# print(student)
# student.add_course_grade("Chemistry", 8)
# student.add_course_grade("Math", 9)
# print(student.get_average())
# print(student.print_grades())
