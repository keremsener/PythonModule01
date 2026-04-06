#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = height
        self._age = age

    def get_height(self):
        return self._height

    def set_height(self, value):
        if value < 0:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            self._height = value
            print(f"Height updated: {value}cm")

    def set_age(self, value):
        if value < 0:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            self._age = value
            print(f"Age updated: {value} days")

    def grow(self):
        self._height += 2.1

    def age_plant(self):
        self._age += 1

    def show(self):
        print(f"{self.name}: {round(self._height, 1)}cm, \
{self._age} days old")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.has_bloomed = False

    def show(self):
        super().show()
        print(f"Color: {self.color}")

    def bloom(self):
        if not self.has_bloomed:
            print(f"{self.name} has not bloomed yet")
            self.has_bloomed = True
        else:
            print(f"{self.name} is blooming beautifully!")      


class Tree(Plant):
    def __init__(self, name, height, age, trunk):
        super().__init__(name, height, age)
        self.trunk = trunk

    def produce_shade(self):
        print(f"Tree {self.name} now produces a shade of {self._height}cm long\
 and {self.trunk}cm wide.")

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk}cm")


class Vegetable(Plant):
    def __init__(self, name, height, age, harvest_season, nutritional_value):
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show(self):
        super().show()
        print(f"Harvest season: {self.harvest_season}")
        print(f"Nutritional value: {self.nutritional_value}")

    def grow(self):
        super().grow()

    def age_plant(self):
        super().age_plant()
        self.nutritional_value += 1


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("=== Vegetable")
    tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        tomato.grow()
        tomato.age_plant()
    tomato.show()
