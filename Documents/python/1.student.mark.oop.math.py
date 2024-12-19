def input_number_of_students():
    num_students = int(input("Enter the number of students: "))
    students = []
    for _ in range(num_students):
        student_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student Date of Birth (YYYY-MM-DD): ")
        major = input("Enter student major: ")
        students.append({
            'id': student_id,
            'name': name,
            'dob': dob,
            'major': major,
            'marks': {}
        })
    return students


def input_number_of_courses():
    num_courses = int(input("Enter the number of courses: "))
    courses = []
    for _ in range(num_courses):
        course_id = input("Enter course ID: ")
        name = input("Enter course name: ")
        courses.append({
            'id': course_id,
            'name': name
        })
    return courses


def input_marks(students, courses):
    print("Available Courses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")
    
    course_id = input("Select a course ID to input marks: ")
    for student in students:
        mark = float(input(f"Enter marks for {student['name']} (ID: {student['id']}): "))
        student['marks'][course_id] = mark


def list_courses(courses):
    print("Courses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")


def list_students(students):
    print("Students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}, Major: {student['major']}, Marks: {student['marks']}")


def show_student_marks(students):
    course_id = input("Enter course ID to show marks: ")
    print(f"Marks for course ID {course_id}:")
    for student in students:
        mark = student['marks'].get(course_id, "No marks entered")
        print(f"{student['name']} (ID: {student['id']}): {mark}")


def main():
    students = input_number_of_students()
    courses = input_number_of_courses()
    input_marks(students, courses)
    
    list_students(students)
    show_student_marks(students)


if __name__ == "__main__":
    main()