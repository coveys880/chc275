def getStudent(directory, student):
    return directory[student]


def getStudentGrades(directory, student):
    return directory[student]["grades"]
def getStudentGradeLevel(directory,student):
    return directory[student]["gradelevel"]

def getStudentEmail(directory,student):
    return directory[student]["studentemail"]
def getStudentsByGradeLevel(directory, gradelevel):
    for student in directory:
        if directory[student]["gradelevel"] == gradelevel:
            print(directory[student])
   
def addStudent(directory):
    student = {}
    name = input("What is the name of the new student?").strip()
    gradelevel = int(input("What is the gradelevel of said student?"))
    email = input("what is the email of said student?").strip()
    englishgrade = int(input("what is the english grade of the student?"))
    mathgrade = int(input("what is the math grade of the student?"))
    historygrade = int(input("what is the history grade of the student?"))
    religiongrade = int(input("what is the religion grade of the student?"))
    grades = {"math":mathgrade,"history":historygrade,"religion":religiongrade,"english":englishgrade}
    student["email"] = email
    student["gradelevel"] = gradelevel
    student["grades"] = grades
    directory[name] = student


def removeStudent(directory, student):
    directory.pop(student)
def updateGrade(directory, student):
    for grade in directory[student]["grades"]:
        directory[student]["grades"][grade] = int(input(f"what is the new grade for {grade}?"))
       
   

def calculateGPA(directory, student):
    GPA = 0
    for grades in directory[student]["grades"]:
        GPA += directory[student]["grades"][grades]
       
    GPA/= len(directory[student]["grades"])
    return GPA


def checkHonorRoll(directory,student):
    GPA = calculateGPA(directory,student)
    for grades in directory[student]["grades"]:
        if directory[student]["grades"][grades] < 81:
            return False
    if GPA >= 88:
        return True
    else:
        return False
def printMenu():
    print("Welcome to Calvet Hall Student Directory")
    print("1. Add student")
    print("2. Remove Student")
    print("3. Get Student")
    print("4. update grades")
    print("5. calculate GPA")
    print("6. Get students grade level")
    print("7. Exit")
    option = input("What option would you like?")
    return option

def main():
    Students = {}
    while True:
        menu = printMenu()
        if menu == "1":
            addStudent(Students)
        if menu == "2":
            name = input("What is the students name")
            removeStudent(Students,name)
        if menu == "3":
            name = input("What student do you wanna get")
            print(getStudent(Students,name))
        if menu == "4":
            name = input("whose grade are you updating")
            updateGrade(Students,name)
        if menu == "5":
            name = input("What student would you like?")
            GPA = calculateGPA(Students,name)
            if checkHonorRoll(Students, name):
                print(f"The student {name} had a GPA of {GPA} and made HonorRoll")
            else:
                print(f"The student{name} had a GPA of {GPA} and didn't make HonorRoll")
        if menu == "6":
            gradelevel = int(input("What gradelevel are they in"))
            getStudentsByGradeLevel(Students,gradelevel)
        if menu == "7":
            print("Have a nice day")
            break
       
if __name__ == "__main__":
    main()
    
    