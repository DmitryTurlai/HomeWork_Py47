from time import timedef cache_decorator(func):
    time_save = 15    cache = {}
    def wrapper(*args):        if args in cache and time() <= cache[args]['time'] + time_save: # проверка есть ли в кэше результат с данными параметрами и прошло ли заданное в начале время хранения
            print('Результат взят из кэша')            return cache[args]['result']
        else:            result = func(*args) # запуска расчетов с помощью функции
            cache[args] = {'result': result, 'time': time()} # сохранения результатов вычисления функции и текущего времени в кэш            print('Результат взят из рассчитанной функции и сохранен в кэш')
            return result
    return wrapper
@cache_decoratordef sum(a, b):
    return a + b
while True:    a = int(input('Введите а:'))
    b = int(input('Введите b:')) # если думать дольше 15 сек над вводом - результат будет условно удален из кэша    print(f"Сумма {a} + {b} = {sum(a, b)}") # вызываем расчет, который с помощью декоратора либо вычисляется функцией
