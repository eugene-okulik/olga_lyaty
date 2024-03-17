import random

number = random.randint(1, 11)

while True:
    user_number = int(input('Угадайте цифру: '))
    if user_number == number:
        print('Поздравляю! Вы угадали!')
        break
    else:
        print('попробуйте снова')
