
from progression import level_up


#start a battle between the player and enemy
def start_battle(player, enemy):
    print(f"A wild {enemy['name']} appeared!")

    while player["hp"] > 0 and enemy["hp"] > 0:
        print("="*40)
        print("\n1. Normal Attack")
        print(f"2. {player['skill']} (20 Mana)")
        print("3. Defend")
        print("="*40)
        choice = input("Choose your action: ")

        #normal attack
        if choice == "1":
            damage = max(1, player["attack"] - enemy["defense"])
            enemy["hp"] = max(0, enemy["hp"] - damage)
            print(f"You dealt {damage} damage!")

        #special skill
        elif choice == "2":
            if player["mana"] >= 20:

                if player["class"] == "Warrior":
                    damage = player["attack"] * 2 - enemy["defense"]

                elif player["class"] == "Mage":
                    damage = player["attack"] * 2 - enemy["defense"]

                elif player["class"] == "Archer":
                    damage = player["attack"] * 2

                elif player["class"] == "Assassin":
                    damage = player["attack"] * 3

                damage = max(1, damage)

                enemy["hp"] = max(0, enemy["hp"] - damage)
                player["mana"] -= 20

                print(f"{player['skill']} dealt {damage} damage!")
                print("Mana remaining:", player["mana"])

            else:
                print("Not enough mana!")
                continue

        #defend against enemy attack
        elif choice == "3":
            print("You defended against the enemy's attack!")

            pdamage = max(0, enemy["attack"] - player["defense"])
            received_damage = pdamage // 2

            player["hp"] = max(0, player["hp"] - received_damage)

            print("Damage received:", received_damage)
            print("Your HP:", player["hp"])
            continue

        else:
            print("Invalid choice!")
            continue

        #enemy attacks if it is still alive
        if enemy["hp"] > 0:
            pdamage = max(1, enemy["attack"] - player["defense"])

            player["hp"] = max(0, player["hp"] - pdamage)

            print("Enemy attacked! Damage:", pdamage)
            print("Your HP:", player["hp"])

    #give rewards when the enemy is defeated
    if enemy["hp"] == 0:
        player["exp"] += enemy["exp_reward"]

        level_up(player)

        player["gold"] += enemy["gold_reward"]

        print(f"\nVictory! {enemy['name']} defeated!")
        print("EXP earned:", enemy["exp_reward"])
        print("Gold earned:", enemy["gold_reward"])
        print("Total EXP:", player["exp"])
        print("Total Gold:", player["gold"])

    #display game over when the player is defeated
    else:
        print("\nGame over, you died!")
