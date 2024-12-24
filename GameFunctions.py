
xyrif = 100
tempest_guardian = 100
import random
from Gamelists import xyrif_random_attacks, tempest_random_attacks
#Boss attack function Rogue P1
#==============================================================================================================================#
def Boss_attack_func():
        global rogue, tempest_random_attacks
        enemy_attack_choice2 = random.choice(tempest_random_attacks)
        print(enemy_attack_choice2)
        if enemy_attack_choice2 == "== HE USES WRAITH STRIKE AND LANDS IT! ==":
            rogue -= 20
            print(f"== XYRIF HAS {tempest_guardian}HP | YOU ARE AT {rogue}HP ==")
        elif enemy_attack_choice2 == "== TEMPEST GUARDIAN IS CHARGING PULSE BLAST WITH HE SHOOTS AND LANDS IT!":
            rogue -= 30
            print(f"== XYRIF HAS {tempest_guardian}HP | YOU ARE AT {rogue}HP ==")
        elif enemy_attack_choice2 == "== HE USES CALL OF GUARDIANS AND LANDS IT, UNLUCKY! ==":
            rogue -= 40
            print(f"== XYRIF HAS {tempest_guardian}HP | YOU ARE AT {rogue}HP ==")
        else:
            print("== WE CAN ALL BE GREATFULL HE MISSED! ==")
            
#1st enemy attack function Rogue P1
#==============================================================================================================================#
def xyrif_attack_func():
        global rogue, xyrif_random_attacks
        enemy_attack_choice = random.choice(xyrif_random_attacks)
        print(enemy_attack_choice)
        if enemy_attack_choice == "HE USES LIGHT BEAM AND LANDS IT!":
            rogue -= 30
            print(f"== XYRIF HAS {xyrif}HP | YOU ARE AT {rogue}HP ==")
        elif enemy_attack_choice == "== XYRIF ATTACKS WITH ANITMATTER PULSE AND LANDS IT! ==":
            rogue -= 20
            print(f"== XYRIF HAS {xyrif}HP | YOU ARE AT {rogue}HP ==")
        elif enemy_attack_choice == "== HE PUNCHES YOU AND LANDS IT, UNLUCKY! ==":
            rogue -= 10
            print(f"== XYRIF HAS {xyrif}HP | YOU ARE AT {rogue}HP ==")
        else:
            print("== WE CAN ALL BE GREATFUL HE MISSED! ==")

#first enemy kill text Rogue P1
#==============================================================================================================================#
def kill_section():
    print("== HE IS DEAD! GOOD JOB ONTO THE NEXT ROOM. ==")
    
def kill_section3():
    print("== THEY ARE DEAD! GOOD JOB ONTO THE NEXT ROOM. ==")
    
# END OF ROGUE FUNCTIONS!!!
#==============================================================================================================================#
    

# def EnemyMenu():
#     from GameClasses import GameVariables
#     for i, p in zip(GameVariables.chosen_names, GameVariables.chosen_hp):
#         print (f"== NAME: {i} HEALTH: {p} ==")
#         continue

def EnemyMenu():
    from GameClasses import GameVariables
    for name, health in zip(GameVariables.chosen_names, GameVariables.chosen_hp):
        print(f"== NAME: {name} HEALTH: {health} ==")

    
    
    
def warrior_p1_Chest():
    
    from GameClasses import GameVariables, Enemies
    from Gamelists import chest_buffr
    import time
    enem2 = Enemies(0, "", 4, 2)
    print (f'=============================================================================================')
    time.sleep(1)
    print("== YOU HAVE BUMPED INTO A CHEST AND FIND A NEW PEICE OF EQUIPMENT! ==")
    chest_buff1 = random.choice(chest_buffr)
    print(chest_buff1)
    if chest_buff1 == "== YOU HAVE RECIEVED A NEW PEACE OF ARMORE WITH +10 ARMORE! ==":
        wraith_strike -= 5
        pulse_blast -= 5
        call_of_guardians -= 5
        poke -= 5
        print("== ALL ENEMY DAMAGE IS DECREASED BY FIVE ==")
    elif chest_buff1 == "== YOU HAVE RECIEVED NEW SWORD! +10 PHYSICAL DAMAGE! ==":
        poision_purge += 5
        infect += 5
        poision_rain += 5
        soul_burst += 5
        print("== ALL OF YOUR ATTACKS HAS GAINED +5 ATTACK")
    elif chest_buff1 == "== YOU HAVE RECIEVED A ARMORED CHESTPEICE +10 HEALTH ==":
        rogue += 10
        print ("== YOU HAVE +10 HEALTH WOOP WOOP == ")


    
    
    
#ALL PATH FUNCTIONS.
#==============================================================================================================================#

#character death for all paths
#==============================================================================================================================#
def show_charcter_Death():
    print("== UNFORTUNATELY THAT LAST ONE HIT A LITTLE HARD :( ==")
    print("== YOU HAVE SUCCUMB TO YOUR INJURIES ==")
    print("== THANK YOU FOR PLAYING: CREATED BY CALLUM JONES ==")
    
#for all paths and characters.
#==============================================================================================================================#
def show_ending_section():
    print("== CONGRATULATIONS YOU HAVE COMPLETED MY GAME! THANK YOU FOR PLAYING")
    print("== GAME CREATE: CALLUM JONES")
    
