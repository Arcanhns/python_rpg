import random
import os
import time

In_batte = False
exp_required = 20
area = 1

class Player():
    def __init__(self):
        self.name = None
        self.hp = 15
        self.max_hp = 15
        self.lvl = 1
        self.exp = 0
        self.required_exp = exp_required
        self.atk = random.randint(6,10)
        self.dfs = random.randint(1,4)
        self.jcoins = max(0, 0)

class Enemy():

    enemy_names = ["SLIME", "DEMON", "WOLF", "GHOST", "HUNTER"]
    
    def __init__(self, area):
        self.name = random.choice(self.enemy_names)
        self.hp = int(10 * (area * 2))
        self.max_hp = self.hp
        self.lvl = random.randint(1 + area, 2 + area)
        self.atk = random.randint(1 * (area + 2), 3 * (area + 2))
        self.dfs = random.randint(1 * (area + 2), 2 * (area + 2))
        
    @staticmethod
    def generate_enemy(area):
        return Enemy(area)
    
class Potion:
    
    def __init__(self, name, description, heal_amount, stock):
        self.name = name
        self.description = description
        self.heal_amount = int(heal_amount)
        self.stock = stock

class Atk_x:

    def __init__(self, name, description, in_amount, stock):
        self.name = name
        self.description = description
        in_amount = in_amount
        self.stock = stock

class Dfs_x:

    def __init__(self, name, description, in_amount, stock):
        self.name = name
        self.description = description
        in_amount = in_amount
        self.stock = stock

player = Player()
potion_25 = Potion("SMALL POTION", "Restores 25 HP", 25, 0)
potion_50 = Potion("MEDIUM POTION", "Restores 50 HP", 50, 0)
potion_100 = Potion("BIG POTION", "Restores 100 HP", 100, 0)
atk_x = Atk_x("ATTACK X", "Increase ATK ST", random.randint(4,10), 0)
dfs_x = Dfs_x("DEFENSE X", "Increase DFS ST", random.randint(3,8), 0)

def inventory():

    while True:
        clear_screen(0)
        display_player()

        print("                INVENTORY")
        print("------------------------------------------")
        print("{:<14s}| {:<15s} | {:<6s}".format("NAME", "DESCRIPTION", "STOCK"))
        print("------------------------------------------")
        print("{:<14s}| {:<15s} | {:<6d}".format(potion_25.name, potion_25.description, potion_25.stock))
        print("{:<14s}| {:<15s} | {:<6d}".format(potion_50.name, potion_50.description, potion_50.stock))
        print("{:<14s}| {:<15s} | {:<6d}".format(potion_100.name, potion_100.description, potion_100.stock))
        print("{:<14s}| {:<15s} | {:<6d}".format(atk_x.name, atk_x.description, atk_x.stock))
        print("{:<14s}| {:<15s} | {:<6d}".format(dfs_x.name, dfs_x.description, dfs_x.stock))
        print("------------------------------------------")
        
        player_input = input("ITEM NAME TO USE | BACK: ").lower()
        if player_input == "small potion" and potion_25.stock > 0:
            potion_25.stock -= 1
            player.hp = min(player.max_hp, player.hp + potion_25.heal_amount)
        elif player_input == "medium potion" and potion_50.stock > 0:
            potion_50.stock -= 1
            player.hp = min(player.max_hp, player.hp + potion_50.heal_amount)
        elif player_input == "big potion" and potion_100.stock > 0:
            potion_100.stock -= 1
            player.hp = min(player.max_hp, player.hp + potion_100.heal_amount)
        elif player_input == "attack x" and atk_x.stock > 0:
            atk_x.stock -= 1
            player.atk += random.randint(3, 6)
        elif player_input == "defense x" and dfs_x.stock > 0:
            dfs_x.stock -= 1
            player.dfs += random.randint(3, 6)
        elif player_input == "back":
            clear_screen(0)
            break
        else:
            clear_screen(0)

def area_handler():

    global area

    while True:

        print("------------------------------------------")
        print("YOU ARE CURRENTLY IN AREA:", area)
        print("------------------------------------------")
        print("'+' OR '-' TO CHANGE AREA ")
        player_input = input("TYPE BACK TO GO BACK ")
        print("------------------------------------------")

        if player_input == "+":
            area = area + 1
            clear_screen(0)
        elif player_input == "-" and area > 1:
            area = area - 1
            clear_screen(0)
        elif player_input == 'back':
            clear_screen(0)
            break
        else:
            print("SELECT A VALID INPUT")
            clear_screen(0)

def display_player():
    print("------------------------------------------")
    print("                 PLAYER")
    print("------------------------------------------")
    print("NAME:", player.name)
    print("HP:", player.hp)
    print("MAX HP:", player.max_hp)
    print("LVL:", player.lvl)
    print("EXP:", player.exp)
    print("REQUIRED EXP:", exp_required)
    print("ATTACK:", player.atk)
    print("DEFENSE:", player.dfs)
    print("------------------------------------------")
    print("JCOINS:", player.jcoins)
    print("------------------------------------------")

def player_turn():
    damage = max(1, player.atk - enemy.dfs)
    enemy.hp = max(0, enemy.hp - damage)
    

def enemy_turn():
    damage = max(1, enemy.atk - player.dfs)
    player.hp = max(0, player.hp - damage)
    display_opp()
    

def display_opp():

    player_info = f"LVL:{player.lvl}    {player.name:<6s} |  {player.hp} / {player.max_hp} HP"
    enemy_info = f"LVL:{enemy.lvl}    {enemy.name:<6s} |  {enemy.hp} / {enemy.max_hp} HP"
    
    print("------------------------------------------")
    print(player_info)
    print(enemy_info)
    print("------------------------------------------")

def battle():

    print("A wild", "LVL:", enemy.lvl ,enemy.name, "has appeared!")
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


def drop_system():
    drops = []

def money_gain_system():
    jcoins_earned = 0
    jcoins_earned += random.randint(4,12) + enemy.lvl
    player.jcoins += jcoins_earned 
    ("------------------------------------------")
    print("YOU EARNED", jcoins_earned, "JCOINS!")
    print("CURRENT BALANCED:", player.jcoins, "JCOINS!")
    ("------------------------------------------")

def shop():

    while True:
        
        print("ฅ(^•ﻌ•^)ฅ      JINGUS SHOP      ฅ(^•ﻌ•^)ฅ")
        print("------------------------------------------")
        print(" - SMALL POTION (25 HP)    | 25 JCOINS")
        print(" - MEDIUM POTION (50 HP)   | 45 JCOINS")
        print(" - BIG POTION (100 HP)     | 75 JCOINS")
        print(" - ATTACK X (+5 / 10 ATK)  | 35 JCOINS")
        print(" - DEFENSE X (+5 / 10 DFS) | 40 JCOINS")
        print("------------------------------------------")
        print("BALANCE:", player.jcoins, "JCOINS")
        print("------------------------------------------")

        player_input = input("ANYTHING YOU WANT TO BUY? ").lower()

        if player_input == "small potion" and player.jcoins >= 25:
            player.jcoins -= 25
            potion_25.stock += 1
            clear_screen(0)
            display_player()
        elif player_input == "medium potion" and player.jcoins >= 45:
            player.jcoins -= 45
            potion_50.stock += 1
            clear_screen(0)
            display_player()
        elif player_input == "big potion" and player.jcoins >= 75:
            player.jcoins -= 75
            potion_100.stock += 1
            clear_screen(0)
            display_player()
        elif player_input == "attack x" and player.jcoins >= 35:
            player.jcoins -= 35
            atk_x.stock += 1
            clear_screen(0)
            display_player()
        elif player_input == "defense x" and player.jcoins >= 35:
            player.jcoins -= 35
            dfs_x.stock += 1
            clear_screen(0)
            display_player()
        elif player_input == "back":
            clear_screen(0)
            break
        else:
            clear_screen(0)
            display_player()

def level_up():

    op_lvl = player.lvl
    op_hp = player.hp
    op_max_hp = player.max_hp
    op_require_exp = player.required_exp
    op_atk = player.atk
    op_dfs = player.dfs
    
    global exp_required
    current_exp_required = exp_required
    exp_required = int(exp_required * 1.2)

    player.lvl += 1
    player.hp = int(player.hp * 1.1 + random.randint(1,2))
    player.max_hp = int(player.max_hp * 1.1)
    player.exp -= current_exp_required # resets player exp
    player.atk = int(player.atk * 1.1 + random.randint(1,3))
    player.dfs = int(player.dfs * 1.1 + random.randint(1,3)) 

    print("------------------------------------------")
    print("                LEVEL UP")
    print("------------------------------------------")
    print("NAME:", player.name)
    print("HP:", op_hp, ">", player.hp)
    print("MAX HP:", op_max_hp, ">", player.max_hp)
    print("LVL:", op_lvl , ">", player.lvl)
    print("REQUIRED EXP:", op_require_exp , ">" , exp_required)
    print("ATTACK:", op_atk, ">", player.atk)
    print("DEFENSE:", op_dfs, ">", player.dfs)
    print("------------------------------------------")


def exp_gain():

    exp_gained = enemy.atk + enemy.dfs
    player.exp += exp_gained
    remaining_exp = exp_gained

    while player.exp >= exp_required:
        level_up()
        print(player.name, "gained", remaining_exp, "EXP!")
        print(player.name, "has leveled up to level", player.lvl)
        remaining_exp = player.exp

    if remaining_exp > 0:
        print(player.name, "gained", remaining_exp, "EXP!")
    
def clear_screen(x):

    time.sleep(x)
    os.system('cls')

player.name = input("ENTER YOUR NAME: ").upper()
clear_screen(0)

while not In_batte:

    display_player()
    player_input = input("FIGHT | AREA | SHOP | BAG:  ").lower()
    if player_input == "fight":
        clear_screen(0)
        enemy = Enemy.generate_enemy(area)
        battle()
    elif player_input == "area":
        if area > 0:
            clear_screen(0)
            area_handler()
    elif player_input == "shop":
        clear_screen(0)
        display_player()
        shop()
    elif player_input == "bag":
        inventory()
    else:
        clear_screen(0)
