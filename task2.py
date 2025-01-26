"""task2.py"""
from collections import deque
import re

def is_palindrome(value):
    # Нормалізуємо вхідний рядок: перетворюємо його в нижній регістр і видаляємо пробіли
    normalized_string = re.sub(r"[^a-zA-Z0-9]", "", value.lower())

    # Створюємо двобічну чергу (deque) і додаємо всі символи
    char_deque = deque(normalized_string)

    while len(char_deque) > 1:
        # Порівнюємо символи на обох кінцях
        if char_deque.popleft() != char_deque.pop():
            return False

    return True

# Тести
test_strings = [
    "radar",
    "kayak",
    "deified",
    "noon",
    "saippuakivikauppias",
    "Evade me, Dave!",
    "A man, a plan, a canal: Panama",
    "No 'x' in Nixon",
    "Was it a car or a cat I saw?",
    "The end"
]

for test in test_strings:
    print(f"'{test}', чи є паліндромом: {is_palindrome(test)}")
