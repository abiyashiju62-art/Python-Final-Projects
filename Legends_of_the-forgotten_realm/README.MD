# Legends of the Forgotten Realm

A text-based fantasy RPG developed using Python. The player explores the world of Eldoria, fights enemies, collects rewards, levels up, purchases equipment, and battles powerful bosses to save the realm.

## About the Game

The kingdom of Eldoria has fallen into darkness. Powerful creatures roam the land, and an ancient evil threatens to destroy the realm.

Choose your hero, explore dangerous regions, improve your abilities, and defeat powerful bosses to restore peace.

## Character Classes

The game offers four character classes:

- **Warrior** – High health and defense.
- **Mage** – Powerful magic and mana.
- **Archer** – Balanced attack and accuracy.
- **Assassin** – High critical damage and speed.

Each class has its own stats and special skill.

## Features

- Character creation with four playable classes
- Turn-based combat system
- Normal attacks, special skills, and defense
- Mana system for special abilities
- Enemy encounters
- Ten explorable regions
- Boss battles at milestone levels
- Experience points and level progression
- Unlockable regions
- Weapons and armor equipment
- 20 weapons
- 12 armor types
- 15 potion types
- Item shop and gold system
- Inventory management
- Health and mana potions
- Save and load functionality using JSON
- Final boss and victory ending

## Game Controls

The game is controlled through the terminal by entering numbers corresponding to the displayed menu options.

### Main Menu

1. New Game
2. Continue
3. Instructions
4. Exit

### Game Menu

1. Explore Regions
2. View Inventory
3. Use Potion
4. Equip Weapon/Armor
5. Visit Shop
6. Save Game
7. Return to Main Menu

## How to Run

1. Install Python.
2. Download or clone this repository.
3. Open the project folder in a terminal.
4. Run the following command:

```bash
python main.py
```

## Project Structure

```text
Legends_of_the_Forgotten_Realm/
│
├── main.py
├── menu.py
├── game.py
├── character.py
├── battle.py
├── enemies.py
├── progression.py
├── world.py
├── items.py
├── save_load.py
└── README.md
```

## Technologies Used

- Python
- Dictionaries
- Lists
- Functions
- Loops and conditional statements
- Exception handling
- Modules and imports
- Random module
- JSON file handling

## Save System

The player's progress can be saved and loaded using a JSON file named `savegame.json`, which is created when the player saves the game.

## Objective

Explore all ten regions, become stronger through battles and level progression, defeat the bosses, and defeat the Ancient Demon King to save Eldoria.

---

**Project:** Legends of the Forgotten Realm  
**Language:** Python  
**Type:** Text-Based RPG  
