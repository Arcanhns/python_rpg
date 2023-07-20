import random
import os
import time
from termcolor import colored

# PLAYER CLASSE ------------------------------------------------------

class Player():

    def __init__(self):

        self.name = "PLAYER"
        self.hp = 35
        self.max_hp = 35
        self.atk = 1
        self.dfs = 1
        self.lvl = 1
        self.exp = 0
        self.req_exp = required_exp
        self.location = "UNKNOWN"
        self.weapon = fists
        self.armor = leather_armor
        self.jcoins = 0

# ENEMY CLASS ------------------------------------------------------

class Enemy():

    def __init__(self):

        self.name = "bob"
        self.hp = 20
        self.max_hp = 20
        self.atk = 1
        self.dfs = 1
        self.lvl = 1

# WEAPON CLASS ------------------------------------------------------

class Weapon():
    
    def __init__(self, name, atk, dfs, required_lvl, price):

        self.name = name
        self.atk = atk
        self.dfs = dfs
        self.required_lvl = required_lvl
        self.price = price
        self.ow = True
    
# WEAPONS

fists = Weapon("FISTS", 1, -4, 1, 0)
fists.ow = True
small_dagger = Weapon("SMALL DAGGER", 3, -3, 1, 45)
small_dagger.ow = False
iron_sword = Weapon("IRON SWORD", 5, -2, 3, 75)
iron_sword.ow = False
wooden_bow = Weapon("WOODEN BOW", 2, 3, 3, 110)
wooden_bow.ow = False

# ARMOR CLASS ------------------------------------------------------

class Armor():
    
    def __init__(self, name, hp, dfs, required_lvl, price):

        self.name = name
        self.hp = hp
        self.dfs = dfs
        self.required_lvl = required_lvl
        self.price = price
        self.ow = True

# ARMOR ------------------------------------------------------

leather_armor = Armor("LEATHER ARMOR", 2, 2, 1, 0,)
leather_armor.ow = True
iron_armor = Armor("IRON ARMOR", 2, 5, 3, 50)
iron_armor.ow = False
maid_outfit = Armor("MAID OUTFIT", 69, 69, 420, 1337)
maid_outfit.ow = False

# CONSUMABLE CLASS ------------------------------------------------------

class Consumable():
    
    def __init__(self, name, hp, price, stock):

        self.name = name
        self.hp = hp
        self.price = price
        self.stock = stock
        self.ow = False

# CONSUMABLE ------------------------------------------------------

small_pot = Consumable("SMALL POT.", 25, 35, 2)
small_pot.ow = True
elixir = Consumable("ELIXIR", 50, 60, 0)
elixir.ow = False

# PLAYER FUNCTIONS ------------------------------------------------

def display_player():

    player_stats_checker()

    print("------------------------------------------")
    print(colored(player.name.center(42), "yellow"))
    print(colored(player.location.center(42), "yellow"))
    print("------------------------------------------")
    print("HP:", player.hp)
    print(f"MAX HP: {updated_hp} ({player.armor.hp})")
    print("LVL:", player.lvl)
    print("EXP:", player.exp)
    print("REQUIRED EXP:", required_exp)
    print(f"ATTACK: {updated_atk} ({player.weapon.atk})")
    print(f"DEFENSE: {updated_dfs} ({player.weapon.dfs}) ({player.armor.dfs})")
    print("------------------------------------------")
    print("WEAPON:", player.weapon.name)
    print("ARMOR:", player.armor.name)
    print("------------------------------------------")
    print("JCOINS:", player.jcoins)
    print("------------------------------------------")

def player_stats_checker():

    if player.lvl <= 9:
        player.location = "STARTER CITY"
    elif player.lvl >= 10:
        player.location = "SECOND CITY"
    elif player.lvl >= 16:
        player.location = "THIRD CITY"

    global updated_hp
    global updated_atk
    global updated_dfs

    updated_hp = player.max_hp + player.armor.hp
    updated_atk = max(1,player.atk + player.weapon.atk)
    updated_dfs = max(0,player.dfs + (player.weapon.dfs + player.armor.dfs))

def level_up():

    global required_exp

    op_lvl = player.lvl
    op_hp = player.hp
    op_max_hp = player.max_hp
    op_require_exp = player.req_exp
    op_atk = player.atk
    op_dfs = player.dfs
    
    current_required_exp = required_exp
    required_exp = int(required_exp * 1.5)

    player.lvl += 1
    player.max_hp = int(player.max_hp + random.randint(1,4))
    player.exp -= current_required_exp # resets player exp
    player.atk = int(player.atk + random.randint(1,3))
    player.dfs = int(player.dfs + random.randint(1,3))

    print("------------------------------------------")
    print("                LEVEL UP")
    print("------------------------------------------")
    print("NAME:", player.name)
    print("HP:", op_hp, ">", player.hp)
    print("MAX HP:", op_max_hp, ">", player.max_hp)
    print("LVL:", op_lvl , ">", player.lvl)
    print("REQUIRED EXP:", op_require_exp , ">" , required_exp)
    print("ATTACK:", op_atk, ">", player.atk)
    print("DEFENSE:", op_dfs, ">", player.dfs)
    print("------------------------------------------")

def money_gain_system():
    jcoins_earned = 0
    jcoins_earned += random.randint(10,30) + enemy.lvl
    player.jcoins += jcoins_earned 
    ("------------------------------------------")
    print("YOU EARNED", jcoins_earned, "JCOINS!")
    print("CURRENT BALANCED:", player.jcoins, "JCOINS!")
    ("------------------------------------------")

def exp_gain():

    exp_gained = enemy.atk + enemy.dfs
    player.exp += exp_gained
    remaining_exp = exp_gained

    while player.exp >= required_exp:
        level_up()
        print(player.name, "gained", remaining_exp, "EXP!")
        print(player.name, "has leveled up to level", player.lvl)
        remaining_exp = player.exp

    if remaining_exp > 0:
        print(player.name, "gained", remaining_exp, "EXP!")

def player_creation():
    
    skill_p = 4

    while skill_p > 0:
        
        clear_screen(0)
        display_player()
        print("SKILL POINTS AVAIALBE: ", skill_p)
        p_input = input("HP | ATTACK | DEFENSE: ").lower()

        if p_input == "hp" and skill_p > 0:
            skill_p -= 1
            player.max_hp += 5
            player.hp = player.max_hp
        elif p_input == "attack" and skill_p > 0:
            skill_p -= 1
            player.atk += 3
        elif p_input == "defense" and skill_p > 0:
            skill_p -= 1
            player.dfs += 2
        else:
            continue

    clear_screen(0)
    display_player()

    player.name = input("WHAT'S YOUR NAME? ").upper()
    clear_screen(0)

# ENEMY FUNCTIONS ------------------------------------------------

def enemy_stats_handler():

    start_tier = ["THIEF", "SLIME", "BULL"]
    low_tier = ["WOLF", "GOBLIN"]
    mid_tier = ["DUELIST", "FAIRY"]
    high_tier = ["GHOST", "DEMON"]

    enemy.name = ""
    enemy.lvl = 1
    enemy.hp = 20
    enemy.max_hp = 20
    enemy.atk = 1
    enemy.dfs = 1

    if player.lvl <= 4:
        enemy.name = random.choice(start_tier)
        enemy.lvl = random.randint(1, 2)
        enemy.hp += (enemy.lvl * 1)
        enemy.max_hp = enemy.hp
        enemy.atk += (enemy.lvl + 2)
        enemy.dfs += (enemy.lvl + 1)
    elif player.lvl > 4 and player.lvl <= 9:
        enemy.name = random.choice(low_tier)
        enemy.lvl = random.randint(4, 9)
        enemy.hp += (enemy.lvl * 2) + 15
        enemy.max_hp = enemy.hp
        enemy.atk += (enemy.lvl + 2) + random.randint(1, 4)
        enemy.dfs += (enemy.lvl + 2) + random.randint(1, 2)
    elif player.lvl >= 10 and player.lvl <= 15:
        enemy.name = random.choice(mid_tier)
        enemy.lvl = random.randint(10, 15)
        enemy.hp += (enemy.lvl * 4) + 30
        enemy.max_hp = enemy.hp
        enemy.atk += (enemy.lvl + 4) + random.randint(2, 4)
        enemy.dfs += (enemy.lvl + 4) + random.randint(1, 2)
    elif player.lvl >= 16:
        enemy.name = random.choice(high_tier)
        enemy.lvl = random.randint(16, 24)
        enemy.hp += (enemy.lvl * 8) + 50
        enemy.max_hp = enemy.hp
        enemy.atk += (enemy.lvl + 8) + random.randint(2, 4)
        enemy.dfs += (enemy.lvl + 8) + random.randint(1, 2)

# INVENTORY FUNCTIONS ------------------------------------------------

def inventory():
    while True:
        clear_screen(0)
        display_player()
        print("------------------------------------------")
        print(colored("SELECT INVENTORY".center(42), "yellow"))
        print("------------------------------------------")
        print(" - WEAPONS INVENTORY (WI)")
        print(" - ARMOR INVENTORY (AI)")
        print(" - USABLE INVENTORY (UI)")
        print("------------------------------------------")

        selected_option = input().lower()

        if selected_option == "wi":
            # Weapons inventory loop
            while True:
                clear_screen(0)
                display_player()
                print("------------------------------------------")
                print(colored("WEAPONS INVENTORY".center(42), "yellow"))
                print("------------------------------------------")

                owned_weapons = []

                for weapon_instance in [fists, small_dagger, iron_sword, wooden_bow]:
                    if weapon_instance.ow:
                        owned_weapons.append(weapon_instance)

                for index, weapon in enumerate(owned_weapons, start=1):
                    print(f"{index}. {weapon.name} | ATK: {weapon.atk}, DFS: {weapon.dfs}")
                print("------------------------------------------")
                print("Select a weapon number to equip (BACK):")
                selected_option = input(">> ").lower()

                if selected_option == 'back':
                    break
                else:
                    try:
                        selected_index = int(selected_option) - 1
                        if 0 <= selected_index < len(owned_weapons):
                            player.weapon = owned_weapons[selected_index]
                    except ValueError:
                        continue

        elif selected_option == "ai":
            # Armor inventory loop
            while True:
                clear_screen(0)
                display_player()
                print("------------------------------------------")
                print(colored("ARMOR INVENTORY".center(42), "yellow"))
                print("------------------------------------------")

                owned_armor = []

                for armor_instance in [leather_armor, iron_armor, maid_outfit]:
                    if armor_instance.ow:
                        owned_armor.append(armor_instance)

                for index, armor in enumerate(owned_armor, start=1):
                    print(f"{index}. {armor.name} | HP({armor.hp}) | DFS({armor.dfs})")
                print("------------------------------------------")
                print("Select an armor number to equip (BACK):")
                selected_option = input(">> ").lower()

                if selected_option == 'back':
                    break
                else:
                    try:
                        selected_index = int(selected_option) - 1
                        if 0 <= selected_index < len(owned_armor):
                            player.armor = owned_armor[selected_index]
                    except ValueError:
                        continue

        elif selected_option == "ui":
            # Consumable inventory loop
            while True:
                clear_screen(0)
                display_player()
                print("------------------------------------------")
                print(colored("CONSUMABLE INVENTORY".center(42), "yellow"))
                print("------------------------------------------")

                owned_consumables = []

                for consumable_instance in [small_pot, elixir]:
                    if consumable_instance.stock > 0:
                        owned_consumables.append(consumable_instance)

                for index, consumable in enumerate(owned_consumables, start=1):
                    print(f"{index}. {consumable.name} | HP({consumable.hp}) | Stock: x({consumable.stock})")
                print("------------------------------------------")
                print("Select a consumable number to use (BACK):")
                selected_option = input(">> ").lower()

                if selected_option == 'back':
                    break
                else:
                    try:
                        selected_index = int(selected_option) - 1
                        if 0 <= selected_index < len(owned_consumables):
                            selected_consumable = owned_consumables[selected_index]
                            # Calculate the actual HP to be healed without exceeding the maximum HP
                            hp_to_heal = min(selected_consumable.hp, updated_hp - player.hp)
                            # Increase player's HP by the calculated amount
                            player.hp += hp_to_heal
                            # Decrease the stock of the consumable by 1
                            selected_consumable.stock -= 1
                            if selected_consumable.stock <= 0:
                                selected_consumable.ow = False
                                # If the stock is zero, we mark the consumable as not owned ('ow' = False)
                            print(f"You used {selected_consumable.name} and healed {hp_to_heal} HP.")
                            time.sleep(2)
                    except ValueError:
                        print("Invalid input. Please select a valid consumable number or 'back' to go back.")
                        time.sleep(2)

        elif selected_option == "back":
            break

        else:
            print("Invalid input. Please select a valid inventory option.")
            time.sleep(2)

# SHOP FUNCTION ------------------------------------------------

def shop():
    while True:
        clear_screen(0)
        display_player()
        print("------------------------------------------")
        print(colored("SELECT SHOP".center(42), "yellow"))
        print("------------------------------------------")
        print(" - WEAPON SHOP (WS)")
        print(" - ARMOR SHOP (AS)")
        print(" - USABLE SHOP (US)")
        print(" - LEAVE SHOP (BACK)")
        print("------------------------------------------")

        p_input = input().lower()

        if p_input == "ws":
            handle_weapon_shop()
        elif p_input == "as":
            handle_armor_shop()
        elif p_input == "us":
            handle_usable_shop()
        elif p_input == "back":
            break
        else:
            print("Invalid input. Please select a valid shop option.")
            time.sleep(2)

def handle_weapon_shop():
    while True:
        clear_screen(0)
        display_player()
        print("------------------------------------------")
        print(colored("WEAPON SHOP".center(42), "yellow"))
        print("------------------------------------------")

        # List of weapon items in the shop
        weapon_items = [small_dagger, iron_sword, wooden_bow]

        for index, weapon in enumerate(weapon_items, start=1):
            if not weapon.ow:  # Only display weapon items that are not owned
                print(f"{index}. {weapon.name} | ATK: {weapon.atk}, DFS: {weapon.dfs}, Price: {weapon.price}")
        print("------------------------------------------")
        print("Select a weapon number to purchase (BACK):")
        selected_option = input(">> ").lower()

        if selected_option == 'back':
            break
        else:
            try:
                selected_index = int(selected_option) - 1
                if 0 <= selected_index < len(weapon_items):
                    selected_weapon = weapon_items[selected_index]
                    if not selected_weapon.ow:  # Check if the weapon is not owned
                        if player.jcoins >= selected_weapon.price:
                            player.jcoins -= selected_weapon.price
                            selected_weapon.ow = True  # Mark the weapon as owned
                            print(f"You purchased {selected_weapon.name}.")
                        else:
                            print("Insufficient Jcoins. You cannot purchase this weapon.")
                        time.sleep(2)
            except ValueError:
                print("Invalid input. Please select a valid weapon number or 'back' to go back.")
                time.sleep(2)

def handle_armor_shop():
    while True:
        clear_screen(0)
        display_player()
        print("------------------------------------------")
        print(colored("ARMOR SHOP".center(42), "yellow"))
        print("------------------------------------------")

        # List of armor items in the shop
        armor_items = [iron_armor, maid_outfit]

        for index, armor in enumerate(armor_items, start=1):
            if not armor.ow:  # Only display armor items that are not owned
                print(f"{index}. {armor.name} | HP: {armor.hp}, DFS: {armor.dfs}, Price: {armor.price}")
        print("------------------------------------------")
        print("Select an armor number to purchase (BACK):")
        selected_option = input(">> ").lower()

        if selected_option == 'back':
            break
        else:
            try:
                selected_index = int(selected_option) - 1
                if 0 <= selected_index < len(armor_items):
                    selected_armor = armor_items[selected_index]
                    if not selected_armor.ow:  # Check if the armor is not owned
                        if player.jcoins >= selected_armor.price:
                            player.jcoins -= selected_armor.price
                            selected_armor.ow = True  # Mark the armor as owned
                            print(f"You purchased {selected_armor.name}.")
                        else:
                            print("Insufficient Jcoins. You cannot purchase this armor.")
                        time.sleep(2)
            except ValueError:
                print("Invalid input. Please select a valid armor number or 'back' to go back.")
                time.sleep(2)

def handle_usable_shop():
    while True:
        clear_screen(0)
        display_player()
        print("------------------------------------------")
        print(colored("USABLE SHOP".center(42), "yellow"))
        print("------------------------------------------")

        # List of consumable items in the shop
        consumable_items = [small_pot, elixir]

        for index, consumable in enumerate(consumable_items, start=1):
            print(f"{index}. {consumable.name} | HP: {consumable.hp}, Price: {consumable.price}")
        print("------------------------------------------")
        print("Select a consumable number to purchase (BACK):")
        selected_option = input(">> ").lower()

        if selected_option == 'back':
            break
        else:
            try:
                selected_index = int(selected_option) - 1
                if 0 <= selected_index < len(consumable_items):
                    selected_consumable = consumable_items[selected_index]
                    if player.jcoins >= selected_consumable.price:
                        player.jcoins -= selected_consumable.price
                        selected_consumable.ow = True
                        selected_consumable.stock += 1  # Increment the stock of the purchased consumable
                        print(f"You purchased {selected_consumable.name}.")
                    else:
                        print("Insufficient Jcoins. You cannot purchase this consumable.")
                    time.sleep(2)
            except ValueError:
                print("Invalid input. Please select a valid consumable number or 'back' to go back.")
                time.sleep(2)

# EXPLORE FUNCTIONS ---------------------------------------------

def exploring():

    enemy_stats_handler()

    clear_screen(0)
    print("------------------------------------------")
    print("Exploring", player.location, "...")
    print("------------------------------------------")
    clear_screen(2)

    encounter_chance = random.randint(1,5)

    if encounter_chance <= 4:
        clear_screen(0)
        print("------------------------------------------")
        print(player.name, "encountered a", enemy.name, "!")
        print("------------------------------------------")
        clear_screen(2)
        battle_system()
    else:
        clear_screen(0)
        print("------------------------------------------")
        item_drop()
        print("------------------------------------------")
        clear_screen(2)

def item_drop():

    chance = random.randint(1,2)

    if chance == 1:
        small_pot.stock += 1
        print("You found", small_pot.name)
    else:
        elixir.stock += 1
        print("You found", elixir.name)
        

def battle_system():

    print("LVL:", enemy.lvl ,enemy.name, "has appeared!")
    display_opp()
    
    while True:

        player_input = input("ATTACK / RUN: ").lower()

        if player_input == "attack":
            clear_screen(0)
            player_turn()
            if enemy.hp <= 0:
                print("------------------------------------------")
                print(enemy.name, "Has been defeated.")
                print("------------------------------------------")
                money_gain_system()
                exp_gain()
                print("------------------------------------------")
                input("PRESS ENTER TO CONTINUE!")
                print("------------------------------------------")
                clear_screen(0)
                break
            else:
                enemy_turn()
                if player.hp <= 0:
                    print("------------------------------------------")
                    print(player.name, "Has been defeated.")
                    print("------------------------------------------")
                    clear_screen(2)
                    break
        elif player_input == "run":
            print("You ran away succesfully!")
            clear_screen(2)
            break
        else:
            clear_screen(0)
            display_opp()

    return True
    

def display_opp():

    player_info = f"LVL:{player.lvl}    {player.name:<6s} |  {player.hp} / {updated_hp} HP"
    enemy_info = f"LVL:{enemy.lvl}    {enemy.name:<6s} |  {enemy.hp} / {enemy.max_hp} HP"
    
    print("------------------------------------------")
    print(player_info)
    print(enemy_info)
    print("------------------------------------------")

def player_turn():
    damage_done = max(1, updated_atk - enemy.dfs)
    enemy.hp = max(0, enemy.hp - damage_done)
    

def enemy_turn():
    damage_done = max(1, enemy.atk - updated_dfs)
    player.hp = max(0, player.hp - damage_done)
    display_opp()

# DATA FUNCTIONS ------------------------------------------------

def menu_ui():
        
        print("------------------------------------------")
        print(colored("EXPLORE | AREA | SHOP | INV | SAVE | QUIT".center(42), "yellow"))
        print("------------------------------------------")
        
        p_input = input(">> ").lower()

        if p_input == "inv":
            inventory()
        elif p_input == "shop":
            shop()
        elif p_input == "explore":
            exploring()

def core_game():

    in_menu = True

    while in_menu:
        clear_screen(0)
        display_player()
        menu_ui()

def clear_screen(x):
    time.sleep(x)
    os.system('cls')

def start_game():

    global player
    global enemy
    
    player = Player()
    enemy = Enemy()
    
    player_creation()
    

required_exp = 10

start_game()
core_game()
    