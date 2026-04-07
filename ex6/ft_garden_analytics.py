#!/usr/bin/env python3
class Plant:
    class _Stats:
        def __init__(self):
            self.grow_count = 0
            self.age_count = 0
            self.show_count = 0
            self.shade_count = 0

    def __init__(self, name, height, age):
        self.name = name
        self._height = height
        self._age = age
        self.stats = self._Stats()

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
            self.stats.age_count += 1

    def grow(self, meter):
        self._height += meter
        self.stats.grow_count += 1

    def age_plant(self):
        self._age += 20
        self.stats.age_count += 1

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
        self.stats.show_count += 1

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
        self.stats.shade_count += 1

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.trunk}cm")
        self.stats.show_count += 1


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


def display_stats(plant):
    print(f"Stats: {plant.stats.grow_count} grow,\
 {plant.stats.age_count} age, {plant.stats.show_count} show")
    if isinstance(plant, Tree):
        print(f"{plant.stats.shade_count} shade")


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
    display_stats(rose)

    print("[asking the rose to grow and bloom]")
    rose.grow(8.0)
    rose.show()
    rose.bloom()
    print("[statistics for Rose]")
    display_stats(rose)

    print("\n=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print("[statistics for Oak]")
    display_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    display_stats(oak)

    print("\n=== Seed")
    seed = Seed("Sunflower", 80.0, 45, "yellow")
    seed.show()
    seed.bloom()
    print("[make sunflower grow, age and bloom]")
    seed.grow(30.0)
    seed.seed()
    seed.age_plant()
    seed.show()
    seed.bloom()
    print("[statistics for Sunflower]")
    display_stats(seed)
