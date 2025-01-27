import random
import time
from gameHPvariables import HPvaribale
from colorama import Fore, Style
from Gamelists import response_list, poison_rain_attack, infect_attack, poison_attack_purge, response_list2, attack_description,soul_burst_attack,option1, option2, option3
#character health and attacks 
#==============================================================================================================================#

poison_purge = 35
infect = 20
poison_rain = 30
soul_burst = 40

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

#boss fight starting
#==============================================================================================================================#
def boss_fight():
    from GameFunctions import Boss_attack_func, show_ending_section, show_charcter_Death
    global tempest_guardian, poison_purge, infect, poison_rain, soul_burst, rogue, tempest_guardian, stored_response, rogue
    print (f'=============================================================================================')
    time.sleep(1)
    print (f'=============================================================================================')
    print("== YOU HAVE ENCOUNTERED A HEALING TOKEN +30 HP! ==")
    HPvaribale.rogue += 30
    print(f"== YOUR HP IS NOW {rogue} ==")
    print (f'=============================================================================================')
    time.sleep(3)
    #announcing a new attack that the charcter learns
    print ("== NEW ATTACK LEARNED SOUL BURST ==")
    print ("== IF YOU WOULD LIKE MORE DETAILS ON THE ATTACK TYPE 'MOVES' :) ==")
    time.sleep(1)
    #playing boss room
    print ("== ONTO THE FINAL BOSS LEVEL ALL YOUR TRAINING HAS LEAD UP TO THIS! ==")
    print (f'=============================================================================================')
    
    
    #boss room entrance
    print (f'=============================================================================================')
    print ("== ENTERING THE DUNGEON WITH THE TEMPEST GUARDIAN ==")
    print (f'=============================================================================================')
        
    print ("== ONTO THE FINAL BOSS LEVEL ALL YOUR TRAINING HAS LEAD UP TO THIS! ==")
    print (f'=============================================================================================')
    time.sleep(3)
    #announcing a new attack that the character learns
    print ("== NEW ATTACK LEARNED SOUL BURST ==")
    print ("== IF YOU WOULD LIKE MORE DETAILS ON THE ATTACK TYPE MOVES :) ==")
    time.sleep(1)
    
    #boss room entrance
    print (f'=============================================================================================')
    print ("== ENTERING THE DUNGEON WITH THE TEMPEST GUARDIAN ==")
    print (f'=============================================================================================')
        
    time.sleep(1)
    while HPvaribale.tempest_guardian > 0:
        if not stored_response:
            last_response = (random.choice(response_list2))
            print (last_response)
        else:
            print(stored_response)
            stored_response = None
        print (f"== TEMPEST GUARDIAN HAS {HPvaribale.tempest_guardian}HP | YOU ARE AT {HPvaribale.rogue}HP ==")
        print (f'=============================================================================================')   
        answer = input("Choose Attack [A, B, C] > ").lower()
        if answer in attack_description:
            print(attack_description[answer])
            stored_response = last_response
            continue
    
        last_response = None
        if answer == "a":
            print (f'=============================================================================================')   
            print (random.choice(poison_attack_purge))
            HPvaribale.tempest_guardian -= 35
            print(f"== TEMPEST GUARDIAN HAS {HPvaribale.tempest_guardian}HP | YOU ARE AT {HPvaribale.rogue}HP ==")
            print (f'=============================================================================================')   
            time.sleep(1)
            Boss_attack_func()
            print (f'=============================================================================================')   
        elif answer == "b":
            print (f'=============================================================================================')  
            print (random.choice(infect_attack))
            HPvaribale.tempest_guardian -= 20
            print(f"== TEMPEST GUARDIAN HAS {HPvaribale.tempest_guardian}HP | YOU ARE AT {HPvaribale.rogue}HP ==")
            print (f'=============================================================================================')  
            time.sleep(1)
            Boss_attack_func()
            print (f'=============================================================================================')  
        elif answer == "c":
            HPvaribale.tempest_guardian -= 30
            print (f'=============================================================================================')  
            print (random.choice(poison_rain_attack))
            print(f"== TEMPEST GUARDIAN HAS {HPvaribale.tempest_guardian}HP | YOU ARE AT {HPvaribale.rogue}HP ==")
            print (f'=============================================================================================')  
            time.sleep(1)
            Boss_attack_func()
            print (f'=============================================================================================')
        elif answer == "d":
            HPvaribale.tempest_guardian -= 40
            print (f'=============================================================================================')  
            print (random.choice(soul_burst_attack))
            print(f"== TEMPEST GUARDIAN HAS {HPvaribale.tempest_guardian}HP | YOU ARE AT {HPvaribale.rogue}HP ==")
            print (f'=============================================================================================')  
            time.sleep(1)
            Boss_attack_func()
            print (f'=============================================================================================') 
        else:
            if answer:
                print (f'=============================================================================================')  
                print("== INVALID INPUT, PLEASE CHOOSE AN ATTACK! ==")
                print (f'=============================================================================================')  
            
    if HPvaribale.tempest_guardian < 0:
        show_ending_section()
    elif HPvaribale.rogue < 0:
        show_charcter_Death()
            

ast_response = None
stored_response = None

# First Fight starting
# ==============================================================================================================================#
def roguepath2():
    global poison_purge, infect, poison_rain, soul_burst, rogue, stored_response
    from GameFunctions import xyrif_attack_func, kill_section, show_charcter_Death
    with open(r'username.txt', 'r') as file:
        name = file.read()
    print (f'=============================================================================================')      
    print (Fore.RED + f"== YOU HAVE ENETERED PATH 1 WITH THE ROGUE GET READY! ==")
    print (f'=============================================================================================')
    time.sleep(1)
    print (Fore.CYAN + f"== TO CHOOSE ATTACK PLEASE TYPE 'A' - 'B' - 'C' ==" + Style.RESET_ALL)
    print (f"== YOU CAN VIEW YOUR ATTACKS AND THERE DESCRIPTION BY TYPING ANT OF THE FOLLOWING WHEN INGAME:")
    for item1, item2, item3 in zip(option1, option2, option3):
        print (Fore.CYAN + f"{item1} - {item2} - {item3}" + Style.RESET_ALL)
    print (f'=============================================================================================')  
    
    time.sleep(3)
    while HPvaribale.xyrif > 0:
        #if not checks if it is still false or = None
        if not stored_response:
            #this assigns last response to random pring response list
            last_response = (random.choice(response_list))
            #if there is no data stores in stored_response this will run
            print (last_response)
        else:
            #if there is data in stored_response this runs
            print(stored_response)
            #resets stores_response to None
            stored_response = None
        print (f"== XYRIF HAS {HPvaribale.xyrif}HP | YOU ARE AT {HPvaribale.rogue}HP ==")
        print (f'=============================================================================================')   
        answer = input("Choose Attack [A, B, C] >").lower()
        if answer in attack_description:
            print(attack_description[answer])
            #assigning stored response to last response
            stored_response = last_response
            continue
        #setting last response to None again.
        last_response = None
        if answer == "a":
            print (f'=============================================================================================')   
            print (random.choice(poison_attack_purge))
            HPvaribale.xyrif -= 35
            print(f"== XYRIF HAS {HPvaribale.xyrif}HP | YOU ARE AT {HPvaribale.rogue}HP ==")
            print (f'=============================================================================================')   
            time.sleep(1)
            xyrif_attack_func()
            print (f'=============================================================================================')   
        elif answer == "b":
            print (f'=============================================================================================')  
            print (random.choice(infect_attack))
            HPvaribale.xyrif -= 20
            print(f"== XYRIF HAS {HPvaribale.xyrif}HP | YOU ARE AT {HPvaribale.rogue}HP ==")
            print (f'=============================================================================================')  
            time.sleep(1)
            xyrif_attack_func()
            print (f'=============================================================================================')  
        elif answer == "c":
            HPvaribale.xyrif -= 30
            print (f'=============================================================================================')  
            print (random.choice(poison_rain_attack))
            print(f"== XYRIF HAS {HPvaribale.xyrif}HP | YOU ARE AT {HPvaribale.rogue}HP ==")
            print (f'=============================================================================================')  
            time.sleep(1)
            xyrif_attack_func()
            print (f'=============================================================================================') 
        else:
            if answer:
                print (f'=============================================================================================')  
                print("== INVALID INPUT, PLEASE CHOOSE AN ATTACK! ==")
                print (f'=============================================================================================')  
                
        if HPvaribale.xyrif <= 0:
            kill_section()
            boss_fight()
        elif HPvaribale.rogue <= 0:
            show_charcter_Death()

if __name__ == "__main__":
    roguepath2()

