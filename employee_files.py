with open("employee_data_24BCE2635.txt", "w") as file1:
    file1.write("Alice Engineering 2020 90000 5\n")
    file1.write("Bob HR 2019 70000 3\n")
    file1.write("Carol Sales 2021 65000 4\n")
    file1.write("Dave Engineering 2022 95000 6\n")
    file1.write("Eve HR 2023 75000 2\n")

with open("employee_data_24BCE2635.txt", "r") as file2:
    data = file2.readlines()

employees = []
for emp in data:
    employees.append(emp.strip().split(' '))

#Which department has highest avg salary
dept_salary = {}
dept_counts = {}
for emp in employees:
    if emp[1] in dept_salary:
        dept_salary[emp[1]] += int(emp[3])
        dept_counts[emp[1]] += 1
    else:
        dept_salary[emp[1]] = int(emp[3])
        dept_counts[emp[1]] = 1

high_salary = 0
high_salary_dept = ''    
for dept in dept_salary:
    avg_salary = dept_salary[dept]/dept_counts[dept]
    if avg_salary > high_salary:
        high_salary = avg_salary
        high_salary_dept = dept

print(high_salary_dept," has the highest avg salary of",high_salary)

#Employee with highest no of projects in engineering dept
highest_proj = 0
highest_proj_emp = ''
for emp in employees:
    if emp[1]=="Engineering" and int(emp[4])>highest_proj:
        highest_proj = int(emp[4])
        highest_proj_emp = emp[0]

print(f"The employee with the highest no of projests is {highest_proj_emp} with {highest_proj} projects")

#Total employees after 2020
count_2020 = 0
for emp in employees:
    if int(emp[2])>2020:
        count_2020 += 1

print(f"{count_2020} employees joined after 2020")

#Average salary-to-projects ratio
salary_project = 0
for emp in employees:
    salary_project = float(emp[3])/float(emp[4])

print(f"The Average salary-to-projects ratio is {salary_project/len(employees)}")