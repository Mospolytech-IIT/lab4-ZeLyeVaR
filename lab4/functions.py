from exceptions import InvalidInputError, CalculationError, DataNotFoundError

def divide(a, b):
    """Деление двух чисел."""
    if b == 0:
        raise ZeroDivisionError("Деление на ноль.")
    return a / b

def square_root(x):
    """Квадратный корень."""
    if x < 0:
        raise ValueError("Нельзя извлекать квадратный корень из отрицательного числа.")
    return x ** 0.5

def calculate_average(numbers):
    """Среднее значение."""
    try:
        if not numbers:
            raise InvalidInputError("Список не должен быть пустым.")
        return sum(numbers) / len(numbers)
    except Exception as e:
        print(f"Ошибка: {e}")

def process_data(data):
    """Обработка данных."""
    try:
        if not isinstance(data, list):
            raise TypeError("Ожидается список.")
        if len(data) == 0:
            raise DataNotFoundError("Данные отсутствуют.")
        return [x * 2 for x in data]
    except Exception as e:
        print(f"Обработка данных завершилась с ошибкой: {e}")
    finally:
        print("Завершение обработки данных.")

def risky_calculation(x):
    """Рискованные вычисления."""
    try:
        if x < 0:
            raise CalculationError("Некорректный ввод для вычислений.")
        return 100 / x
    except CalculationError as ce:
        print(f"Ошибка вычисления: {ce}")
    except ZeroDivisionError as zde:
        print(f"Ошибка деления: {zde}")
    except Exception as e:
        print(f"Общая ошибка: {e}")
    finally:
        print("Завершение рискованных вычислений.")

def generate_exception(value):
    """Генерация исключений."""
    try:
        if value < 0:
            raise InvalidInputError("Отрицательное значение.")
        if value == 0:
            raise CalculationError("Нулевое значение.")
    except InvalidInputError as ie:
        print(f"Обработка InvalidInputError: {ie}")
    except CalculationError as ce:
        print(f"Обработка CalculationError: {ce}")
    finally:
        print("Завершение генерации исключений.")
