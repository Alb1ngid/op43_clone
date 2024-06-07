import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Запоминаем время начала выполнения функции
        result = func(*args, **kwargs)  # Выполняем функцию
        end_time = time.time()  # Запоминаем время окончания выполнения функции
        elapsed_time = end_time - start_time  # Вычисляем затраченное время
        print(f"Функция {func.__name__} выполнялась {elapsed_time:.6f} секунд")
        return result
    return wrapper

# Пример использования декоратора
@timing_decorator
def example_function(n):
    total = 0
    for i in range(n):
        total += i
    return total

# Вызов функции
result = example_function(1000000)