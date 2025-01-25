
from gameHPvariables import HPvaribale
import random
from Gamelists import xyrif_random_attacks, tempest_random_attacks

#1st enemy health and attacks
#==============================================================================================================================#

light_beam = 30
anitmatter_pulse = 20
punch = 10

#Boss health and attacks
#==============================================================================================================================#

swing = 10
wraith_strike = 20
pulse_blast = 30
call_of_guardians = 40



#Boss attack function Rogue P1
#==============================================================================================================================#
def Boss_attack_func():
    enemy_attack_choice2 = random.choice(tempest_random_attacks)
    print(enemy_attack_choice2)
    if enemy_attack_choice2 == "== HE USES WRAITH SWING AND LANDS IT! ==":
        HPvaribale.rogue -= swing
        print(f"== TEMPEST GUARDIAN HAS {HPvaribale.tempest_guardian}HP | YOU ARE AT {HPvaribale.rogue}HP ==")
    elif enemy_attack_choice2 == "== TEMPEST GUARDIAN IS CHARGING PULSE BLAST WITH HE SHOOTS AND LANDS IT!":
        HPvaribale.rogue -= pulse_blast
        print(f"== TEMPEST GUARDIAN HAS {HPvaribale.tempest_guardian}HP | YOU ARE AT {HPvaribale.rogue}HP ==")
    elif enemy_attack_choice2 == "== HE USES CALL OF GUARDIANS AND LANDS IT, UNLUCKY! ==":
        HPvaribale.rogue -= call_of_guardians
        print(f"== TEMPEST GUARDIAN HAS {HPvaribale.tempest_guardian}HP | YOU ARE AT {HPvaribale.rogue}HP ==")
    elif enemy_attack_choice2 == "== HE USES WRAITH STRIKE AND LANDS IT! ==":
        HPvaribale.rogue -= wraith_strike
        print(f"== TEMPEST GUARDIAN HAS {HPvaribale.tempest_guardian}HP | YOU ARE AT {HPvaribale.rogue}HP ==")
    else:
        if enemy_attack_choice2 == "== HE HAS MISSED ==":
            pass
            
#1st enemy attack function Rogue P1
#==============================================================================================================================#
def xyrif_attack_func():
    enemy_attack_choice = random.choice(xyrif_random_attacks)
    print(enemy_attack_choice)
    if enemy_attack_choice == "== HE USES LIGHT BEAM AND LANDS IT! ==":
        HPvaribale.rogue -= 30
        print(f"== XYRIF HAS {HPvaribale.xyrif}HP | YOU ARE AT {HPvaribale.rogue}HP ==")
    elif enemy_attack_choice == "== XYRIF ATTACKS WITH ANITMATTER PULSE AND LANDS IT!":
        HPvaribale.rogue -= 20
        print(f"== XYRIF HAS {HPvaribale.xyrif}HP | YOU ARE AT {HPvaribale.rogue}HP ==")
    elif enemy_attack_choice == "== HE PUNCHES ON YOU AND LANDS IT, UNLUCKY! ==":
        HPvaribale.rogue -= 10
        print(f"== XYRIF HAS {HPvaribale.xyrif}HP | YOU ARE AT {HPvaribale.rogue}HP ==")
    else:
        if enemy_attack_choice == "== HE HAS MISSED ==":
            pass

#first enemy kill text Rogue P1
#==============================================================================================================================#
def kill_section():
    print("== HE IS DEAD! GOOD JOB ONTO THE NEXT ROOM. ==")
    
def kill_section3():
    print("== THEY ARE DEAD! GOOD JOB ONTO THE NEXT ROOM. ==")
    
# END OF ROGUE FUNCTIONS!!!
#==============================================================================================================================#


#ALL PATH FUNCTIONS.
#==============================================================================================================================#

#character death for all paths
#==================================#
def show_charcter_Death():
    print("== UNFORTUNATELY THAT LAST ONE HIT A LITTLE HARD :( ==")
    print("== YOU HAVE SUCCUMB TO YOUR INJURIES ==")
    print("== THANK YOU FOR PLAYING: CREATED BY CALLUM JONES ==")
    
#for all paths and characters.
#==============================================================================================================================#
def show_ending_section():
    print("== CONGRATULATIONS YOU HAVE COMPLETED MY GAME! THANK YOU FOR PLAYING")
    print("== GAME CREATE: CALLUM JONES")
    
if __name__ in "__main__":
    Boss_attack_func()
    xyrif_attack_func()