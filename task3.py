# Функція для перевірки симетрії дужок
def is_symmetric(expression):
    # Створюємо стек для збереження відкритих дужок
    stack = []
    # Визначаємо пари відкритих і закритих дужок
    pairs = {')': '(', ']': '[', '}': '{'}

    # Проходимо по кожному символу у виразі
    for char in expression:
        # Якщо символ - відкрита дужка, додаємо у стек
        if char in '([{':
            stack.append(char)
        # Якщо символ - закрита дужка
        elif char in ')]}':
            # Якщо стек порожній або остання відкрита дужка не відповідає — несиметрично
            if not stack or stack[-1] != pairs[char]:
                return "Несиметрично"
            # Якщо все гаразд — видаляємо з вершини стеку
            stack.pop()

    # Якщо після перевірки стек порожній — симетрично
    return "Симетрично" if not stack else "Несиметрично"


# Приклади використання
examples = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

# Перевіряємо кожен приклад
for ex in examples:
    print(f"{ex}: {is_symmetric(ex)}")
