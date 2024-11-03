import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100  
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            time.sleep(1)
            self.days += 1
            self.enemies -= self.power


            remaining_enemies = max(self.enemies, 0)
            day_word = "день" if self.days == 1 else "дня"
            print(f"{self.name}, сражается {self.days} {day_word}..., осталось {remaining_enemies} воинов.")


        print(f"{self.name} одержал победу спустя {self.days} {day_word}!")



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)


first_knight.start()
second_knight.start()


first_knight.join()
second_knight.join()


print("Все битвы закончились!")
