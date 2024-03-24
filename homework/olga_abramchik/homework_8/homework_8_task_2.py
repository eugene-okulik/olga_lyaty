import sys

sys.set_int_max_str_digits(0)


def fibonacci_gen():
    f0, f1 = 0, 1
    while True:
        yield f0
        f0, f1 = f1, f0 + f1


f = fibonacci_gen()
count = 0
while True:
    count += 1
    f_number = next(f)
    if count == 5:
        print(f'5-ое чиcло Фибоначчи: {f_number}')
    elif count == 200:
        print(f'200-ое чиcло Фибоначчи: {f_number}')
    elif count == 1000:
        print(f'1 000-ое чиcло Фибоначчи: {f_number}')
    elif count == 100000:
        print(f'100 000-ое чиcло Фибоначчи: {f_number}')
        break
