import json

def save(player):
    data = {
        "health": player.health,
        "scrap": player.scrap,
        "inventory": player.inventory,
        "scientists_killed": player.scientists_killed,
        "elite_crates_opened": player.elite_crates_opened,
        "deaths": player.deaths,
        "total_scrap_earned": player.total_scrap_earned,
    }

    with open("character.json", "w") as outfile:
        json.dump(data, outfile, indent=4)


def load(player):
    try:
        with open("character.json", "r") as outfile:
            data = json.load(outfile)

        player.health = data["health"]
        player.scrap = data["scrap"]
        player.inventory = data["inventory"]
        player.scientists_killed = data.get("scientists_killed", 0)
        player.elite_crates_opened = data.get("elite_crates_opened", 0)
        player.deaths = data.get("deaths", 0)
        player.total_scrap_earned = data.get("total_scrap_earned", 0)

    except FileNotFoundError:
        print("No save file found, creating a new one...")