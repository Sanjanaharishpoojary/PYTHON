class employee:
    def __init__(s):
        s.name = input("Enter Name: ")
        s.emp_id = int(input("Enter Employee ID: "))
        s.dept = input("Enter Dept: ")
        s.salary = float(input("Enter Salary: "))


    def update_sal(s, target_dept, new_salary):
        if s.dept == target_dept:
            s.salary = new_salary

    def display(s):
        print("Name: {} ID: {}, Department: {}, Salary: {}".format(s.name,s.emp_id,s.dept,s.salary))

employees = []
n = int(input("enter the number of employee"))
for i in range(n):
    employees.append(employee())

for obj in employees:
    obj.display()

target_dept = input("Enter the target department to update salary: ")
new_salary_value = int(input("Enter the new salary: "))
for obj in employees:
    obj.update_sal(target_dept, new_salary_value)

for i in employees:
    i.display()