#!/usr/bin/env python3
class Plant:
    class Status:
        grow_count = 0
        age_count = 0
        show_count = 0

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
            Plant.Status.age_count += 1

    def grow(self):
        self._height += 2.1
        Plant.Status.grow_count += 1

    def age_plant(self):
        self._age += 1

    def show(self):
        print(f"{self.name}: {round(self._height, 1)}cm, \
{self._age} days old")

    def status(self):
        print(f"Stats: {Plant.Status.grow_count} grow,\
 {Plant.Status.age_count} age, {Plant.Status.show_count} show")


class Flower(Plant):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.has_bloomed = False

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        Plant.Status.show_count += 1

    def bloom(self):
        if not self.has_bloomed:
            print(f"{self.name} has not bloomed yet")
            self.has_bloomed = True
        else:
            print(f"{self.name} is blooming beautifully!")

    def status(self):
        super().status()


class Tree(Flower):
    def __init__(self, name, height, age, color):
        super().__init__(name, height, age)
        self.color = color
        self.has_bloomed = False

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        Plant.Status.show_count += 1

    def bloom(self):
        if not self.has_bloomed:
            print(f"{self.name} has not bloomed yet")
            self.has_bloomed = True
        else:
            print(f"{self.name} is blooming beautifully!")

    def status(self):
        super().status()



if __name__ == "__main__":
    print("=== Garden statistics ===")
    # print("=== Check year-old")

    print("=== Flower")
    rose = Flower("Rose", 15.0, 10, "red")
    rose.show()
    rose.bloom()
    print("[statistics for Rose]")
    rose.status()

    print("\n=== Tree")
