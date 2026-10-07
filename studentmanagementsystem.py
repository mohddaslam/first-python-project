students = []


def add_student():
    name = input("Enter student name: ")
    mark = int(input("Enter student mark: "))

    student = {
        "name": name,
        "mark": mark
    }

    students.append(student)

    print("Student added successfully!")


def show_students():
    if len(students) == 0:
        print("No students found.")
        return

    print("\n--- Student List ---")

    for student in students:
        print("Name:", student["name"])
        print("Mark:", student["mark"])
        print("----------------")


while True:
    print("\n=== Student Management System ===")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        show_students()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")