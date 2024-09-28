from queue import Queue
import time

class Request:
    # Лічильник для генерації унікальних ідентифікаторів
    _id_counter = 0  

    def __init__(self):
        self.request_id = Request._get_next_id()

    @classmethod
    def _get_next_id(cls):
        cls._id_counter += 1
        return cls._id_counter

class ServiceCenter:
    def __init__(self):
        self.requests = Queue()

    def new_request(self, request):
        self.requests.put(request)

    def process_requests(self):
        while not self.requests.empty():
            current_request = self.requests.get()
            print(f"Обробляємо заявку {current_request.request_id}")
            print(f"Заявка {current_request.request_id} успішно оброблена.\n")

# Створюємо сервісний центр
service_center = ServiceCenter()

# Додаємо заявки з унікальними ідентифікаторами
for i in range(5):
    service_center.new_request(Request())

# Обробляємо заявки
service_center.process_requests()