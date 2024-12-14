
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
    
# END OF ROGUE FUNCTIONS!!!
#==============================================================================================================================#
    

    
    
    
    
    
    
    
    
    
    
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
    
