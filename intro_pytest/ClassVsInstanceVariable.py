
class Student:
    TOTAL_STUDENTS = 0

    def __init__(self, name: str):
        self.name = name

    @classmethod
    def get_report(cls):
        print(f"CLASS REPORT: {cls.TOTAL_STUDENTS}")

    def register(self):
        print(f"Register {self.name}")
        Student.TOTAL_STUDENTS += 1
        print(f"Total students: {Student.TOTAL_STUDENTS}")

    def leave(self):
        print(f"Leave {self.name}")
        Student.TOTAL_STUDENTS -= 1
        print(f"Total students: {Student.TOTAL_STUDENTS}")

