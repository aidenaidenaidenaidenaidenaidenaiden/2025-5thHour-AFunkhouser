import random
import sys

class Player:
    def __init__(self):
        self.health = 100
        self.max_health = 100
        self.inventory = {
            "Wood": 0,
            "Stone": 0,
            "Iron": 0,
            "Wooden Pickaxe": 0,
            "Stone Pickaxe": 0,
            "Iron Pickaxe": 0,
        }
        self.location = "Plains"

    def show_status(self):
        print(f"\nHealth: {self.health}/{self.max_health}")
        print(f"Location: {self.location}")
        self.show_inventory()

    def show_inventory(self):
        print("\nInventory:")
        for item, qty in self.inventory.items():
            if qty > 0:
                print(f" - {item}:
