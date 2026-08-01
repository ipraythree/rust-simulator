import time
import random
from collections import Counter
from loot import (
    elite_crate_loot_pool_weights,
    elite_crate_loot_pool
)

class Player:
    def __init__(self):
        self.health = 100
        self.scrap = 0
        self.inventory = []
        self.scientists_killed = 0
        self.elite_crates_opened = 0
        self.deaths = 0
        self.total_scrap_earned = 0

    def open_elite_crate(self):
        item = random.choices(
            elite_crate_loot_pool,
            weights = elite_crate_loot_pool_weights,
            k=1
        )[0]
        print("Opening elite crate...")
        time.sleep(2)
        self.inventory.append(item)
        self.elite_crates_opened += 1
        if item == "M249":
            print(f"You are lucky today, you found: {item}!")
        else:
            print(f"You found {item}!")

    def show_inventory(self):
        print("\n===== INVENTORY =====")

        if len(self.inventory) == 0:
            print("Inventory is empty.")
        else:
            items = Counter(self.inventory)

            for item, amount in items.items():
                if amount == 1:
                    print(item)
                else:
                    print(f"{item} x{amount}")

    def heal(self):
        if "Medical Syringe" in self.inventory:
            self.health += 15
            if self.health > 100:
                self.health = 100
            self.inventory.remove("Medical Syringe")
            print(f"Medical Syringe used!\nCurrent Health: {self.health}")
        else:
            print("You dont have any medical syringes...")

    def show_statistics(self):
        print("\n===== STATISTICS =====")
        print(f"Scientists killed : {self.scientists_killed}")
        print(f"Elite crates opened : {self.elite_crates_opened}")
        print(f"Total scrap earned : {self.total_scrap_earned}")
        print(f"Deaths : {self.deaths}")
        print("======================")
