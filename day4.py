students = []
def add_student():
    name = input("Enter student name: ")

    try:
        mark = int(input("Enter student mark: "))
    except ValueError:
        print("Please enter a valid number.")
        return

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

def show_average():
    if len(students) == 0:
        print("No students found.")
        return
    total = 0
    for student in students:
        total = total + student["mark"]
    average = total / len(students)
    print("Average mark:", average)
while True:
    print("\n=== Student Management System ===")
    print("1. Add Student")
    print("2. Show Students")
    print("3. Show Average")
    print("4. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        show_average()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")