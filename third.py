# Третє завдання
import re

def normalize_phone(phone_number):
    """
    Нормалізує телефонний номер до стандартного формату, залишаючи тільки цифри та символ '+' на початку.
    Додає код країни '+38' для України, якщо код відсутній.

    Args:
    phone_number (str): Телефонний номер у будь-якому форматі.

    Returns:
    str: Нормалізований телефонний номер.
    """
    # Видаляємо всі символи, крім цифр і '+'
    cleaned_number = re.sub(r'[^\d+]', '', phone_number)
    
    # Перевіряємо, чи починається номер з '+'
    if not cleaned_number.startswith('+'):
        if cleaned_number.startswith('380'):
            cleaned_number = '+' + cleaned_number
        else:
            cleaned_number = '+38' + cleaned_number
    elif not cleaned_number.startswith('+38') and cleaned_number.startswith('+'):
        cleaned_number = '+38' + cleaned_number[1:]
    
    return cleaned_number

# Приклад використання функції
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
