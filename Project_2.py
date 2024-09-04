student_grades = {}

def add_student(name, grade):
    student_grades[name] = grade
    print(f"Added {name} with a grade of {grade}.")

def update_student(name, grade):
    if name in student_grades:
        student_grades[name] = grade
        print(f"Updated {name}'s grade to {grade}.")
    else:
        print(f"{name} is not found!")

def delete_student(name):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfully deleted!")
    else:
        print(f"{name} is not found!")  # Corrected f-string

def display_all_students():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name}: {grade}")
    else:
        print("No students found.")

def main():
    while True:
        print("\nTaqwa Students Grades Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. View Students")
        print("5. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            name = input("Enter student's name: ")
            try:
                grade = int(input("Enter student's grade: "))
            except ValueError:
                print("Invalid grade! Please enter a number.")
                continue
            add_student(name, grade)

        elif choice == 2:
            name = input("Enter student's name: ")
            try:
                grade = int(input("Enter new grade: "))
            except ValueError:
                print("Invalid grade! Please enter a number.")
                continue
            update_student(name, grade)

        elif choice == 3:
            name = input("Enter student's name: ")
            delete_student(name)

        elif choice == 4:
            display_all_students()

        elif choice == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid choice. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()
