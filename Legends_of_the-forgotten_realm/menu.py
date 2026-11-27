#import functions required for starting and continuing the game
from game import new_game
from save_load import load_game
from game import game_menu

#display the game title and introduction
def display_title():
    print("="*40)
    print("LEGENDS OF THE FORGOTTEN REALM".center(40))
    print("="*40)
    print("The kingdom of Eldoria has fallen into darkness".center(40))
    print("A hero must rise to save the realm.".center(40))

#display the main menu options
def display_menu():
    print("="*40)
    print("1. New Game")
    print("2. Continue")
    print("3. Instructions")
    print("4. Exit")
    print("=" * 40)

#handle the main menu and its different options
def main_menu():
    display_title()
    while True:
        display_menu()

        #get the user's menu choice and handle invalid input
        try:
         choice = int(input("Enter your choice: "))
        except ValueError:
            print("please enter a valid number")
            continue
        if choice == 1:
            new_game()

        #load a previously saved game
        elif choice == 2:
            player = load_game()
            if player:
             game_menu(player)

        #display the game instructions
        elif choice == 3:
            instructions()

        #exit the game
        elif choice == 4:
            print("\nThank you for playing Legends of the Forgotten Realm!")
            print("Goodbye, hero!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 4")


#display the story, rules and instructions of the game
def instructions():
    print("="*40)
    print("THE CHRONICLES OF ELDORIA".center(40))
    print()
    print("An ancient guide for those who dare to enter the Forgotten Realm".center(40)) 
    print("="*40)

    #introduce the story behind the game
    print("\nLong ago,the kingdom of Eldoria flourished in peace." \
    "But darkness has awakened, powerful creatures roam the land and " \
    "an ancient evil threatens to consume the realm.")

    #explain the available character classes
    print("\n1.Choose Your Destiny")
    print("\nFour heroes stand ready to answer the call: " \
    "the mighty Warrior, the mystical Mage, the skilled Archer and the deadly Assassin. " \
    "Each follows a different path with unique abilities\n")
    print("-"*40)

    #explain exploration and the journey
    print("\n2.The Journey Begins")
    print("\nExplore dangerous regions, encounter mysterious creatures and " \
    "face increasingly powerful enemies.\n")
    print("-"*40)

    #explain combat, rewards and character progression
    print("\n3.The Art Of Battle")
    print("\nEvery victory brings experience and gold. Grow stronger, level up, "
    "discover weapons and armor, and improve your abilities.\n"
    "Every battle is turn-based. Choose your attacks wisely, unleash "
    "special skills, defend yourself and use potions to survive.\n")
    print("-"*40)

    #explain the bosses and final challenge
    print("\n4.Your Final Destiny")
    print("\nTen powerful bosses stand between you and victory. " \
    "Your ultimate challenge awaits in the Demon Realm: the Ancient Demon King.\n")
    print("Will you become the hero who saves Eldoria or will darkness claim the realm?".center(70))
    print("="*40)
    print("YOUR LEGEND BEGINS HERE...".center(40))

    #wait for the player to return to the main menu
    print("="*40)
    input("Press Enter to return to the main menu...")


