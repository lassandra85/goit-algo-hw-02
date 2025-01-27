from collections import deque
import re

def is_palindrome(value):
    # Переводимо рядок у нижній регістр і видаляємо всі пробіли а також інші символи, крім букв
    normalized_string = re.sub(r"[^a-zA-Z0-9]", "", value.lower())

    # Якщо рядок містить менше двох символів, він автоматично є паліндромом
    if len(normalized_string) < 2:
        return True

    # Створюємо двосторонню чергу (deque) і заповнюємо її символами рядка
    deque_str = deque(normalized_string)

    # Порівнюємо символи з обох кінців черги, поки вона не спорожніє
    while len(deque_str) > 1:
        if deque_str.popleft() != deque_str.pop():
            return False # Якщо не співпадають - це не паліндром

    return True # Якщо всі символи співпали

test_strings = [
    "Hello, World!",
    "Ukraine will win",
    "Ukraine will win, enemies loses",
    "I believe in the A F U",
    "I believe in the AFU",
    "A"
]

for string in test_strings:
    print(f"'{string}' -> Паліндром: {is_palindrome(string)}")