#Design a menu-driven program using user-defined functions to manage student grades, where each student's information is stored as a tuple. The program should allow the user to:
#- Add a new student’s name and grades (store as a tuple)
#- View all student names and their corresponding grades
#- Calculate and display the average grade of a student
#- Find and display the student with the highest grade
#- Find and display the student with the lowest grade
#- Search for a student by name and display their grades
import random
import string
students = []
def enterStudent(name,g1,g2,g3):
    students.append((name,g1,g2,g3))

def viewGrades():
    for student in students:
        print(student[0]," - ",student[1],student[2],student[3])

def studentAverage(n):
    sum = 0
    for i in range(1,4,1):
        sum += students[n][i] 
    print("Average of ",students[n][0],"is ",sum/3)

def highGrade():
    high = 0
    name = ''
    for student in students:
        for i in range(1,4,1):
            if student[i] > high:
                high = student[i]
                name = student[0]
    print("The highest grade is", high,"of ",name)

def lowGrade():
    low = 100
    name = ''
    for student in students:
        for i in range(1,4,1):
            if student[i] <  low:
                low = student[i]
                name = student[0]
    print("The lowest grade is", low,"of ",name)

def search(name):
    for student in students:
        if student[0]==name:
            print(student[0]," - ",student[1],student[2],student[3])
            break

enterStudent("Sri", 30, 40, 30)
enterStudent("Arun", 85, 90, 75)
enterStudent("Meena", 60, 70, 80)
enterStudent("Ravi", 95, 88, 92)
enterStudent("Kiran", 45, 50, 55)
enterStudent("Anjali", 78, 82, 89)
enterStudent("Pooja", 90, 85, 88)
enterStudent("Ajay", 50, 60, 65)
enterStudent("Sneha", 75, 80, 70)
enterStudent("Raj", 65, 55, 60)


while True:
    print("1: Add a new student’s name and grades")
    print("2: View all student names and their corresponding grades")
    print("3: Calculate and display the average grade of a student")
    print("4: Find and display the student with the highest grade")
    print("5: Find and display the student with the lowest grade")
    print("6: Search for a student by name and display their grades")
    c = random.randint(1,10)
    print("Enter your choice: ",c)
    if c==1:
        name = ''.join(random.choices(string.ascii_letters, k=5))
        print("Enter student name: ",name)
        g1= random.randint(1,100)
        g2= random.randint(1,100)
        g3= random.randint(1,100)
        print("Enter student grades:",g1,g2,g3)
        enterStudent(name,g1,g2,g3)
        print(students[len(students)-1][0]," - ",students[len(students)-1][1],students[len(students)-1][2],students[len(students)-1][3])
        break
    elif c==2:
        viewGrades()
        break
    elif c==3:
        i = random.randint(0,len(students))
        print("Enter the rollno of student to display:",i)
        studentAverage(i)
        break
    elif c==4:
        highGrade()
        break
    elif c==5:
        lowGrade()
        break
    elif c==6:
        name = 'Sri'
        search(name)
        break
    else:
        print("Enter the correct value: ")
        c = random.randint(1,6)