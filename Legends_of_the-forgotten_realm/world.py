#import random module to select enemies randomly
import random

#import battle function and enemy data
from battle import start_battle
from enemies import (
    goblin, slime, skeleton, orc, troll, demon,
    forest_boss, desert_boss, mountain_boss,
    ruins_boss, castle_boss, volcano_boss,
    ice_boss, sky_boss, demon_lord, demon_king
)


#handle region exploration and enemy encounters
def explore_region(player):

    #display the world map
    enter_region()

    #display the world map
    while True:
        try:
            choice = int(input("Choose a region (1-10) or 0 to return: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        #return to the main menu
        if choice == 0:
            print("Returning to main menu...")
            break

        #check whether the selected region is unlocked
        elif 1 <= choice <= player["unlocked_region"]:

            region = regions[choice - 1]
            print(f"\nYou entered: {region}")
            print("You begin exploring...")

            #define which enemies can appear in each region
            region_enemies = {
                1: [goblin, slime],
                2: [goblin, skeleton],
                3: [skeleton, orc],
                4: [orc, troll],
                5: [orc, troll],
                6: [troll, demon],
                7: [troll, demon],
                8: [orc, troll],
                9: [troll, demon],
                10: [demon]
            }

            #randomly select an enemy from the region
            enemy = random.choice(region_enemies[choice])

            #set the starting health of each enemy
            enemy_hp = {
                "Goblin": 50,
                "Slime": 35,
                "Skeleton": 65,
                "Orc": 90,
                "Troll": 120,
                "Demon": 180
            }

            #store the player's level before the battle
            enemy["hp"] = enemy_hp[enemy["name"]]
            previous_level = player["level"]

            #start the normal enemy battle
            start_battle(player, enemy)

            #connect each milestone level with its boss
            bosses = {
                10: forest_boss,
                20: desert_boss,
                30: mountain_boss,
                40: ruins_boss,
                50: castle_boss,
                60: volcano_boss,
                70: ice_boss,
                80: sky_boss,
                90: demon_lord,
                100: demon_king
            }

            #check whether the player is alive after the battle
            if player["hp"] > 0:
             
             #find the latest milestone level reached
             boss_level = (player["level"] // 10) * 10

             #check whether the player has reached a new boss level
             if previous_level < boss_level and boss_level in bosses:
                
                #check whether this boss has already been defeated
                if boss_level not in player["bosses_defeated"]:

                   #create a separate copy of the boss data
                    boss = bosses[boss_level].copy()

                    print("\nA powerful boss has appeared!")

                    #start the boss battle
                    start_battle(player, boss)

                    #record the boss defeat if the player wins
                    if boss["hp"] == 0 and player["hp"] > 0:
                     player["bosses_defeated"].append(boss_level)
                     print("Boss defeated! Your victory has been recorded!")

                     #display the victory message after defeating the final bos
                     if boss_level == 100:
                        print("\n" + "=" * 40)
                        print("       CONGRATULATIONS, HERO!")
                        print("   YOU HAVE SAVED THE REALM OF ELDORIA!")
                        print("=" * 40)
            #return after completing the region encounter
            break

        #display a message if the selected region is locked
        else:
            print(
                f"Region locked! You can access regions "
                f"1 to {player['unlocked_region']}."
            )

        
#define the ten regions of Eldoria
regions = [
    "The Forgotten Village",
    "Dark Forest",
    "Goblin Cave",
    "Burning Desert",
    "Ancient Ruins",
    "Dark Castle",
    "Volcano",
    "Frozen Mountain",
    "Sky Temple",
    "Demon Realm"
]

#display the world map and available regions
def enter_region():
    print("\n" + "=" * 40)
    print("       WORLD OF ELDORIA")
    print("=" * 40)

    #display all regions with their numbers
    for number, region in enumerate(regions, start=1):
        print(f"{number}. {region}")

    print("=" * 40)
