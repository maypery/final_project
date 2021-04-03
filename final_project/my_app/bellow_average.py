import json
from average_salary import *

with open('employees.json') as f:
    employees = json.load(f)
    bellow_average = []
    for employee in employees:
        hire_date = employee['hire_date']
        split_date = hire_date.split('/')
        hire_year = split_date[2]
        seniority = 2021 - int(hire_year)
        salary = employee['salary']

        if salary < av_salary and seniority > 1:
            bellow_average.append(employee)
        else:
            continue

with open('bellow_average.txt','w') as file:
    for element in bellow_average:
        full_name = element['first_name'] + ' ' + element['last_name']
        file.write(full_name + '\n')
        file.write(json.dumps(element) + '\n')