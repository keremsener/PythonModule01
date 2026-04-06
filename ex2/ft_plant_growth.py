#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {round(self.height, 1)}cm, {self.age} days old")

    def grow(self):
        self.height += 0.8

    def age_plant(self):
        self.age += 1


if __name__ == "__main__":
    i = 1
    rose = Plant("Rose", 25.0, 30)
    print("=== Garden Plant Growth ===")
    while i <= 7:
        print(f"=== Day {i} ===")
        rose.show()
        rose.grow()
        rose.age_plant()
        i += 1
    print("Growth this week: 6cm")
