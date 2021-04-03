import json

with open('employees.json') as f:
    employees = json.load(f)
    av_salary = 0
    employees_num = 0
    for employee in employees:
        employees_num += 1
        av_salary += employee['salary']
    av_salary = av_salary/employees_num
    print('The Average salary is:', av_salary)
