import random


salary = int(input('Enter your salary: '))
bonus = random.choice([True, False])
salary_all = 0

if bonus is True:
    salary_all = salary + random.randint(100, 1000)
else:
    salary_all = salary

print(f"{salary}, {bonus} - '${salary_all}'")
