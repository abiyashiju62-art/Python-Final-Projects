
#store the starting statistics and special skills for each character class
character_stats = {
    "Warrior": {"hp": 150, "attack": 15, "defense": 15, "mana": 30, "gold": 100,"skill":"Power Strike"},
    "Mage": {"hp": 90, "attack": 25, "defense": 5, "mana": 100, "gold": 100,"skill":"Fireball"},
    "Archer": {"hp": 110, "attack": 20, "defense": 8, "mana": 50, "gold": 100,"skill":"Piercing arrow"},
    "Assassin": {"hp": 100, "attack": 22, "defense": 6, "mana": 40, "gold": 100,"skill":"Shadow Strike"}
}

#ask the player for a name and character class
def create_character():
    #get a character name and make sure it is not empty
    while True:
     name = input("Enter your character name: ").strip()
     if not name:
        print("Name cannot be empty")
     else:
      break

    #display the available character classes
    print("="*40)
    print("1.Warrior - High health and defense.")
    print("2.Mage - Powerful magic and mana.")
    print("3.Archer - Balanced attack and accuracy")
    print("4.Assassin - High critical damage and speed")

    #get the player's class choice
    while True:
       try:
        print("="*40)
        choice = int(input("Enter your choice for class: "))
       except ValueError:
         print("Enter a valid number")
         continue

       #assign the selected character class
       if choice == 1:
         character_class = "Warrior"
         break
       elif choice == 2:
        character_class = "Mage"
        break
       elif choice == 3:
         character_class ="Archer"
         break
       elif choice == 4:
        character_class = "Assassin"
        break
       else:
         print("Invaild choice! Please entre a number between 1" )

    #get the starting statistics of the selected class
    stats = character_stats[character_class]
    #return the character's name, class and statistics
    return(name,character_class,stats)

