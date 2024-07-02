# Друге завдання
import random

def get_numbers_ticket(min_num, max_num, quantity):
    """
    Генерує набір унікальних випадкових чисел у заданому діапазоні.
    
    Args:
    min_num (int): Мінімальне можливе число у наборі (не менше 1).
    max_num (int): Максимальне можливе число у наборі (не більше 1000).
    quantity (int): Кількість чисел, які потрібно вибрати (значення між min_num і max_num).

    Returns:
    list: Відсортований список випадкових унікальних чисел. Повертає порожній список, якщо параметри не відповідають обмеженням.
    """
    # Перевіряємо коректність параметрів
    if min_num < 1 or max_num > 1000 or quantity > (max_num - min_num + 1) or quantity < 1:
        return []
    
    # Генеруємо унікальні випадкові числа
    unique_numbers = random.sample(range(min_num, max_num + 1), quantity)
    
    # Повертаємо відсортований список
    return sorted(unique_numbers)

# Приклади виклику функції
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 1000, 10)
print("Ваші лотерейні числа:", lottery_numbers)

lottery_numbers = get_numbers_ticket(1, 5, 6)  # Параметри не відповідають обмеженням
print("Ваші лотерейні числа:", lottery_numbers)