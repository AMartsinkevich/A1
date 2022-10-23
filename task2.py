#!/usr/bin/env python3

#Задача 2.
#Необходимо создать класс Animal, который имеет атрибуты Name (тип животного), Color (его расцветку) и Voice (издаваемый звук).
#Написать функцию, которая возвращает строку вида «It says <Voice>.», где <Voice> является уникальным атрибутом класса Animal.
#Задать три экземпляра класса Cow, Cat, Dog с уникальными атрибутами для каждого. Для каждого экземпляра вывести строку вида «<Name> is <Color>. It says <Voice>.»

print("\n")
print('#' * 80)
print("\n")
print("Aliaksandr Martsinkevich | 2022-10-21 | Stage 2 | Task 2 | Classes")
print("\n")
print('#' * 80)
print("\n")

print("Задача 2.")
print("Необходимо создать класс Animal, который имеет атрибуты Name (тип животного),")
print("Color (его расцветку) и Voice (издаваемый звук). Написать функцию, которая")
print("возвращает строку вида «It says <Voice>.», где <Voice> является уникальным")
print("атрибутом класса Animal. Задать три экземпляра класса Cow, Cat, Dog")
print("с уникальными атрибутами для каждого. Для каждого экземпляра вывести строку")
print("вида «<Name> is <Color>. It says <Voice>.»")

print("\n")
print('-' * 80)
print("\n")

class Animal:
    def __init__(self, Name, Color, Voice):
        self.Name = Name
        self.Color = Color
        self.Voice = Voice

    def __str__(self):
        return f"It says {self.Voice}."


def animal_say(animal):
    return f"{animal.Name} is {animal.Color}. {animal}"


def main():

    Cow = Animal("Cow", "Brown", "Moo")
    Cat = Animal("Cat", "Black", "Meow")
    Dog = Animal("Dog", "White", "Woof")

    print("Animals and the sounds they make:")

    print(animal_say(Cow))
    print(animal_say(Cat))
    print(animal_say(Dog))

    print("\n")

if __name__ == "__main__":
    main()