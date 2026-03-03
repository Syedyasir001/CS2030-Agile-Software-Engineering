class CourseSystem:
    def __init__(self):
        self.courses = {}

    def add_course(self, course):
        if course not in self.courses:
            self.courses[course] = []
            print("Course added.")
        else:
            print("Course already exists.")

    def register_student(self, student, course):
        if course in self.courses:
            if student not in self.courses[course]:
                self.courses[course].append(student)
                print("Student registered.")
            else:
                print("Student already enrolled.")
        else:
            print("Course not found.")

    def drop_course(self, student, course):
        if course in self.courses and student in self.courses[course]:
            self.courses[course].remove(student)
            print("Student dropped from course.")
        else:
            print("Enrollment not found.")

    def view_students(self, course):
        if course in self.courses:
            print("Enrolled Students:", self.courses[course])
        else:
            print("Course not found.")


# Simple Testing
system = CourseSystem()

system.add_course("Math")
system.register_student("Ali", "Math")
system.view_students("Math")
system.drop_course("Ali", "Math")
system.view_students("Math")
