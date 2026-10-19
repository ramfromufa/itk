from functools import wraps
from time import sleep
from random import choice

def retry(max_attempts, delay):
    def decorator_retry(func):
        @wraps(func)
        def wrapper():
            for attempt in range(max_attempts):
                try:
                    return func() # Оператор return, чтобы прервать цикл попыток при удачном выполнении
                except Exception as e:
                    print(f'\ntry {attempt + 1}\n{e}')
                    if attempt == max_attempts - 1: raise e
                    sleep(delay)
        return wrapper
    return decorator_retry

@retry(3, 1)
def func():
    """Рандомный генератор ошибок и их отсутствия"""
    print(f'\n{1/choice([1, 0, 'str'])}')
 
# Проверка 
    
try:
    func()
except Exception as e:
    print(f'\nlast exception\n{e}')

print(f'\n{func.__name__}\n{func.__doc__}')

