
class StudentManagement:

    def __init__(self):
        self.students = []

    def add_student(self, name, marks):
        if not name:
            raise ValueError("Student name is required")

        if marks < 0 or marks > 100:
            raise ValueError("Marks must be between 0 and 100")

        student = {
            "name": name,
            "marks": marks
        }

        self.students.append(student)
        return student

    def get_students(self):
        return self.students

    def calculate_grade(self, marks):
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 50:
            return "C"
        else:
            return "Fail"
