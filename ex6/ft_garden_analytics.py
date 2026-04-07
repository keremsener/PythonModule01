#!/usr/bin/env python3
class Plant:

    def __init__(self, name, height, age):
        self.name = name
        self._height = height
        self._age = age
        self.grow_count = 0
        self.age_count = 0
        self.show_count = 0
    
    @staticmethod
    def is_old_than_a_year(age):
        if age > 365:
            print(f"Is {age} days more than a year ? -> True")
        else:
            print(f"Is {age} days more than a year ? -> False")

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
            self.age_count += 1

    def grow(self, meter):
        self._height += meter
        self.grow_count += 1

    def age_plant(self):
        self._age += 20
        self.age_count += 1

    def show(self):
        print(f"{self.name}: {round(self._height, 1)}cm, \
{self._age} days old")

    def status(self):
        print(f"Stats: {self.grow_count} grow,\
 {self.age_count} age, {self.show_count} show")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.has_bloomed = False

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        self.show_count += 1

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
        self.shade_count = 0

    def produce_shade(self):
        print(f"Tree {self.name} now produces a shade of {self._height}cm long\
 and {self.trunk}cm wide.")
        self.shade_count += 1

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk}cm")
        self.show_count += 1

    def status(self):
        super().status()
        print(f"{self.shade_count} shade")


class Seed(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age, color)
        self.seed_count = 0

    def seed(self):
        self.seed_count += 42

    def show(self):
        super().show()
        if not self.has_bloomed:
            print(f"{self.name} has not bloomed yet")
        else:
            print(f"{self.name} is blooming beautifully!")
        print(f"Seeds: {self.seed_count}")

    def bloom(self):
        if not self.has_bloomed:
            self.has_bloomed = True


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    Plant.is_old_than_a_year(30)
    Plant.is_old_than_a_year(400)

    print("\n=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.bloom()
    print("[statistics for Rose]")
    rose.status()

    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.show()
    rose.bloom()
    print("[statistics for Rose]")
    rose.status()

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    oak.status()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    oak.status()

    print("\n=== Seed")
    seed = Seed("Sunflower", 80.0, 45)
    seed.show()
    seed.bloom()
    print("[make sunflower grow, age and bloom]")
    seed.grow(30.0)
    seed.seed()
    seed.age_plant()
    seed.show()
    seed.bloom()
    print("[statistics for Sunflower]")
    seed.status()
