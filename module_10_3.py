import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 500  # Начальный баланс
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
                amount = random.randint(50, 500)  # Случайная сумма пополнения
                with self.lock:  # Блокировка потока
                    self.balance += amount
                    if self.balance >= 500 and self.lock.locked():
                        self.lock.release()  # Освобождение замка
                    print(f"Пополнение: {amount}. Баланс: {self.balance}.")
                time.sleep(0.001)  # Имитация задержки

    def take(self):
        for _ in range(100):
            request = random.randint(50, 500)
            print(f"Запрос на {request}")
            with self.lock:
                if request <= self.balance:
                    self.balance -= request
                    print(f"Снятие: {request}. Баланс: {self.balance}")
                else:
                    print("Запрос отклонён, недостаточно средств")
                    self.lock.acquire()  # Блокировка потока
                    time.sleep(1)  # Ожидание
                    self.lock.release()  # Разблокировка


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')