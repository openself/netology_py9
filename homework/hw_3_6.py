# coding: utf-8
"""
Домашнее задание к лекции 3.6 «Классы и их применение в Python»

Необходимо реализовать классы животных на ферме:

    Коровы, козы, овцы, свиньи;
    Утки, куры, гуси.

Условия:

    Должен быть один базовый класс, который наследуют все остальные животные.
    Базовый класс должен определять общие характеристики и интерфейс.
"""

class Animal(object):
    def __init__(self, name):
        self.name = name
        print("Родилось животное.")

    def eat(self):
        print("Ням ням")

    def makeNoise(self):
        print(" ".join((self.name, "издает какой-то звук")))

class Artiodactyl(Animal):
    pass


class Birds(Animal):
    pass


class Cow(Artiodactyl):
    def __init__(self, *args, **kwargs):
        super(Cow, self).__init__(*args, **kwargs)
        print("Родилась корова!")

    def makeNoise(self):
        print(" ".join((self.name, "говорит муу")))


class Goat(Artiodactyl):
    def __init__(self, *args, **kwargs):
        super(Goat, self).__init__(*args, **kwargs)
        print("Родилась коза!")

    def makeNoise(self):
        print(" ".join((self.name, "говорит бее")))


class Sheep(Artiodactyl):
    def __init__(self, *args, **kwargs):
        super(Sheep, self).__init__(*args, **kwargs)
        print("Родилась овца!")

    def makeNoise(self):
        print(" ".join((self.name, "говорит мее")))


class Pig(Artiodactyl):
    def __init__(self, *args, **kwargs):
        super(Pig, self).__init__(*args, **kwargs)
        print("Родилась свинья!")

    def makeNoise(self):
        print(" ".join((self.name, "говорит хрю-хрю")))


class Duck(Birds):
    def __init__(self, *args, **kwargs):
        super(Duck, self).__init__(*args, **kwargs)
        print("Родилась утка!")

    def makeNoise(self):
        print(" ".join((self.name, "говорит кря-кря")))


class Chicken(Birds):
    def __init__(self, *args, **kwargs):
        super(Chicken, self).__init__(*args, **kwargs)
        print("Родилась курица!")

    def makeNoise(self):
        print(" ".join((self.name, "говорит ко-ко")))


class Goose(Birds):
    def __init__(self, *args, **kwargs):
        super(Goose, self).__init__(*args, **kwargs)
        print("Родился гусь!")

    def makeNoise(self):
        print(" ".join((self.name, "говорит га-га-га")))


if __name__ == "__main__":
    obj = Animal("Маша")
    obj.makeNoise()
    obj.eat()
    obj1 = Cow("Буренка")
    obj1.makeNoise()
    obj1.eat()
    obj2 = Goose("Гаврюша")
    obj2.makeNoise()
    obj2.eat()