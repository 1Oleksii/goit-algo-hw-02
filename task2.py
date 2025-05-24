from collections import deque

def is_palindrome(input_string):
    # Перетворюємо рядок у нижній регістр та видаляємо пробіли
    cleaned = ''.join(char.lower() for char in input_string if char != ' ')
    
    # Додаємо всі символи до двосторонньої черги
    char_deque = deque(cleaned)
    
    # Порівнюємо символи з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False  # Якщо символи не збігаються — це не паліндром
    return True  # Якщо всі символи збіглися — це паліндром

# Приклади використання
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("racecar"))                      # True
print(is_palindrome("Hello World"))                  # False
