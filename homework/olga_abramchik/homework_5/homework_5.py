# Задание 1

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person
print(name, last_name, city, phone, country)

# Задание 2

result1 = 'результат операции: 42'
result2 = 'результат операции: 514'
result3 = 'результат работы программы: 9'

last_index_1 = result1.index(':') + 2
print(int(result1[last_index_1:]) + 10)

last_index_2 = result2.index(':') + 2
print(int(result2[last_index_2:]) + 10)

last_index_3 = result3.index(':') + 2
print(int(result3[last_index_3:]) + 10)

# Задание 3

students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']
students1 = ', '.join(students)
subjects1 = ', '.join(subjects)
text = f'Students {students1} study these subjects: {subjects1}'
print(text)
