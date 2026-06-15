import os
os.system("cls")

from abc import ABC, abstractmethod

class Player(ABC):
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def kick(self):
        pass

    @abstractmethod
    def jump(self):
        pass

class Ironman(Player):
    def run(self):
        print("Yuguryapti...")
    
    def kick(self):
        print("Tepmoqda...")

    def jump(self):
        print("Sakramoqda...")
    
    def fly(self):
        print("Ironman is flying...")

i1 = Ironman()
i1.fly()
i1.run()