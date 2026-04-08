#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self._height = height
        self._age = age

    def get_height(self):
        return self._height

    def get_age(self):
        return self._age

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


if __name__ == "__main__":
    rose = Plant("Rose", 15.0, 10)
    print("=== Garden Security System ===")

    print(f"Plant created: {rose.name}: {rose.get_height()}cm,\
 {rose.get_age()} days old")

    rose.set_height(25.0)
    rose.set_age(30)
    print("\n")
    rose.set_height(-5)
    rose.set_age(-5)
    print(f"Current state: {rose.name}: {rose.get_height()}cm,\
 {rose.get_age()} days old")
