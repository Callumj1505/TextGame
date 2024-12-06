import random
import time
from ListsRogue import response_list, poison_rain_attack, infect_attack, poison_attack_purge, xyrif_random_attacks, buff_list

#charcter health and attacks 
#==============================================================================================================================#
rogue = 100

poision_purge = 35
infect = 20
poision_rain = 30
soul_burst = 40

#a dictionary to get a discription of what the attacks do!
#==============================================================================================================================#
attack_description ={}

#boss health and attacks
#==============================================================================================================================#
xyrif = 100

light_beam = 30
anitmatter_pulse = 20
punch = 10

buff_list = ["+25HP", "+10ATK", "-10HP", "-10ATK"]
random_buff = random.choice(buff_list)

#this link to his attack function this is weather he lands or misses.
#==============================================================================================================================#
xyrif_random_attacks = [
    "== HE USES LIGHT BEAM AND LANDS IT! ==",
    "== HE USES LIGHT BEAM AND MISSES! ==",
    "== XYRIF ATTACKS WITH ANITMATTER PULSE AND LANDS IT!",
    "== XYRIF ATTACKS WITH ANITMATTER PULSE AND MISSES, LUCKY YOU! ==",
    "== HE PUNCHES YOU AND LANDS IT, UNLUCKY! ==",
    "== HE PUNCHES YOU AND MISSES, WE WILL COUNT THAT ONE AS A WIN! =="
]
#when poison attack is chosen this text prints randomly
#==============================================================================================================================#
poison_attack_purge = [
    "== DAMN THAT ISNT FUN FOR HIM! LUCKLY I DONT FEEL BAD :D ==", #1
    "== I PERSONALLY WOULDNT WANT TO EXPERIENCE THAT! GOOD JOB KEEP IT UP. ==", #2
    "== BEEP BOOP PURGING BEEP BOOP! ==", #3
    "== IF IT WAS ME I WOULDN'T PERSONALLY LIKE THAT! ==", #4
    "== GO CRAZY AHHHHHH GO STUPID AHHHHH.... GOOD JOB. ==", #5
    "== ENJOYING WATCHING YOU WIN.. FOR ONCE HAHAHAHAHA! ==" #6
]
#when infect attack is chosen this text prints randomly
#==============================================================================================================================#
infect_attack = [
    f"== YOU INFECTED HIM -20 FOR HIM! ==",#1
    "== TRY NOT TO GET A CUT DONT WANT TO GO THAT FAR! ==",#2
    "== TRY NOT TO LAUGH CHALLENGE, OHN WAIT TO LATE HA HA HA ==",#3
    "== OMG HE JUST GOT INFECTED FROM YOUR LOVE :0 JKJK EZ -20 ==",#4
    "== YOUR SMASHING THIS KEEP IT UP! ==",#5
    "== BISH BASH BOSH YOU INFECTED HIM CARRY ON PUSHING ==",#6
]
#when poison rain is chosen this text prints randomly
#==============================================================================================================================#
poison_rain_attack =[
    "== ITS RAINING POISON HALLELIJAH ITS RAINING POISON! ==",#1
    "== HITTING HIM WITH THE BIG GUNS KEEP HER GOIN! ==",#2
    "== BEING POISONED THIS MUCH CANT BE FUN IN ALL FAIRNESS! ==",#3
    "== PINKY PONKO POISON! THERES NO WAY HE ISNT FEELING THIS! FINISH HIM. ==",#4
    "== DONT LET HIM EFFECT YOU WITH HIS NONCHALANTNESS. ==",#5
    "== RUEN EM DOWN AND POISON EM DOWN....",#6
]
#round start text. print randomly
#==============================================================================================================================#
response_list = [
f"== GOING STRONG SO FAR! LESTS SEE WHAT YOU CHOOSE NEXT!==\n== Poision Purge -35HP == Infect -20HP == Poison Rain -30HP ==",#1
f"== GOOD JOB WITH THAT ONE, LETS FINISH HIM OFF SOONER RATHER THSN LATER ==\n== Poision Purge -35HP == Infect -20HP == Poison Rain -30HP ==", #2
f"== OKAY ONTO THE NEXT ATTACK! BRING IT ON XYRIF ==\n== Poision Purge -35HP == Infect -20HP == Poison Rain -30HP ==",#3
f"== COMMANDER HES WE ARE ATTACKING WHAT ARE YOU GUNNA DO! ==\n== Poision Purge -35HP == Infect -20HP == Poison Rain -30HP ==", #4
f"== SIR WE ARE GOING TO ATTACK PREPARE! ==\n== Poision Purge -35HP == Infect -20HP == Poison Rain -30HP ==", #5
f"== THERE IS ONLY ONE VICTOR IN THIS REALM LETS HOPE ITS YOU! ==\n== Poision Purge -35HP == Infect -20HP == Poison Rain -30HP ==" #6
]
#enemy attack function
#==============================================================================================================================#
def xyrif_attack_func():
        global rogue
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
            
#text that is displayed when first enemy is dead
#==============================================================================================================================#
def kill_section2():
    print("== GOBLIN IS DEAD! GOOD JOB ONTO THE NEXT ROOM. ==")

#boss fight starting
#==============================================================================================================================#
def boss_fight():
    global xyrif, random_buff, rogue, soul_burst
    
    tempest_guardian = 100
    
    wraith_strike = 20
    pulse_blast = 30
    call_of_guardians = 40
    
    if xyrif <= 0:
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
        
roguepath1()

