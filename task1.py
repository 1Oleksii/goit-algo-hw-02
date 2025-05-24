import queue
import time
import random

# Створення черги заявок
request_queue = queue.Queue()

# Лічильник для унікального номера заявки
request_counter = 1

# Функція генерації нової заявки
def generate_request():
    global request_counter
    request = f"Заявка №{request_counter}"
    request_queue.put(request)
    print(f"[+] Створено: {request}")
    request_counter += 1

# Функція обробки заявки
def process_request():
    if not request_queue.empty():
        request = request_queue.get()
        print(f"[-] Обробляється: {request}")
    else:
        print("[!] Черга пуста. Немає заявок для обробки.")

# Головний цикл програми
def main_program():
    print("Імітація роботи сервісного центру. Натисніть Ctrl+C для зупинки.")
    try:
        while True:
            generate_request()
            time.sleep(random.uniform(0.5, 1.5))  # Пауза між створенням заявок
            process_request()
            time.sleep(random.uniform(0.5, 1.5))  # Пауза між обробками
    except KeyboardInterrupt:
        print("\n[✋] Програму зупинено користувачем.")

# Запуск програми
main_program()