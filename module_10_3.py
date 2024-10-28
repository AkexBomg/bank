import random
import threading
import time

class Bank:

    def __init__(self, balance, lock = threading.Lock()):
        self.balance = balance
        self.lock = lock

    def deposit(self):
        i = 0
        while i < 100:
            if self.balance >= 500 and self.lock.locked() == True:
                self.lock.release()
            cashe = random.randint(50, 500)
            self.balance = self.balance + cashe
            time.sleep(0.01)
            print(f"Пополнение: {cashe}, Баланс: {self.balance} ")
            i = i+1

    def take(self):
        i = 0
        while i < 100:
            cashe = random.randint(50, 500)
            print(f"Запрос на: {cashe}")
            if self.balance < cashe:
                print("Запрос отклонен, недостаточно средств")
                self.lock.acquire()
            else:
                self.balance = self.balance - cashe
                print(f"Снятие: {cashe}, Баланс: {self.balance} ")
            i = i + 1


bk = Bank(balance=0)

th1 = threading.Thread(target = Bank.deposit, args = (bk,))
th2 = threading.Thread(target = Bank.take, args = (bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
print(f'Итоговый баланс: {bk.balance}')
