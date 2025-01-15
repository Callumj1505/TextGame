import random
import time
from colorama import Fore, Style
from Gamelists import response_list, poison_rain_attack, infect_attack, poison_attack_purge, response_list2, chest_buffr, attack_description,soul_burst_attack, option1, option2, option3
from GameFunctions import Boss_attack_func, xyrif_attack_func, kill_section, show_ending_section, show_charcter_Death

#charcter health and attacks 
#==============================================================================================================================#
rogue = 100

poision_purge = 35
infect = 20
poision_rain = 30
soul_burst = 40

#1st enemy health and attacks
#==============================================================================================================================#
xyrif = 100

light_beam = 30
anitmatter_pulse = 20
punch = 10

#Boss health and attacks
#==============================================================================================================================#
tempest_guardian = 100

swing = 10
wraith_strike = 20
pulse_blast = 30
call_of_guardians = 40

#boss fight starting
#==============================================================================================================================#
def boss_fight():
    global tempest_guardian
    if tempest_guardian <= 0:
        print (f'=============================================================================================')
        time.sleep(1)
        print("== YOU HAVE BUMPED INTO A CHEST AND FIND A NEW PEICE OF EQUIPMENT! ==")
        chest_buff1 = random.choice(chest_buffr)
        print(chest_buff1)
        while True:
            if chest_buff1 == "== YOU HAVE RECIEVED A NEW PEACE OF ARMORE WITH +10 ARMORE! ==":
                wraith_strike -= 5
                pulse_blast -= 5
                call_of_guardians -= 5
                poke -= 5
                print("== ALL ENEMY DAMAGE IS DECREASED BY FIVE ==")
                break
            elif chest_buff1 == "== YOU HAVE RECIEVED NEW DAGGERS! +10 PHYSICAL DAMAGE! ==":
                poision_purge += 5
                infect += 5
                poision_rain += 5
                soul_burst += 5
                print("== ALL OF YOUR ATTACKS HAS GAINED +5 ATTACK")
                break
            elif chest_buff1 == "== YOU HAVE RECIEVED A METAL LEGGINGS +10 HEALTH ==":
                rogue += 10
                print ("== YOU HAVE +10 HEALTH WOOP WOOP == ")
                break
        
        print (f'=============================================================================================')
                
        time.sleep(1)
        #playing boss room
        print ("== ONTO THE FINAL BOSS LEVEL ALL YOUR TRAINING HAS LEAD UP TO THIS! ==")
        print (f'=============================================================================================')
        time.sleep(3)
        #announcing a new attack that the charcter learns
        print ("== NEW ATTACK LEARNED SOUL BURST ==")
        print ("== IF YOU WOULD LIKE MORE DETAILS ON THE ATTACK TYPE MOVES :) ==")
        time.sleep(1)
        
        #boss room entrance
        print (f'=============================================================================================')
        print ("== ENTERING THE DUNGEON WITH THE TEMPEST GUARDIAN ==")
        print (f'=============================================================================================')
            
        time.sleep(1)
        while tempest_guardian > 0:
            if not stored_response:
                last_response = (random.choice(response_list2))
                print (last_response)
            else:
                print(stored_response)
                stored_response = None
            print (f"== TEMPEST GUARDIAN HAS {tempest_guardian}HP | YOU ARE AT {rogue}HP ==")
            print (f'=============================================================================================')   
            answer = input("Choose Attack > ").lower()
            if answer in attack_description:
                print(attack_description[answer])
                stored_response = last_response
                continue
        
            last_response = None
            if answer == "a":
                print (f'=============================================================================================')   
                print (random.choice(poison_attack_purge))
                xyrif -= 35
                print(f"== TEMPEST GUARDIAN HAS {tempest_guardian}HP | YOU ARE AT {rogue}HP ==")
                print (f'=============================================================================================')   
                time.sleep(1)
                Boss_attack_func()
                print (f'=============================================================================================')   
            elif answer == "b":
                print (f'=============================================================================================')  
                print (random.choice(infect_attack))
                xyrif -= 20
                print(f"== TEMPEST GUARDIAN HAS {tempest_guardian}HP | YOU ARE AT {rogue}HP ==")
                print (f'=============================================================================================')  
                time.sleep(1)
                Boss_attack_func()
                print (f'=============================================================================================')  
            elif answer == "c":
                xyrif -= 30
                print (f'=============================================================================================')  
                print (random.choice(poison_rain_attack))
                print(f"== TEMPEST GUARDIAN HAS {tempest_guardian}HP | YOU ARE AT {rogue}HP ==")
                print (f'=============================================================================================')  
                time.sleep(1)
                Boss_attack_func()
                print (f'=============================================================================================')
            elif answer == "d":
                xyrif -= 40
                print (f'=============================================================================================')  
                print (random.choice(soul_burst_attack))
                print(f"== TEMPEST GUARDIAN HAS {tempest_guardian}HP | YOU ARE AT {rogue}HP ==")
                print (f'=============================================================================================')  
                time.sleep(1)
                Boss_attack_func()
                print (f'=============================================================================================') 
            else:
                if answer:
                    print (f'=============================================================================================')  
                    print("== INVALID INPUT, PLEASE CHOOSE AN ATTACK! ==")
                    print (f'=============================================================================================')  
                
        if tempest_guardian < 0:
            show_ending_section()
        elif rogue < 0:
            show_charcter_Death()
            
last_response = None
stored_response = None

#First Fight starting
#==============================================================================================================================#
def roguepath3():
    global rogue, xyrif, last_response, stored_response
    with open(r'username.txt', 'r') as file:
        name = file.read()
    print (f'=============================================================================================')      
    print (Fore.RED + f"== YOU HAVE ENETERED PATH 3 WITH THE ROGUE GET READY! ==")
    print (f'=============================================================================================')
    time.sleep(1)
    print (Fore.CYAN + f"== TO CHOOSE ATTACK PLEASE TYPE 'A' - 'B' - 'C' ==" + Style.RESET_ALL)
    print (f"== YOU CAN VIEW YOUR ATTACKS AND THERE DESCRIPTION BY TYPING ANT OF THE FOLLOWING WHEN INGAME:")
    for item1, item2, item3 in zip(option1, option2, option3):
        print (Fore.CYAN + f"{item1} - {item2} - {item3}" + Style.RESET_ALL)
    print (f'=============================================================================================')  
    
    time.sleep(3)
    while xyrif > 0:
        if not stored_response:
            last_response = (random.choice(response_list))
            print (last_response)
        else:
            print(stored_response)
            stored_response = None
        print (f"== XYRIF HAS {xyrif}HP | YOU ARE AT {rogue}HP ==")
        print (f'=============================================================================================')   
        answer = input("Choose Attack > ").lower()
        if answer in attack_description:
            print(attack_description[answer])
            stored_response = last_response
            continue
        
        last_response = None
        if answer == "a":
            print (f'=============================================================================================')   
            print (random.choice(poison_attack_purge))
            xyrif -= 35
            print(f"== XYRIF HAS {xyrif}HP | YOU ARE AT {rogue}HP ==")
            print (f'=============================================================================================')   
            time.sleep(1)
            xyrif_attack_func()
            print (f'=============================================================================================')   
        elif answer == "b":
            print (f'=============================================================================================')  
            print (random.choice(infect_attack))
            xyrif -= 20
            print(f"== XYRIF HAS {xyrif}HP | YOU ARE AT {rogue}HP ==")
            print (f'=============================================================================================')  
            time.sleep(1)
            xyrif_attack_func()
            print (f'=============================================================================================')  
        elif answer == "c":
            xyrif -= 30
            print (f'=============================================================================================')  
            print (random.choice(poison_rain_attack))
            print(f"== XYRIF HAS {xyrif}HP | YOU ARE AT {rogue}HP ==")
            print (f'=============================================================================================')  
            time.sleep(1)
            xyrif_attack_func()
            print (f'=============================================================================================') 
        else:
            if answer:
                print (f'=============================================================================================')  
                print("== INVALID INPUT, PLEASE CHOOSE AN ATTACK! ==")
                print (f'=============================================================================================')  
            
    if xyrif < 0:
        kill_section()
        boss_fight()
    elif rogue < 0:
        show_charcter_Death()

if __name__ == '__main__':
    roguepath3()

