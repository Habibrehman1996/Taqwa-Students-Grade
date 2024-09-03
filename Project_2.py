student_grades={ }

#add a new student
def add_student(name,grade):
    student_grades[name]=grade
    print(f"Added {name} with a {grade}")

def update_student(name,grade):
    if name in student_grades:
        student_grades[name]=grade
        print(f"{name} with marks are updated {grade}" )
    else:
        print(f"{name} is not found!")
def delete_student(name, grade):
    if name in student_grades:
        del student_grades[name]
        print(f"{name} has been successfuly deleted!")
    else:
         print(f"{name} is not found!")

def display_all_students():
    if student_grades:
        for name, grade in student_grades.items():
            print(f"{name} : {grade}")

    else:
        print("No student found/added")

def main():
    while True:
        print('\n Taqwa Students Grades Management System')
        print("1. Add Student")
        print("2. update Student")
        print("3. delete Student")
        print("4. view Student")
        print("5. exit Student")

        


