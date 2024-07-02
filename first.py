# Перше завдання
from datetime import datetime

def get_days_from_today(date_str):
    """
    Розраховує кількість днів між заданою датою і поточною датою.

    Args:
    date_str (str): Дата у форматі 'РРРР-ММ-ДД'.

    Returns:
    int: Кількість днів від заданої дати до поточної. Від'ємне значення, якщо задана дата пізніша за поточну.
    """
    try:
        # Перетворюємо рядок у об'єкт datetime
        given_date = datetime.strptime(date_str, '%Y-%m-%d')
        
        # Отримуємо поточну дату
        current_date = datetime.today()
        
        # Розраховуємо різницю між датами
        delta = current_date - given_date
        
        # Повертаємо кількість днів як ціле число
        return delta.days
    except ValueError:
        # У разі неправильного формату дати повертаємо відповідне повідомлення про помилку
        return "Неправильний формат дати. Будь ласка, використовуйте формат 'РРРР-ММ-ДД'."

# Приклад виклику функції
print(get_days_from_today("2021-07-02"))  # Наприклад, якщо сьогодні 2 липня 2021 року
print(get_days_from_today("2026-12-18"))  # Приклад з майбутньою датою
print(get_days_from_today("hello"))   # Приклад з неправильним форматом дати