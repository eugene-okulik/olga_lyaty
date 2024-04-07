'''Создайте универсальный декоратор, который можно будет применить к любой функции. 
Декоратор должен делать следующее: он должен распечатывать слово "finished"
после выполнения декорированной функции.

Код, использующий этот декоратор может выглядеть, например, так:

@finish_me
def example(text):
    print(text)
    
example('print me')
В результате работы будет такое:

print me

finished'''


def example_decorator(func):
    def wrapper(*args):
        print()
        func(*args)
        print()
        print('finished')

    return wrapper


@example_decorator
def example(text):
    print(text)
    
example('print me')
