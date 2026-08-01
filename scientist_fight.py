import time
import random
from loot import scientist_loot_pool
from save import save

def scientist_fight(player, scientist):
    print("You encountered a scientist!")
    time.sleep(1)
    while scientist.health > 0 and player.health > 0:

        player_damage = random.randint(15, 35)
        scientist_damage = random.randint(10, 25)

        scientist.health -= player_damage

        print(f"You hit him for {player_damage} damage! ")
        if scientist.health < 0:
            scientist.health = 0
        time.sleep(1)
        print(f"Scientist remaining health: {scientist.health}")
        time.sleep(1)

        if scientist.health <= 0:
            print("Scientist is dead!")
            time.sleep(1)
            print("Searching body...")
            scientist_loot = random.choice(scientist_loot_pool)
            scrap = random.randint(1, 5)
            print(f"Found:\n-{scientist_loot}\n-{scrap} Scrap")
            player.scientists_killed += 1
            player.total_scrap_earned += scrap
            player.scrap += scrap
            time.sleep(1)
            player.inventory.append(scientist_loot)
            print(f"Your remaining health: {player.health}")
            time.sleep(1)
            scientist.health = 100
            save(player)
            break

        player.health -= scientist_damage

        print(f"Scientist hit you for {scientist_damage} damage!")
        if player.health < 0:
            player.health = 0
        time.sleep(1)
        print(f"Your remaining health: {player.health}")
        time.sleep(1)

        if player.health <= 0:
            print("You died!")
            player.deaths += 1
            player.inventory.clear()
            player.health = 100
            save(player)
            break