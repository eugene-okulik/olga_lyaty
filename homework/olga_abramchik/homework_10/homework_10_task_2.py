'''Создайте универсальный декоратор, который будет управлять тем, 
сколько раз запускается декорируемая функция
Код, использующий этот декоратор может выглядеть, например, так:

@repeat_me
def example(text):
    print(text)
    
example('print me', count=2)
В результате работы будет такое:

print me

print me

Если есть время и желание погуглить и повозиться, то можно попробовать создать декоратор, 
который сможет обработать такой код:

@repeat_me(count=2)
def example(text):
    print(text)
    
example('print me')'''


# version 1

def repeat_me(func):
        def wrapper(*args, **kwargs):
            for _ in range(*(kwargs.values())):
                print()
                result = func(*args)
            return result
               
        return wrapper


@repeat_me
def example(text):
    print(text)
    
example('print me', count=2)


# version 2

def repeat_me(count):
    def decorator(func):
        def wrapper(*args):
            for _ in range(count):
                print()
                result = func(*args)
            return result
               
        return wrapper
    return decorator


@repeat_me(count=2)
def example(text):
    print(text)
    
example('print me')
