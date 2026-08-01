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
    print("7. Exit")

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
        print("Saving...")
        save(player)
        print("Goodbye!")
        break

    else:
        print("Invalid choice.\n")

# bu projede ilk defa py dosyalarini ayirdin ve tek dosyaya 300 satir yazmaktan kurtuldun
# class kullanmayi ilk defa bugun ogrendin ve onu bundan onceki projede ilk defa kullandin
# bu rust simulator v1in devami olan rust simulator v2 ikisini de bugun yazdin
# suan arkada bu notu yazarken calan sarki black sabbath - war pigs
# saat 12:14 AM tarih 8/2/2026 yani 2 agustos 2026
# asla pes etme bi gun cok istedigin almanyadaki universiteyi kazanicaksin ve mezun olucaksin
# umarim bu dosyayi acacak kadar yol katetmissindir ve bunlari okurken gulumsuyodundur :)
# (arkada anlik olarak war pigsten sonra calan ve gojiranin en sevdigin (sevdigim mi artik kendime not dusmek kafa karistirici aq ) gojira - amazonia caliyo)
# hadi ben bunu githuba repo atmaya gidiyom ilerde belki sirkete seni alirlarsa almani saglayan sey 16 yasinda emek edip calisman ve bugun bu repolari biriktirmen henuz 16 yasindan