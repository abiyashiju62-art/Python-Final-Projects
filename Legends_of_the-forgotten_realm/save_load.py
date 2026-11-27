#import json module to store and retrieve game data
import json

#save the player's progress to a json file
def save_game(player):

    #open the save file in write mode
    with open("savegame.json", "w") as file:

        #convert player data into json format and save it
        json.dump(player, file, indent=4)

    print("Game saved successfully!")

#load the player's saved progress from a json file
def load_game():
    try:

        #open the save file in read mode
        with open("savegame.json", "r") as file:

            #convert json data back into python data
            player = json.load(file)

        print("Game loaded successfully!")
        return player

    #handle the situation when no save file exists
    except FileNotFoundError:
        print("No saved game found!")
        return None