from typing import List

from flask import Flask, url_for

from elements.student import Student

app = Flask(__name__)
elements_list: List[Student] = []


@app.route('/')
def index():
    return 'Vreau sa vad ca merge'


@app.route('/add/<username>/<address>' )
def add(username, address):
    a = Student(name=username, address=address)
    global elements_list
    elements_list.append(a)
    return 'I did it'


@app.route('/list')
def list():
    global elements_list
    return_value: str = ''
    for each in elements_list:
        return_value = return_value + ' ' + str(each)
    return return_value




app.run()


# from elements.student import Student
#
# student = Student(name="Andrei", address="Fabricii")
# print(student)
# student.add_course_grade("Chemistry", 8)
# student.add_course_grade("Math", 9)
# print(student.get_average())
# print(student.print_grades())
