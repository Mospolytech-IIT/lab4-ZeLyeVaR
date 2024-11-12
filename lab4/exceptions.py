class InvalidInputError(Exception):
    """Исключение для некорректного ввода."""
    pass

class CalculationError(Exception):
    """Исключение для ошибок в расчетах."""
    pass

class DataNotFoundError(Exception):
    """Исключение для отсутствия данных."""
    pass