from typing import List


class Person:
    def __init__(self, name: str, address: str):
        self.__name = name
        self.__address = address

    def get_name(self) -> str:
        return self.__name

    @property
    def name(self) -> str:
        return self.__name

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    def __str__(self) -> str:
        return "Name: " + self.__name + "\tAddress: " + self.address


class Teacher(Person):
    def __init__(self, name: str, address: str):
        super().__init__(name, address)
        self.__courses: List[str] = []

    def add_course(self, course: str) -> bool:
        if len(self.__courses) < 3:
            self.__courses.append(course)
            return True
        return False


class Student(Person):
    def __init__(self, name: str, address: str):
        super().__init__(name, address)
        self.__numCourses: int = 0
        self.__courses: List[str] = []
        self.__grades: List[int] = []

    def __str__(self) -> str:
        return "Student: " + self.name + "\tAddress = " + self.address

    def add_course_grade(self, course: str, grade: int):
        self.__courses.append(course)
        self.__grades.append(grade)

    def get_average(self) -> float:
        s = 0
        for i in self.__grades:
            s = s + i
        return s/(len(self.__grades))

    def print_grades(self):
        print(self.__grades)


student = Student(name="Andrei", address="Fabricii")
print(student)
student.add_course_grade("Chemistry", 8)
student.add_course_grade("Math", 9)
print(student.get_average())
print(student.print_grades())