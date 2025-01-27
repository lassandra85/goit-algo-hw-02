import queue
import random
import time

# Створення черги заявок
app_queue = queue.Queue()

def generate_request():
    # Створення нової заявки з унікальним id
    requests_id = random.randint(1, 100)
    print(f"Створено заявку: {requests_id}")
    # Додавання заявки до черги
    app_queue.put(requests_id)

def process_request():
    # Якщо черга не порожня
    if not app_queue.empty():
        # Видалення заявки з черги
        requests_id = app_queue.get()
        # Обробка заявки
        print(f"Обробка заявки: {requests_id}")
    else:
        # Виведення повідомлення про порожню чергу
        print("Черга порожня")


# Головний цикл програми
try:
    while True:
        # Виклик функції для створення нових заявок
        generate_request()
        # Виклик функції для обробки заявок
        process_request()
        # Імітація затримки між операціями
        time.sleep(1)

except KeyboardInterrupt:
    print("Вихід з програми.")  # Для виходу натисніть Ctrl + C