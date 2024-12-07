import random
import time
from lists import response_list, poison_rain_attack, infect_attack, poison_attack_purge, xyrif_random_attacks, buff_list, tempest_random_attacks, response_list2
from Functions import Boss_attack_func, xyrif_attack_func, kill_section2, show_ending_section, show_charcter_Death
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

wraith_strike = 20
pulse_blast = 30
call_of_guardians = 40

#a dictionary to get a discription of what the attacks do!
#==============================================================================================================================#
attack_description ={}

#boss fight starting
#==============================================================================================================================#
def boss_fight():
    global tempest_guardian
    if tempest_guardian <= 0:
        print (f'=============================================================================================')
        time.sleep(1)
        print (f'-- AMAZING YOU HAVE ENCOUNTERED A SHRINE A BUFF OR DEBUFF COULD BE ADDED LETS HOPE WE GET LUCKY! --')
        time.sleep(1)
        random_buff = random.choice(buff_list)
        print(random_buff)
        while True:
            #random buff or debuff is applied to character
            if random_buff == "+25HP":
                rogue += 25
                print (f"-- YOU HAVE RECIEVED A HEALTH BONUS OF 25HP YOUR HP IS NOW {rogue} --")
                break
            elif random_buff == "+10ATK":
                poision_purge += 5
                infect += 5
                poison_rain += 5
                soul_burst += 5
                print ("YOU HAVE GOT AN ATTACK BUFF OF 10 ALL YOUR ATTACKS DO 5 MORE DAMAGE -- ")
                break
            elif random_buff == "-10HP":
                rogue -= 10
                print(f"-- YOU HAVE BEEN GIVEN A DEBUFF OF -10HP YOU ARE NOW AT {rogue}")
                break
            elif random_buff == "-10ATK":
                poision_purge -= 5
                infect -= 5
                poision_rain -= 5
                soul_burst -= 5
                print("-- YOU HAVE BEEN GIVEN A DEBUFF YOU NOW HAVE -10ATK ALL ATTACKS TO 5 LESS DAMAGE --")
                break
                
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
        while xyrif > 0:
            response_list.pop(0)
            print (random.choice(response_list))
            print (f"== XYRIF HAS {tempest_guardian}HP | YOU ARE AT {rogue}HP ==")
            print (f'=============================================================================================')   
            answer = input("Choose Attack > ").lower()
            if answer == "Purge" or answer == "a":
                print (f'=============================================================================================')   
                print (random.choice(poison_attack_purge))
                xyrif -= 35
                print(f"== XYRIF HAS {tempest_guardian}HP | YOU ARE AT {rogue}HP ==")
                print (f'=============================================================================================')   
                time.sleep(1)
                Boss_attack_func()
                print (f'=============================================================================================')   
            elif answer == "infect" or answer == "b":
                print (f'=============================================================================================')  
                print (random.choice(infect_attack))
                xyrif -= 20
                print(f"== XYRIF HAS {tempest_guardian}HP | YOU ARE AT {rogue}HP ==")
                print (f'=============================================================================================')  
                time.sleep(1)
                Boss_attack_func()
                print (f'=============================================================================================')  
            elif answer == "rain" or answer == "c":
                xyrif -= 30
                print (f'=============================================================================================')  
                print (random.choice(poison_attack_purge))
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
    global rogue, xyrif, poison_attack_purge, infect_attack, poison_rain_attack
    with open(r'C:\Users\callu\Desktop\coding\game\username.txt', 'r') as file:
        name = file.read()
    print (f'=============================================================================================')      
    print ("== YOU HAVE ENETERED PATH 1 WITH THE ROGUE GET READY! ==")
    
    time.sleep(1)
    
    print ("== TO CHOOSE ATTACK PLEASE TYPE 'PURGE' - 'INFECT' - 'RAIN' ==")
    print (f'=============================================================================================')  
    
    time.sleep(3)
    while xyrif > 0:
        response_list.pop(0)
        print (random.choice(response_list))
        print (f"== XYRIF HAS {xyrif}HP | YOU ARE AT {rogue}HP ==")
        print (f'=============================================================================================')   
        answer = input("Choose Attack > ").lower()
        if answer == "Purge" or answer == "a":
            print (f'=============================================================================================')   
            print (random.choice(poison_attack_purge))
            xyrif -= 35
            print(f"== XYRIF HAS {xyrif}HP | YOU ARE AT {rogue}HP ==")
            print (f'=============================================================================================')   
            time.sleep(1)
            xyrif_attack_func()
            print (f'=============================================================================================')   
        elif answer == "infect" or answer == "b":
            print (f'=============================================================================================')  
            print (random.choice(infect_attack))
            xyrif -= 20
            print(f"== XYRIF HAS {xyrif}HP | YOU ARE AT {rogue}HP ==")
            print (f'=============================================================================================')  
            time.sleep(1)
            xyrif_attack_func()
            print (f'=============================================================================================')  
        elif answer == "rain" or answer == "c":
            xyrif -= 30
            print (f'=============================================================================================')  
            print (random.choice(poison_attack_purge))
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
        kill_section2()
        boss_fight()
    elif rogue < 0:
        show_charcter_Death()
        
roguepath1()

