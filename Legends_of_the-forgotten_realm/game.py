#import functions from other game modules
from character import create_character
from world import enter_region, explore_region
from items import view_inventory, use_potion, equip_item, buy_item
from save_load import save_game

#display the game menu and handle the player's choices
def game_menu(player):
    while True:
     print("\n========== GAME MENU ==========")
     print("1. Explore Regions")
     print("2. View Inventory")
     print("3. Use Potion")
     print("4. Equip Weapon/Armor")
     print("5. Visit Shop")
     print("6. Save Game")
     print("7. Return to Main Menu")

     #get the player's choice and handle invalid input
     try:
      print("="*40)
      choice = int(input("Enter your choice: "))
     except ValueError:
        print("Please enter a valid number.")
        continue

     #explore regions and check whether the player is defeated
     if choice == 1:
        explore_region(player)
        if player["hp"] <= 0:
          print("\n========== GAME OVER ==========")
          print("Your adventure has ended.")
          break

     #display the player's inventory
     elif choice == 2:
        view_inventory(player)

     #allow the player to use a potion
     elif choice == 3:
        use_potion(player)

     #equip weapons or armor from the inventory
     elif choice == 4:
        equip_item(player)

     #visit the shop to purchase items
     elif choice == 5:
        buy_item(player)


     #save the current game progress
     elif choice == 6:
      save_game(player)

     #return to the main menu
     elif choice == 7:
        print("Returning to main menu...")
        break
     else:
      print("Invalid choice!")


#create a new character and initialize their game data
def new_game():
    name, character_class, stats = create_character()

    #store the character's information in a dictionary
    player ={"name":name,
             "class":character_class,
             "hp":stats["hp"],
             "attack":stats["attack"],
             "defense":stats["defense"],
             "mana":stats["mana"],
             "gold":stats["gold"],
             "exp":0,
             "level":1,
             "max_hp":stats["hp"],
             "inventory": [],
             "unlocked_region":1,
             "bosses_defeated": [],
             "skill":stats["skill"]

    

    }

    #display the newly created character's profile  
    print("\n" + "=" * 35)
    print("      CHARACTER PROFILE")
    print("=" * 35)
    print(f"Name: {name}")
    print(f"Class: {character_class}")
    print(f"HP: {player['hp']}")
    print(f"Attack: {player['attack']}")
    print(f"Defense: {player['defense']}")
    print(f"Mana: {player['mana']}")
    print(f"Gold: {player['gold']}")
    print(f"Skill: {player['skill']}")
    print(f"Level: {player['level']}")
 
    #start the game with the newly created character
    game_menu(player)