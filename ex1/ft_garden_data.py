#!/usr/bin/env python3

class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f"{self.name}: {self.height}, {self.age}")
    

if __name__ == "__main__":
    rose = Plant("Rose", "25cm", "30 days old")
    sunflower = Plant("Sunflower", "80cm", "45 days old")
    cactus = Plant("Cactus", "15cm", "120 days old")
    print("=== Garden Plant Registry ===")
    rose.show()
    sunflower.show()
    cactus.show()
