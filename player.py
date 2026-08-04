import time
import random
from collections import Counter
from loot import (
    elite_crate_loot_pool_weights,
    elite_crate_loot_pool,
    RECYCLE_VALUES
)
from save import save

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
        scrap = random.randint(20, 60)
        self.scrap += scrap
        self.total_scrap_earned += scrap
        loot_count = random.randint(2,4)
        print("=====================\nOpening Elite Crate...\n=====================")
        time.sleep(1)
        print(f"+{scrap} Scrap")
        print("\nYou found:")
        for x in range(loot_count):
            item = random.choices(
                elite_crate_loot_pool,
                weights = elite_crate_loot_pool_weights,
            )[0]
            print(f"• {item}")
            self.inventory.append(item)
            if item == "M249":
                print(f"You are lucky today, you found: {item}!")
        self.elite_crates_opened += 1


    def show_inventory(self):
        print("\n===== INVENTORY =====")
        print(f"Scrap: {self.scrap}")

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

    def recycle(self):
        recycle = input("\nWhat item do you want to recycle?: ").lower()
        for item in self.inventory:
            if item.lower() == recycle:
                scrap = RECYCLE_VALUES[item]

                if scrap == 0:
                    print("\nYou cant recycle this item!")
                else:
                    self.scrap += scrap
                    self.total_scrap_earned += scrap
                    self.inventory.remove(item)
                    print(f"You recycled {item}!")
                    print(f"\nYou got {scrap} Scrap.")

                return

        print("Item not found in inventory, maybe you made a typo?")

    def bandit_camp(self):
        while True:
            print("\n===== BANDIT CAMP =====")

            print(f"Current scrap: {self.scrap}")
            print(f"\n1. Buy Medical Syringe (100 Scrap)")
            print(f"\n2. Exit")

            choice = input("\nWhat do you want to do?: ")
            if choice == "1":
                if self.scrap >= 100:
                    self.inventory.append("Medical Syringe")
                    self.scrap -= 100
                    print("\nSuccessfully purchased a Medical Syringe!")
                    print(f"\nCurrent scrap: {self.scrap}")
                    save(self)
                else:
                    print("You dont have enough scrap!")
            elif choice == "2":
                print("\nLeaving Bandit Camp...")
                break
            else:
                print("Invalid choice!")

