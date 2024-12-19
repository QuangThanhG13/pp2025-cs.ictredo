class Student:
    def __init__(self, student_id, name, dob, major):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.major = major
        self.marks = {}

    def input_marks(self, course_id, mark):
        self.marks[course_id] = mark

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}, Major: {self.major}, Marks: {self.marks}"


class Course:
    def __init__(self, course_id, name):
        self.course_id = course_id
        self.name = name

    def __str__(self):
        return f"ID: {self.course_id}, Name: {self.name}"


class ManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        num_students = int(input("Enter the number of students: "))
        for _ in range(num_students):
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student Date of Birth (YYYY-MM-DD): ")
            major = input("Enter student major: ")
            self.students.append(Student(student_id, name, dob, major))

    def input_courses(self):
        num_courses = int(input("Enter the number of courses: "))
        for _ in range(num_courses):
            course_id = input("Enter course ID: ")
            name = input("Enter course name: ")
            self.courses.append(Course(course_id, name))

    def input_marks(self):
        print("Available Courses:")
        for course in self.courses:
            print(course)

        course_id = input("Select a course ID to input marks: ")
        for student in self.students:
            mark = float(input(f"Enter marks for {student.name} (ID: {student.student_id}): "))
            student.input_marks(course_id, mark)

    def list_courses(self):
        print("Courses:")
        for course in self.courses:
            print(course)

    def list_students(self):
        print("Students:")
        for student in self.students:
            print(student)

    def show_student_marks(self):
        course_id = input("Enter course ID to show marks: ")
        print(f"Marks for course ID {course_id}:")
        for student in self.students:
            mark = student.marks.get(course_id, "No marks entered")
            print(f"{student.name} (ID: {student.student_id}): {mark}")

    def run(self):
        self.input_students()
        self.input_courses()
        self.input_marks()
        self.list_students()
        self.show_student_marks()


if __name__ == "__main__":
    system = ManagementSystem()
    system.run()
