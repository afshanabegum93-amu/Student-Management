students = {
    "S101": ("Alice", 20, "Computer Science", 3.8),
    "S102": ("Bob", 21, "Mathematics", 3.6)
    }  # Dictionary to store employee data
def add_students():
    try:
        stu_id = input("Enter Student ID: ").strip()
        if stu_id in students:
            print("Error: Students ID already exists!")
            return
        
        name = input("Enter Name: ").strip()
        age = int(input("Enter Age: ").strip())  # Convert to integer
        course = input("Enter course: ").strip()
        GPA = float(input("Enter GPA: ").strip())  # Convert to float

        students[stu_id] = (name, age, course, GPA)
        print("student added successfully!")
    
    except ValueError:
        print("Error: Invalid input! Age must be an integer and GPA must be a number.")
def view_students():
    if not students:
        print("No students found!")
        return
    
    print("\nStudent List:")
    print("ID\tName\tAge\tCourse\tGPA")
    print("-" * 50)
    
    for stu_id, details in students.items():
        print(f"{stu_id}\t{details[0]}\t{details[1]}\t{details[2]}\t{details[3]}")
def search_student():
    stu_id = input("Enter Student ID to search: ").strip()
    if stu_id in students:
        details = students[stu_id]
        print(f"\nstudent Found:\nID: {stu_id}\nName: {details[0]}\nAge: {details[1]}\ncourse: {details[2]}\nGPA: {details[3]}")
    else:
        print("Error: Student not found!")
def update_student():
    stu_id = input("Enter Student ID to update: ").strip()
    
    if stu_id in students:
        name, age, course, GPA = students[stu_id]
        
        print("Leave blank to keep current value.")
        new_name = input(f"Enter new Name ({name}): ").strip() or name
        new_age = input(f"Enter new Age ({age}): ").strip()
        new_course = input(f"Enter new Course ({course}): ").strip() or course
        new_GPA = input(f"Enter new GPA ({gpa}): ").strip()
        
        # Convert types if input is not empty
        age = int(new_age) if new_age else age
        GPA = float(new_GPA) if new_GPA else GPA

        students[stu_id] = (new_name, age, new_course, GPA)
        print("Student details updated successfully!")
    
    else:
        print("Error: Student not found!")
def delete_student():
    stu_id = input("Enter student ID to delete: ").strip()
    
    if stu_id in students:
        del students[stu_id]
        print("Student deleted successfully!")
    else:
        print("Error: Student not found!")
def students_by_course():
    courses = set(stu[2] for stu in students.values())  # Extracting department names
    
    if not courses:
        print("No students found!")
        return

    for dept in courses:
        print(f"\nCourse: {dept}")
        print("ID\tName\tAge\tGPA")
        print("-" * 40)
        
        for stu_id, details in students.items():
            if details[2] == dept:
                print(f"{stu_id}\t{details[0]}\t{details[1]}\t{details[3]}")
def average_gpa():
    if not students:
        print("No employees found!")
        return

    total_gpa = sum(stu[3] for stu in students.values())  # Summing salaries
    avg_gpa = total_gpa / len(students)
    
    print(f"\nAverage Gpa: {avg_gpa:.2f}")
while True:
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Student by Course")
    print("7. Average GPA")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ").strip()

    if choice == "1":
        add_students()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        students_by_course()
    elif choice == "7":
        average_gpa()
    elif choice == "8":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 8.")
        
        
