import math
import numpy as np
import curses

class Student:
    def __init__(self, student_id, name, dob, major):
        self.student_id = student_id
        self.name = name
        self.dob = dob
        self.major = major
        self.marks = {}
        self.gpa = 0.0

    def input_marks(self, course_id, mark):
        self.marks[course_id] = math.floor(mark * 10) / 10  

    def calculate_gpa(self, courses):
        total_credits = 0
        weighted_sum = 0
        for course in courses:
            if course.course_id in self.marks:
                weighted_sum += self.marks[course.course_id] * course.credits
                total_credits += course.credits
        self.gpa = weighted_sum / total_credits if total_credits > 0 else 0
        return self.gpa

    def __str__(self):
        return f"ID: {self.student_id}, Name: {self.name}, DoB: {self.dob}, Major: {self.major}, GPA: {self.gpa:.2f}, Marks: {self.marks}"


class Course:
    def __init__(self, course_id, name, credits):
        self.course_id = course_id
        self.name = name
        self.credits = credits

    def __str__(self):
        return f"ID: {self.course_id}, Name: {self.name}, Credits: {self.credits}"


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
            credits = int(input("Enter course credits: "))
            self.courses.append(Course(course_id, name, credits))

    def input_marks(self):
        print("Available Courses:")
        for course in self.courses:
            print(course)

        course_id = input("Select a course ID to input marks: ")
        for student in self.students:
            mark = float(input(f"Enter marks for {student.name} (ID: {student.student_id}): "))
            student.input_marks(course_id, mark)

    def calculate_gpa_for_all(self):
        for student in self.students:
            student.calculate_gpa(self.courses)

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

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda s: s.gpa, reverse=True)

    def run(self):
        def main(stdscr):
            stdscr.clear()
            self.input_students()
            self.input_courses()
            self.input_marks()
            self.calculate_gpa_for_all()
            self.sort_students_by_gpa()

            stdscr.addstr("\nStudents sorted by GPA:\n")
            for student in self.students:
                stdscr.addstr(str(student) + "\n")
            stdscr.refresh()
            stdscr.getch()

        curses.wrapper(main)


if __name__ == "__main__":
    system = ManagementSystem()
    system.run()
