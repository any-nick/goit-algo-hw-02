from collections import deque

def preprocess_string(input_string):
    # Видаляємо пробіли та робимо всі символи маленькими
    return ''.join(char.lower() for char in input_string if char.isalnum())

def check_palindrome(input_string):
    # Попередня обробка рядка
    processed_string = preprocess_string(input_string)
    
    # Створюємо двосторонню чергу (deque)
    string_deque = deque(processed_string)

    # Порівнюємо символи з початку і кінця
    while len(string_deque) > 1:
        if string_deque.popleft() != string_deque.pop():
            return False
    
    return True

# Тестування
input_string = "Паліндром — і ні морд, ні лап"
if check_palindrome(input_string):
    print(f'"{input_string}" є паліндромом.')
else:
    print(f'"{input_string}" не є паліндромом.')