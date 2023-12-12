from time import time

def cache_decorator(func):
    time_save = 15
    cache = {}

    def wrapper(*args):
        if args in cache and time() <= cache[args]['time'] + time_save:
            print('Результат взят из кэша')
            print(f'Время хранения: {round(abs(cache[args]["time"] - time()), 2)}')
            return cache[args]['result']
        else:
            result = func(*args)
            cache[args] = {'result': result, 'time': time()}
            print(f'Результат взят из рассчитанной функции {func.__name__} и сохранен в кэш')
            return result

    return wrapper

@cache_decorator
def sum_func(a, b):
    return a + b

@cache_decorator
def mult_func(a, b):
    return a * b

while True:
    a = int(input('Введите а:'))
    b = int(input('Введите b:'))

    print(f"Функция суммирования: {a} + {b} = {sum_func(a, b)}")

    a = int(input('Введите а:'))
    b = int(input('Введите b:'))

    print(f"Функция произведения: {a} * {b} = {mult_func(a, b)}")


