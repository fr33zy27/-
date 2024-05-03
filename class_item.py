import random
from random import randint


class Item:
    def __init__(self, name):
        self.name = name
        self.__value = 0

    # Возвращает значение предмета для использования
    def use(self):
        return self.__value


class Food(Item):
    def __init__(self, name):
        super().__init__(name)
        self.__value = randint(5, 30)
