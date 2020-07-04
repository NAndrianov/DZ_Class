# Вы приехали помогать на ферму Дядюшки Джо и видите вокруг себя множество разных животных:
#
# гусей "Серый" и "Белый"
# корову "Маньку"
# овец "Барашек" и "Кудрявый"
# кур "Ко-Ко" и "Кукареку"
# коз "Рога" и "Копыта"
# утку "Кряква"
# Со всеми животными вам необходимо как-то взаимодействовать:
#
# кормить
# корову и коз доить
# овец стричь
# собирать яйца у кур, утки и гусей
# различать по голосам(коровы мычат, утки крякают и т.д.)
#
# Задача №1
# Нужно реализовать классы животных, не забывая использовать наследование, определить общие методы взаимодействия с животными и дополнить их в дочерних классах,
# если потребуется.
#
# Задача №2
# Для каждого животного из списка должен существовать экземпляр класса. Каждое животное требуется накормить и подоить/постричь/собрать яйца, если надо.
#
# Задача №3
# У каждого животного должно быть определено имя(self.name) и вес(self.weight).
#
# Необходимо посчитать общий вес всех животных(экземпляров класса);
# Вывести название самого тяжелого животного.

from functools import reduce

class Animal:
    #weight = 0
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def makeNoise(self):
       pass

    def feed(self):
        print(self.name + " накормлен(а)")

    def milk(self):
        print(self.name + " подоили")

    def cut(self):
        print(self.name + " пострижен(а)")

    def collect_eggs(self):
        print(self.name + " собрали яйца")


class Cow(Animal):
    def makeNoise(self):
        print(self.name + " издает звук: Muo!")


class Chicken(Animal):
    def makeNoise(self):
        print(self.name + " издает звук: Ko-ko!")


class Sheep(Animal):
    def makeNoise(self):
        print(self.name + " издает звук: Be!")


class Goat(Animal):
    def makeNoise(self):
        print(self.name + " издает звук: Me!")


class Duck(Animal):
    def makeNoise(self):
        print(self.name + " издает звук: Krya-Krya!")


class Geese(Animal):
    def makeNoise(self):
        print(self.name + " издает звук: Ga-GA!")


geese1 = Geese("Гусыня Серая", 20)
geese2 = Geese("Гусыня Белая", 22)
cow = Cow("Корова Манька", 480)
sheep1 = Sheep("Баран Барашек", 50)
sheep2 = Sheep("Баран Кудрявый", 50)
chicken1 = Chicken("Курица Ко-Ко", 5)
chicken2 = Chicken("Петух Кукареку", 8)
goat1 = Goat('Козел Рога', 25)
goat2 = Goat("Коза Копыта", 20)
duck = Duck("Утка Кряква", 10)

geese1.makeNoise()
geese1.feed()
geese1.collect_eggs()
print("Вес", geese1.name, "составляет", geese1.weight, "кг")
print(" ")
geese2.makeNoise()
geese2.feed()
geese2.collect_eggs()
print("Вес", geese2.name, "составляет", geese2.weight, "кг")
print(" ")
cow.makeNoise()
cow.feed()
cow.milk()
print ("Вес", cow.name, "составляет", cow.weight, "кг")
print(" ")
sheep1.makeNoise()
sheep1.feed()
sheep1.cut()
print ("Вес", sheep1.name, "составляет", sheep1.weight, "кг")
print (" ")
sheep2.makeNoise()
sheep2.feed()
sheep2.cut()
print ("Вес", sheep2.name, "составляет", sheep2.weight, "кг")
print (" ")
goat1.makeNoise()
goat1.feed()
print ("Вес", goat1.name, "составляет", goat1.weight, "кг")
print (" ")
goat2.makeNoise()
goat2.feed()
goat2.milk()
print ("Вес", goat2.name, "составляет", goat2.weight, "кг")
print (" ")
chicken1.makeNoise()
chicken1.feed()
chicken1.collect_eggs()
print ("Вес", chicken1.name, "составляет", chicken1.weight, "кг")
print (" ")
chicken2.makeNoise()
chicken2.feed()
print ("Вес", chicken2.name, "составляет", chicken2.weight, "кг")
print (" ")
duck.makeNoise()
duck.feed()
duck.collect_eggs()
print ("Вес", duck.name, "составляет", duck.weight, "кг")

#Необходимо посчитать общий вес всех животных(экземпляров класса);
#Вывести название самого тяжелого животного.

animals = [
  geese1,
  geese2,
  cow,
  sheep1,
  sheep2,
  chicken1,
  chicken2,
  goat1,
  goat2,
  duck
]

animal_weights = [animal.weight for animal in animals]
sum_weight = reduce((lambda x, y: x + y), animal_weights)
max_weight = max(animal_weights)
print (" ")
print("Суммарный вес всех домашних животных составляет:", sum_weight)
print("Самое тяжелое животное весит:", max_weight)
