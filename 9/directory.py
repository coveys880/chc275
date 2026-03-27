f getStudent(directory, student): 

    """Return the record dict for a student. 

 

    Args: 

        directory (dict): Student directory. 

        student (str): Student name. 

 

    Returns: 

        dict: The student record, or None if not found. 

    """ 

    return directory.get(student) 

 

def getStudentGrades(directory, student): 

    """Return the student's gradebook dict (course -> grade).""" 

    stu = getStudent(directory, student) 

    if not stu: 

        return None 

    return stu.get("grades", {}) 

 

def getStudentGradeLevel(directory, student): 

    """Return the student's grade level (int).""" 

    stu = getStudent(directory, student) 

    if not stu: 

        return None 

    return stu.get("grade_level") 

 

def getStudentEmail(directory, student): 

    """Return the student's email address.""" 

    stu = getStudent(directory, student) 

    if not stu: 

        return None 

    return stu.get("email") 

 

def getStudentsByGradeLevel(directory, gradelevel): 

    """Print all students in a given grade level.""" 

    matches = [name for name, record in directory.items() if record.get("grade_level") == gradelevel] 

    if not matches: 

        print(f"No students found in grade {gradelevel}.") 

        return 

    print(f"Students in grade {gradelevel}:") 

    for name in sorted(matches): 

        print(f" - {name}") 

 

def addStudent(directory): 

    """Add a new student to the directory via user input.""" 

    name = input("Enter student name: ").strip() 

    if not name: 

        print("Student name cannot be empty.") 

        return 

    if name in directory: 

        print(f"Student '{name}' already exists.") 

        return 

 

    try: 

        grade_level = int(input("Enter grade level (e.g., 9): ").strip()) 

    except ValueError: 

        print("Invalid grade level. Must be an integer.") 

        return 

 

    email = input("Enter email: ").strip() 

    if not email: 

        print("Email cannot be empty.") 

        return 

 

    grades: dict = {} 

    while True: 

        course = input("Enter course name (or blank to finish): ").strip() 

        if not course: 

            break 

        try: 

            score = float(input(f"Enter grade for {course}: ").strip()) 

        except ValueError: 

            print("Invalid grade. Must be a number.") 

            continue 

        grades[course] = score 

 

    directory[name] = {"grade_level": grade_level, "email": email, "grades": grades} 

    print(f"Added {name} to the directory.") 

 

def removeStudent(directory, student): 

    """Remove a student from the directory.""" 

    if student not in directory: 

        print(f"Student '{student}' not found.") 

        return 

    del directory[student] 

    print(f"Removed student '{student}'.") 

 

def updateGrade(directory, student): 

    """Update or add a grade for a student.""" 

    grades = getStudentGrades(directory, student) 

    if grades is None: 

        print(f"Student '{student}' not found.") 

        return 

 

    course = input("Enter course to update/add: ").strip() 

    if not course: 

        print("Course name cannot be empty.") 

        return 

 

    try: 

        score = float(input("Enter new grade: ").strip()) 

    except ValueError: 

        print("Invalid grade. Must be a number.") 

        return 

 

    grades[course] = score 

    print(f"Updated grade for {student} - {course}: {score}.") 

 

def calculateGPA(directory, student): 

    """Calculate the average grade (GPA) for a student.""" 

    grades = getStudentGrades(directory, student) 

    if grades is None: 

        return None 

    if not grades: 

        return 0.0 

 

    total = sum(grades.values()) 

    return total / len(grades) 

 

def checkHonorRoll(directory, student): 

    """Return True if student is on the honor roll. 

 

    Honor roll criteria: 

    - GPA >= 88 

    - All grades strictly above 81 

    """ 

    grades = getStudentGrades(directory, student) 

    if grades is None or not grades: 

        return False 

 

    gpa = calculateGPA(directory, student) 

    if gpa is None: 

        return False 

 

    if gpa < 88: 

        return False 

 

    return all(score > 81 for score in grades.values()) 

 

def printMenu(): 

    """Print the user menu.""" 

    print("\n=== Student Directory Menu ===") 

    print("1) Show student record") 

    print("2) Show student grades") 

    print("3) Show student grade level") 

    print("4) Show student email") 

    print("5) List students by grade level") 

    print("6) Add a student") 

    print("7) Remove a student") 

    print("8) Update a student's grade") 

    print("9) Check honor roll") 

    print("0) Quit") 

 

def main(): 

    Students = { 

        "Alice": {"grade_level": 10, "email": "alice@example.com", "grades": {"Math": 92, "English": 88}}, 

        "Bob": {"grade_level": 11, "email": "bob@example.com", "grades": {"Chemistry": 79, "History": 85}}, 

    } 

 

    while True: 

        printMenu() 

        choice = input("Choose an option: ").strip() 

 

        if choice == "0": 

            print("Goodbye!") 

            break 

 

        if choice in {"1", "2", "3", "4", "8", "9", "7"}: 

            student = input("Enter student name: ").strip() 

 

        if choice == "1": 

            record = getStudent(Students, student) 

            if not record: 

                print(f"Student '{student}' not found.") 

            else: 

                print(f"Record for {student}: {record}") 

 

        elif choice == "2": 

            grades = getStudentGrades(Students, student) 

            if grades is None: 

                print(f"Student '{student}' not found.") 

            else: 

                print(f"Grades for {student}:") 

                for course, score in grades.items(): 

                    print(f" - {course}: {score}") 

 

        elif choice == "3": 

            grade_level = getStudentGradeLevel(Students, student) 

            if grade_level is None: 

                print(f"Student '{student}' not found.") 

            else: 

                print(f"{student} is in grade {grade_level}.") 

 

        elif choice == "4": 

            email = getStudentEmail(Students, student) 

            if email is None: 

                print(f"Student '{student}' not found.") 

            else: 

                print(f"{student}'s email: {email}") 

 

        elif choice == "5": 

            try: 

                gradelevel = int(input("Enter grade level to list: ").strip()) 

                getStudentsByGradeLevel(Students, gradelevel) 

            except ValueError: 

 print("Invalid grade level. Must be an integer.") 

 

elif choice == "6": 

 addStudent(Students) 

 

elif choice == "7": 

removeStudent(Students, student) 

 

 elif choice == "8": 

 updateGrade(Students, student) 

 

 elif choice == "9": 

 is_honor = checkHonorRoll(Students, student) 

if is_honor: 

print(f"{student} is on the honor roll!") 

else: 

print(f"{student} is not on the honor roll.") 

 

else: 

print("Invalid option. Please choose a number from the menu.") 

 

if __name__ == "__main__": 

main() 