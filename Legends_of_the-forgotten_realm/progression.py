#handle player level progression
def level_up(player):

    #check if the player has enough experience to level up
    while player["exp"] >= player["level"] * 100:
        player["level"] += 1

        #increase player stats after leveling up
        player["max_hp"] += 20
        player["hp"] = min(player["hp"] + 20, player["max_hp"])
        player["attack"] += 2

        #unlock a new region every 10 levels
        if player["level"] % 10 == 0:
            player["unlocked_region"] = min(
                10, player["unlocked_region"] + 1
            )
            print(f"New region unlocked: Region {player['unlocked_region']}!")
            
        #unlock a new region every 10 levels
        print(f"Congratulations! You reached Level {player['level']}!")
        print("New HP:", player["hp"])
        print("New Max HP:", player["max_hp"])
        print("New Attack:", player["attack"])

