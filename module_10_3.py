import threading
import random
import time

class Bank:
    def __init__(self, balance):
        self.balance = balance  # Начальный баланс
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            if self.balance >= 500 and self.lock.locked() == True:
                self.lock.release()  # Освобождение замка
            amount = random.randint(50, 500)  # Случайная сумма пополнения
            self.balance += amount
            time.sleep(0.001)  # Имитация задержки
            print(f"Пополнение: {amount}. Баланс: {self.balance}.")

    def take(self):
        for _ in range(100):
            request = random.randint(50, 500)
            print(f"Запрос на {request}")
            if request <= self.balance:
                self.balance -= request
                print(f"Снятие: {request}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()  # Блокировка потока


bk = Bank(balance = 0)

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
