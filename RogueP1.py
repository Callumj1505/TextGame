import random
import time
from colorama import Fore, Style
from Gamelists import response_list, poison_rain_attack, infect_attack, poison_attack_purge, buff_list, response_list2,attack_description,soul_burst_attack, option1, option2, option3, response_append
from GameFunctions import Boss_attack_func, xyrif_attack_func, kill_section, show_ending_section, show_charcter_Death
#character health and attacks 
#==============================================================================================================================#
rogue = 100

poison_purge = 35
infect = 20
poison_rain = 30
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
        print (f'== AMAZING YOU HAVE ENCOUNTERED A SHRINE A BUFF OR DEBUFF COULD BE ADDED LETS HOPE WE GET LUCKY! ==')
        time.sleep(1)
        random_buff = random.choice(buff_list)
        print(random_buff)
        while True:
            #random buff or debuff is applied to character
            if random_buff == "+25HP":
                rogue += 25
                print (f"== YOU HAVE RECEIVED A HEALTH BONUS OF 25HP YOUR HP IS NOW {rogue} ==")
                break
            elif random_buff == "+10ATK":
                poison_purge += 5
                infect += 5
                poison_rain += 5
                soul_burst += 5
                print ("YOU HAVE GOT AN ATTACK BUFF OF 10 ALL YOUR ATTACKS DO 5 MORE DAMAGE == ")
                break
            elif random_buff == "-10HP":
                rogue -= 10
                print(f"== YOU HAVE BEEN GIVEN A DEBUFF OF -10HP YOU ARE NOW AT {rogue}")
                break
            elif random_buff == "-10ATK":
                poison_purge -= 5
                infect -= 5
                poison_rain -= 5
                soul_burst -= 5
                print("== YOU HAVE BEEN GIVEN A DEBUFF YOU NOW HAVE -10ATK ALL ATTACKS TO 5 LESS DAMAGE ==")
                break
                
        time.sleep(1)
        #playing boss room
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
        while tempest_guardian > 0:
            response_list.pop(0)
            print (random.choice(response_list2))
            print (f"== XYRIF HAS {tempest_guardian}HP | YOU ARE AT {rogue}HP ==")
            print (f'=============================================================================================')   
            answer = input("Choose Attack > ").lower()
            if answer in attack_description:
                print(attack_description[answer])
            elif response_list2:
                response_list2.append(response_append)
                print(response_append)
            elif answer == "a":
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
                print(f"== XYRIF HAS {tempest_guardian}HP | YOU ARE AT {rogue}HP ==")
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
            

#First Fight starting
#==============================================================================================================================#
def roguepath1():
    global rogue, xyrif
    with open(r'C:\Users\callu\Desktop\coding\game\username.txt', 'r') as file:
        name = file.read()
    print (f'=============================================================================================')      
    print (Fore.RED + f"== YOU HAVE ENTERED PATH 1 WITH THE ROGUE GET READY! ==")
    
    time.sleep(1)
    option1 = ["YOUR ATTACKS","poison purge","infect      ","poison rain ","soul burst  "]
    option2 = ["XYRIF ATTACKS","light beam      ","antimatter pulse","punch           ","xyrif           "]#
    option3 = ["TEMPEST GUARDIAN ATTACKS","swing","pulse blast","call of guardians","wraith strike","tempest"]
    print (Fore.CYAN + f"== TO CHOOSE ATTACK PLEASE TYPE 'A' - 'B' - 'C' ==" + Style.RESET_ALL)
    print (f"== YOU CAN VIEW YOUR ATTACKS AND THERE DESCRIPTION BY TYPING ANT OF THE FOLLOWING WHEN INGAME:")
    for item1, item2, item3 in zip(option1, option2, option3):
        print (Fore.CYAN + f"{item1} - {item2} - {item3}" + Style.RESET_ALL)
    print (f'=============================================================================================')  
    
    time.sleep(3)
    while xyrif > 0:
        response_list.pop(0)
        print (random.choice(response_list))
        print (f"== XYRIF HAS {xyrif}HP | YOU ARE AT {rogue}HP ==")
        print (f'=============================================================================================')   
        answer = input("Choose Attack > ").lower()
        if answer in attack_description:
            print(attack_description[answer])
        elif response_list:
            response_list.append(response_append)
            print(response_append)
        elif answer == "a":
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
        
roguepath1()

