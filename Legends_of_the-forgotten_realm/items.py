
#store all available weapons with their attack bonus and price
weapons = {
    "Iron Sword": {"attack": 5, "price": 50},
    "Steel Sword": {"attack": 10, "price": 100},
    "Magic Staff": {"attack": 12, "price": 120},
    "Hunter Bow": {"attack": 8, "price": 80},
    "Shadow Dagger": {"attack": 15, "price": 150},
    "Flame Sword": {"attack": 18, "price": 200},
    "Ice Blade": {"attack": 16, "price": 180},
    "Thunder Hammer": {"attack": 22, "price": 250},
    "Golden Sword": {"attack": 20, "price": 230},
    "Dragon Slayer": {"attack": 30, "price": 400},
    "Crystal Staff": {"attack": 17, "price": 220},
    "Elven Bow": {"attack": 19, "price": 240},
    "Poison Dagger": {"attack": 21, "price": 260},
    "Battle Axe": {"attack": 24, "price": 280},
    "Silver Spear": {"attack": 14, "price": 160},
    "Demon Blade": {"attack": 35, "price": 500},
    "Royal Sword": {"attack": 26, "price": 350},
    "Phoenix Bow": {"attack": 28, "price": 380},
    "Ancient Staff": {"attack": 32, "price": 450},
    "Legendary Katana": {"attack": 40, "price": 600}
}


#store all available armor with their defense bonus and price
armors = {
    "Leather Armor": {"defense": 3, "price": 40},
    "Iron Armor": {"defense": 6, "price": 80},
    "Steel Armor": {"defense": 10, "price": 120},
    "Magic Robe": {"defense": 5, "price": 100},
    "Shadow Armor": {"defense": 12, "price": 150},
    "Golden Armor": {"defense": 14, "price": 180},
    "Dragon Armor": {"defense": 20, "price": 350},
    "Crystal Armor": {"defense": 16, "price": 250},
    "Silver Armor": {"defense": 8, "price": 110},
    "Phoenix Robe": {"defense": 18, "price": 300},
    "Royal Armor": {"defense": 22, "price": 400},
    "Demon Armor": {"defense": 25, "price": 500}
}


#store all available potions with their effects and price
potions = {
    "Small Health Potion": {"heal": 30, "price": 20},
    "Health Potion": {"heal": 60, "price": 40},
    "Large Health Potion": {"heal": 100, "price": 70},
    "Mana Potion": {"mana": 30, "price": 25},
    "Large Mana Potion": {"mana": 60, "price": 50},
    "Greater Health Potion": {"heal": 150, "price": 100},
    "Small Mana Potion": {"mana": 15, "price": 15},
    "Greater Mana Potion": {"mana": 100, "price": 90},
    "Elixir of Life": {"heal": 200, "price": 150},
    "Elixir of Magic": {"mana": 150, "price": 130},
    "Minor Healing Potion": {"heal": 20, "price": 15},
    "Minor Mana Elixir": {"mana": 20, "price": 20},
    "Supreme Health Potion": {"heal": 300, "price": 200},
    "Supreme Mana Potion": {"mana": 200, "price": 180},
    "Ancient Elixir": {"heal": 250, "price": 250}
}


#display all items in the player's inventory
def view_inventory(player):
    print("\n" + "=" * 40)
    print("             INVENTORY")
    print("=" * 40)

    #check whether the inventory is empty
    if not player["inventory"]:
        print("Your inventory is empty.")
    else:

        #display each item in the inventory
        for item in player["inventory"]:
            print("-", item)

    print("=" * 40)


#allow the player to use health or mana potions
def use_potion(player):

    #get only the potions available in the inventory
    available_potions = [
        item for item in player["inventory"]
        if item in potions
    ]

    #check whether the player has any potions
    if not available_potions:
        print("You don't have any potions!")
        return

    #display available potions
    print("\nAvailable Potions:")
    for number, potion in enumerate(available_potions, start=1):
        print(f"{number}. {potion}")

    #get and validate the potion choice
    try:
        choice = int(input("Choose a potion: "))

        if choice < 1 or choice > len(available_potions):
            print("Invalid choice.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    #get the selected potion and its details
    selected = available_potions[choice - 1]
    details = potions[selected]
    
    # Check whether healing is needed
    if "heal" in details and player["hp"] >= player["max_hp"]:
        print("Your HP is already full! Potion not used.")
        return

    #check whether mana needs to be restored
    if "mana" in details and player["mana"] >= 100:
        print("Your mana is already full! Potion not used.")
        return

    #restore health if the selected potion is a health potion
    if "heal" in details:
        old_hp = player["hp"]
        player["hp"] = min(
            player["hp"] + details["heal"],
            player["max_hp"]
        )
        print(f"You restored {player['hp'] - old_hp} HP!")

    #restore mana if the selected potion is a mana potion
    if "mana" in details:
        player["mana"] += details["mana"]
        print(f"You restored {details['mana']} mana!")

    #remove the used potion from the inventory
    player["inventory"].remove(selected)
    print(f"{selected} used successfully!")


#allow the player to equip weapons or armor
def equip_item(player):

    #get only weapons and armor from the inventory
    available_items = [
        item for item in player["inventory"]
        if item in weapons or item in armors
    ]

    #check whether the player has any equipment
    if not available_items:
        print("You don't have any weapons or armor!")
        return

    #display available equipment
    print("\nAvailable Equipment:")

    for number, item in enumerate(available_items, start=1):
        print(f"{number}. {item}")

    #get and validate the equipment choice
    try:
        choice = int(input("Choose equipment: "))

        if choice < 1 or choice > len(available_items):
            print("Invalid choice.")
            return

    except ValueError:
        print("Please enter a valid number.")
        return

    #get the selected equipment
    selected = available_items[choice - 1]

    #increase attack when a weapon is equipped
    if selected in weapons:
        player["attack"] += weapons[selected]["attack"]
        print(f"You equipped {selected}!")
        player["inventory"].remove(selected)

    #increase defense when armor is equipped
    elif selected in armors:
        player["defense"] += armors[selected]["defense"]
        print(f"You equipped {selected}!")
        player["inventory"].remove(selected)


#allow the player to purchase items from the shop
def buy_item(player):
    print("\n===== ITEM SHOP =====")

    #combine weapons, armor and potions into one shop collection
    all_items = {**weapons, **armors, **potions}
    item_list = list(all_items.keys())

    #display all available items and their prices
    for number, item in enumerate(item_list, start=1):
        print(f"{number}. {item} - {all_items[item]['price']} Gold")

    print("0. Exit Shop")

    #get the player's purchase choice
    try:
        choice = int(input("Choose an item to buy: "))

    except ValueError:
        print("Please enter a valid number.")
        return

    #exit the shop
    if choice == 0:
        return

    #check whether the selected item number is valid
    if choice < 1 or choice > len(item_list):
        print("Invalid choice.")
        return

    #get the selected item and its price
    selected = item_list[choice - 1]
    price = all_items[selected]["price"]

    #check whether the player has enough gold
    if player["gold"] < price:
        print("Not enough gold!")
        return

    #deduct gold and add the purchased item to inventory
    player["gold"] -= price
    player["inventory"].append(selected)

    print(f"You bought {selected}!")
    print("Remaining Gold:", player["gold"])
