def print_number(result):
    result_new = result.split()
    return (int(result_new[-1]) + 10)

print(print_number('результат операции: 42'))
print(print_number('результат операции: 54'))
print(print_number('результат работы программы: 209'))
print(print_number('результат: 2'))
