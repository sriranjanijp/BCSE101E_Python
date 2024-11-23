#Question 3
with open("student_data_24bce2635.txt","w") as file1:
    file1.write("John Computer_Science 2021 3.8 40\n")
    file1.write("Sarah Mechanical_Engineering 2020 3.5 50\n")
    file1.write("Mike Electrical_Engineering 2022 3.7 30\n")
    file1.write("Emma Civil_Engineering 2021 3.9 45\n")
    file1.write("Liam Computer_Science 2020 3.6 55\n")
with open("student_data_24bce2635.txt","r") as file2:   
    data = file2.readlines()

students = []
for student in data:
    students.append(student.strip().split(' '))

high_gpa = 0
high_gpa_student = ''
for student in students:
    if float(student[3]) > high_gpa:
        high_gpa = float(student[3])
        high_gpa_student = student[0]
    
print(f"{high_gpa_student} has the highest gpa of {high_gpa}")

gpa_sum = 0
count_2021 = 0
for student in students:
    if int(student[2]) == 2021:
        gpa_sum += float(student[3])
        count_2021 += 1

print(f"The average gpa of 2021 students is {gpa_sum/count_2021}")
check = False
print("Student with more than 35 credits in Electrical Engineering:")
for student in students:
    if student[1] == "Electrical_Engineering" and int(student[4])>35:
        print(student[0])
        check = True

if check == False:
    print("No students have more than 35 credits in ELectrical Engineering")

dept_credits = {}
dept_counts = {}
for student in students:
    if student[1] in dept_credits:
        dept_credits[student[1]] += int(student[4])
        dept_counts[student[1]] += 1
    else:
        dept_credits[student[1]] = int(student[4])
        dept_counts[student[1]] = 1

high_avg = 0
high_avg_dept = ''
for dept in dept_credits:
    avg = dept_credits[dept]/dept_counts[dept]
    if avg>high_avg:
        high_avg = avg
        high_avg_dept = dept

print(f"The {high_avg_dept} has the highest avg credits of {high_avg}")
