from typing import List

from elements.person import Person

class Student(Person):
    def __init__(self, name: str, address: str):
        super().__init__(name, address)
        self.__courses: List[str] = []
        self.__grades: List[int] = []

    def __str__(self) -> str:
        return "Student{name:  " + self.name + ", address: " + self.address + '}'

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