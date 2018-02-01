from typing import List

from elements.person import Person


class Teacher(Person):
    def __init__(self, name: str, address: str):
        super().__init__(name, address)
        self.__courses: List[str] = []

    def add_course(self, course: str) -> bool:
        if len(self.__courses) < 3:
            self.__courses.append(course)
            return True
        return False