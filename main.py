from player import Player
from save import (
    save,
    load
)
from scientist import Scientist
from scientist_fight import scientist_fight

scientist = Scientist()
player = Player()

load(player)

while True:

    print("====== RUST SIMULATOR ======")
    print("1. Open Elite Crate")
    print("2. Show Inventory")
    print("3. Fight Scientist")
    print("4. Use Medical Syringe")
    print("5. Show Current Health")
    print("6. Show Statistics")
    print("7. Recycler")
    print("8. Bandit Camp")
    print("9. Exit")

    choice = input("Choose: ")

    if choice == "1":
        player.open_elite_crate()
        save(player)

    elif choice == "2":
        player.show_inventory()

    elif choice == "3":
        scientist_fight(player, scientist)

    elif choice == "4":
        player.heal()
        save(player)

    elif choice == "5":
        print(f"Current health: {player.health}")

    elif choice == "6":
        player.show_statistics()

    elif choice == "7":
        player.show_inventory()
        player.recycle()
        save(player)

    elif choice == "8":
        player.bandit_camp()
        save(player)

    elif choice == "9":
        print("Saving...")
        save(player)
        print("Goodbye!")
        break



    else:
        print("Invalid choice.\n")
