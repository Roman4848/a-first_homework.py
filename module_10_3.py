import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0  # Начальный баланс
        self.lock = threading.Lock()  # Объект блокировки

    def deposit(self):
        for _ in range(100):  # 100 транзакций пополнения
            amount = random.randint(50, 500)  # Случайная сумма пополнения
            with self.lock:  # Блокируем доступ к балансу
                self.balance += amount  # Увеличиваем баланс
                print(f"Пополнение: {amount}. Баланс: {self.balance}")
                # Проверяем, если баланс >= 500 и замок не заблокирован
                if self.balance >= 500 and not self.lock.locked():
                    self.lock.release()  # Разблокируем, если он был заблокирован
            time.sleep(0.001)  # Имитация скорости выполнения

    def take(self):
        for _ in range(100):  # 100 транзакций снятия
            amount = random.randint(50, 500)  # Случайная сумма снятия
            print(f"Запрос на {amount}")
            with self.lock:  # Блокируем доступ к балансу
                if amount <= self.balance:  # Если достаточно средств
                    self.balance -= amount  # Уменьшаем баланс
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")  # Недостаточно средств
                    # Блокируем поток, если недостаточно средств
                    self.lock.acquire()
            time.sleep(0.001)  # Имитация скорости выполнения

# Создание объекта класса Bank
bk = Bank()

# Создание потоков для методов deposit и take
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

# Запуск потоков
th1.start()
th2.start()

# Ожидание завершения потоков
th1.join()
th2.join()

# Вывод итогового баланса
print(f'Итоговый баланс: {bk.balance}')