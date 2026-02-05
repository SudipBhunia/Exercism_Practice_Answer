class School:
    def __init__(self):
        self.students = {}
        self.add_results = []

    def add_student(self, name, grade):
    # Check if student already exists in any grade
        for students_in_grade in self.students.values():
            if name in students_in_grade:
                self.add_results.append(False)
                return False

        # Add student
        if grade not in self.students:
            self.students[grade] = []

        self.students[grade].append(name)
        self.add_results.append(True)
        return True

    def roster(self):
        result = []
        for grade in sorted(self.students.keys()):
            result.extend(sorted(self.students[grade]))
        return result

    def grade(self, grade_number):
        return sorted(self.students.get(grade_number, []))

    def added(self):
        return self.add_results