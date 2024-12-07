
path1 = "left"
path2 = "middle"
path3 = "right"

goblin = 100
character = 100

second3 = 3

second5 = 5

second = 1.3

half = 0.4

#players attacks
fireball = 30
zap = 40
wack = 20

# moves goblin
spit = 15
slap = 25
bite = 20

#boss hp
gorlock_the_destroyer = 100

#player attacks
fireball = 30
zap = 40
wack =20
rolling_thunder = 50

#gorlock attacks
poke = 20
body_slam =  30
Electric_Hammer = 35
Hammer_swing = 30

import time
from PIL import Image
import random
from lists import goblin_attack2, goblin_attack1, goblin_attack3, gorlock_list, gorlock_list2, gorlock_list3, gorlock_list4, buff_list
from Functions import show_ending_section, show_charcter_Death, kill_section

im = Image.open(r'C:\Users\callu\Desktop\coding\r.png')
im2 = Image.open(r'C:\Users\callu\Desktop\coding\wi.png')
im3 = Image.open(r'C:\Users\callu\Desktop\coding\w.png')

#---------------------------------------------------------------------------------------------------------------------------------#
#PATH 2
#this brings over name from gamebv1.py
with open(r'C:\Users\callu\Desktop\coding\game\username.txt', 'r') as file:
    name = file.read()
    
def goblin_killP3():
    #boss hp
    gorlock_the_destroyer = 100

    #player attacks
    fireball = 30
    zap = 40
    wack =20
    rolling_thunder = 50

    #gorlock attacks
    poke = 20
    body_slam =  30
    Electric_Hammer = 35
    Hammer_swing = 30
    
    global character
    
    if goblin <= 0:
        print (f'=============================================================================================')
        print("-- YOU HAVE ENCOUNTERED A HEALING TOKEN +30 HP! --")
        character += 30
        print(f"-- YOU HP IS NOW {character} --")
        print (f'=============================================================================================')
        time.sleep(second3)
        print ("-- NEW ATTACK LEARNED ROLLING THUNDER")
        print ("-- This attack that stuns the enemy for one round and allows you to land 2 attacks without getting hit. You can only use this once every other round.")
        time.sleep(second)
        
        
        print (f'======================================================================================================================================================')
        print ("-- ENTERING THE DUNGEON GORLOCK THE DESTROYER")
        print (f'=============================================================================================')


        #first attack
        print ("-- YOU FIRST WHICH ATTACK WILL YOU CHOOSE?")
        print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
        print (f"-- fireball -{fireball}HP == zap -{zap}HP == Wack -{wack}HP == rolling thunder -{rolling_thunder}HP --")
        print (f'=============================================================================================')
        while True:
            gorlock_answer = input("Choose Fireball, Zap, Wack: ").lower()
            if gorlock_answer == "fireball":
                gorlock_the_destroyer -= fireball
                print("-- OOOOO BOSS MAN IS FEELING THAT ONE LOOK AT HIM STUMBLE! --")
                print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                print (f'=============================================================================================')
                break
            elif gorlock_answer == "zap":
                gorlock_the_destroyer -= zap
                print("-- DAYUM I WOULDNT WANT TO BE THAT GUY! --")
                print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                print (f'=============================================================================================')
                break
            elif gorlock_answer == "wack":
                gorlock_the_destroyer -= wack
                print("-- WACKING A GUY THIS BUG SHOULD BE ILLEGAL AND SHOULD ALSO BE A BANISHABLE OFFENSE! --")
                print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                print (f'=============================================================================================')
                break
            elif gorlock_answer == "rolling thunder":
                gorlock_the_destroyer -= rolling_thunder
                print("-- WAYYYYYY THE NEW ATTACK IS WHERE IT IS AT! GOOD JOB :) --")
                print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                print (f'=============================================================================================')
                break
            else:
                print ("Invalid move! Please choose from: fireball, zap, wack, rolling thunder.")
                gorlock_answer = input("Choose Fireball, Zap, Wack: ").lower()
                
            
        gorlock_response = random.choice(gorlock_list)
        print(gorlock_response)
        print (f'=============================================================================================')
        
        if gorlock_response == "-- HE REPLIES WITH ELECTRIC HAMMER AND MISSES *JESUS NOISES START PLAYING* --":
            print("-- OKAY FIRST ONE DOWN GOOD JOB ON NOT GETTING HIT --")  # TITLE
            time.sleep(second)
            print("-- WHAT ELSE YOU GOT TO SHOW EM MAKE SURE IT HITS HARD TO PUT THIS GUY DOWN! --")
            print("-- fireball -30HP == zap -40HP == wack -20HP == Rolling Thunder -50HP --")  # ATTACK LIST
            print("=============================================================================================")
        if gorlock_response == "-- HE SWINGS WITH ELECTRIC HAMMER AND HITS YOU :O --":
            character -= Electric_Hammer
            print("-- WELL FIRST ONE DOWN AND ITS NOT LOOKING AMAZING IS IT... --")
            print(f"-- GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP] --")
            print("=============================================================================================")
            time.sleep(second)
            print("-- WHAT ELSE YOU GOT TO SHOW EM MAKE SURE IT HITS HARD TO PUT THIS GUY DOWN! --") # TITLE
            print("-- fireball -30HP == zap -40HP == wack -20HP == rolling Thunder -50HP --")  # ATTACK LIST
            print("=============================================================================================")
                
        while True:
            gorlock_answer2 = input("Choose Fireball, Zap, Wack: ").lower()
            if gorlock_answer2 == "fireball":
                gorlock_the_destroyer -= fireball
                print("-- SOMEONE CALL A FIREMAN BECAUSE YOUR ON FIREE !!.... or he is :/ --")
                print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                print (f'=============================================================================================')
            elif gorlock_answer2 == "zap":
                gorlock_the_destroyer -= zap
                print("-- ZAPPY ZAAPIDY ZAP ZAP WE LOVE EM! GOOD SHOT. --")
                print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                print (f'=============================================================================================')
            elif gorlock_answer2 == "wack":
                gorlock_the_destroyer -= wack
                print("-- ITS MOMENTS LIKE THIS WHERE I WISH I WASNT THE COMMENTATOR YAWWWNNNN. --")
                print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                print (f'=============================================================================================')
            elif gorlock_answer2 == "rolling thunder":
                gorlock_the_destroyer -= rolling_thunder
                print("-- ROLLING ROLLING ROLLING KEEP IT ROLLING ROOLING ROLLING! --")
                print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                print (f'=============================================================================================')
            elif gorlock_answer == "rolling thunder" and gorlock_answer2 == "rolling thunder":
                print("-- YOU CANT USE THIS RIGHT NOW YOU NEED TO WAIT UNTIL NEXT ROUND TO USE AGAIN! --")
                print("=============================================================================================")
                gorlock_answer2 = input("Choose Fireball, Zap, Wack: ").lower()
            else:
                print ("Invalid move! Please choose from: fireball, zap, wack, rolling thunder.")
                gorlock_answer2 = input("Choose Fireball, Zap, Wack: ").lower()
                
            if gorlock_the_destroyer <= 0:
                show_ending_section()
                break
                
            if character <= 0:
                show_charcter_Death()
                break
            gorlock_response2 = random.choice(gorlock_list2)
            print (gorlock_response2)
            print (f'=============================================================================================')

            if gorlock_response2 == "-- HERE IT COMES... HERE IT LANDS AND HE MISSES POKE IM HAPPY FOR YOU PAL! --":
                print ("-- OKAY WELL THANK GOD YOU DIDNT GET POKED TO DEATH AYE WOULD OF BEEN EMBARASSING! --")
                print("=============================================================================================")
                time.sleep(second)
                print("-- BUT WE ARE ALMOST THERE I KNOW YOU CAN DO THIS WHAT YOU GOT NEXT? --")  # TITLE
                print("-- fireball -30HP == zap -40HP == wack -20HP == Rolling Thunder -50hp --")  # ATTACK LIST
                print("=============================================================================================")

            if gorlock_response2 == "-- INCOMMING! A HUGE POKE FROM THE BIG MAN HIMSELF! --":
                character -= poke
                print ("-- THATS EMBARASSING IMAGINE GETTING POKED LMAO --")
                print(f"-- GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP] --")
                print("=============================================================================================")
                time.sleep(second)
                print("-- BUT WE ARE ALMOST THERE I KNOW YOU CAN DO THIS WHAT YOU GOT NEXT? --")  # TITLE
                print("-- fireball -30HP == zap -40HP == wack -20HP == Rolling Thunder -50hp --")   # ATTACK LIST
                print("=============================================================================================")
        
            while True:
                gorlock_answer3 = input("Choose Fireball, Zap, Wack: ").lower()
                if gorlock_answer3 == "fireball":
                    gorlock_the_destroyer -= fireball
                    print("-- SOMEBODY CALL 9-1-1 SOMEBODY KILLED SOMEONE ON THE DANCE FLOOR!... not really but close. --")
                    print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                    print (f'=============================================================================================')
                    break
                elif gorlock_answer3 == "zap":
                    gorlock_the_destroyer -= zap
                    print("-- BLINDED BY THE LIGHTTTTSSSSS! THAT WAS A BIRGHT ZAP KEEP IT UP! --")
                    print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                    print (f'=============================================================================================')
                    break
                elif gorlock_answer3 == "wack":
                    gorlock_the_destroyer -= wack
                    print("-- DO YOU THINK THIS IS WACK-A-MOLE OR A LIFE OR DEATH SITUATION IM CONFUSED? --")
                    print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                    print (f'=============================================================================================')
                    break
                elif gorlock_answer3 == "rolling thunder":
                    gorlock_the_destroyer -= rolling_thunder
                    print("-- ROLLING THUNDER HAS HIT HIM HARD AND HEAVY LIKE ALWAYS HEHEHE --")
                    print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                    print (f'=============================================================================================')
                    break
                elif gorlock_answer2 == "rolling thunder" and gorlock_answer3 == "rolling thunder":
                    print("-- YOU CANT USE THIS RIGHT NOW YOU NEED TO WAIT UNTIL NEXT ROUND TO USE AGAIN! --")
                    gorlock_answer3 = input("Choose Fireball, Zap, Wack: ").lower()
                    print (f'=============================================================================================')
                    break
                else:
                    print ("Invalid move! Please choose from: fireball, zap, wack, rolling thunder.")
                    gorlock_answer3 = input("Choose Fireball, Zap, Wack: ").lower()
                    
                if gorlock_the_destroyer <= 0:
                    show_ending_section()
                    break
                    
                if character <= 0:
                    show_charcter_Death()
                    break
                gorlock_response3 = random.choice(gorlock_list3)
                print (gorlock_response3)
                print (f'=============================================================================================')
                
                if gorlock_response3 == "-- HERE IT COMES... HERE IT LANDS AND HE MISSES HAMMER SWING IM HAPPY FOR YOU PAL! --":
                    print(f"-- {name} YOU KNOW I DIDNT SEE YOU DODGING THAT ONE BUT YOU DID!--")  # TITLE
                    print("=============================================================================================")
                    time.sleep(second)
                    print("-- YOU ARE RUNNING OUT OF CHANCES BETTER DO SOMTHING! --")  # TITLE
                    print("-- fireball -30HP == zap -40HP == wack -20HP == Rolling Thunder -50hp --")  # ATTACK LIST
                    print("=============================================================================================")

                if gorlock_response3 == "-- PLEASE NO NOT THE HAMMER AGAIN! BOOM YOUR SQUISHED WITH HIS HAMMER SWING --":
                    character -= Hammer_swing
                    print(f"-- {name} DAMN YOUR TAKING A BEATING BETTER END THIS QUICK! --")
                    print(f"-- GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP] --")
                    print("=============================================================================================")
                    time.sleep(second)
                    print("-- YOU ARE RUNNING OUT OF CHANCES BETTER DO SOMTHING! --")  # TITLE
                    print("-- fireball -30HP == zap -40HP == wack -20HP == Rolling Thunder -50hp --")   # ATTACK LIST
                    print("=============================================================================================")
                
                while True:
                    gorlock_answer4 = input("Choose Fireball, Zap, Wack: ").lower()
                    if gorlock_answer4 == "fireball":
                        gorlock_the_destroyer -= fireball
                        print("-- PPEK A BOO THE FIREBALL SEES HIM AND HOPEFULLY WILL KILL HIM!")
                        print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                        print (f'=============================================================================================')
                        break
                    elif gorlock_answer4 == "zap":
                        gorlock_the_destroyer -= zap
                        print("-- ITS SHOCKING YOU MANAGED TO LAND THAT ONE! --")
                        print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                        print (f'=============================================================================================')
                        break
                    elif gorlock_answer4 == "wack":
                        gorlock_the_destroyer -= wack
                        print("-- YIKERSS NOT THIS AGAIN *ROLLES EYES* --")
                        print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                        print (f'=============================================================================================')
                        break
                    elif gorlock_answer4 == "rolling thunder":
                        gorlock_the_destroyer -= rolling_thunder
                        print("-- BOW WOW WOW THATS WHAT THE THUNDER SAIS BOW WOW WOW AND MY HEART KEEPS PUMPING! --")
                        print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                        print (f'=============================================================================================')
                        break
                    elif gorlock_answer3 == "rolling thunder" and gorlock_answer4 == "rolling thunder":
                        print("-- YOU CANT USE THIS RIGHT NOW YOU NEED TO WAIT UNTIL NEXT ROUND TO USE AGAIN! --")
                        gorlock_answer3 = input("Choose Fireball, Zap, Wack: ").lower()
                        print (f'=============================================================================================')
                        break
                    else:
                        print ("Invalid move! Please choose from: fireball, zap, wack, rolling thunder.")
                        gorlock_answer3 = input("Choose Fireball, Zap, Wack: ").lower()
                        
                    if gorlock_the_destroyer <= 0:
                        show_ending_section()
                        break
                        
                    if character <= 0:
                        show_charcter_Death()
                        break
                gorlock_response4 = random.choice(gorlock_list4)
                print (gorlock_response4)
                print("=============================================================================================")
                
                if gorlock_response4 == "-- OMG HE IS IN THE AIR... HES FALLING OMG HE MISSED BODY SLAM YAYYYYYY --":
                    print("=============================================================================================")
                    print("-- THANK GOD THAT BIG LARD DIDNT LAND ON YOUR HEAD! --") 
                    time.sleep(second)
                    print("-- THIS FIGHT IS GOING ON A BIT LONGER THAN I ANTICIPATED! --")  # TITLE
                    print("-- fireball -30HP == zap -40HP == wack -20HP == Rolling Thunder -50hp --")  # ATTACK LIST
                    print("=============================================================================================")

                if gorlock_response4 == "---- OMG HE IS IN THE AIR... AND BOOOOOMMM RIGHT IN HIS BELLY BUTTON HE USES BODY SLAM AND LANDS IT! --":
                    character -= body_slam
                    print("-- THAT HONESLT CANT OF BEEN FUN I FEEL FOR YOU :/ --")
                    print(f"-- GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP] --")
                    print("=============================================================================================")
                    time.sleep(second)
                    print("-- THIS FIGHT IS GOING ON A BIT LONGER THAN I ANTICIPATED! --")  # TITLE
                    print("-- fireball -30HP == zap -40HP == wack -20HP == Rolling Thunder -50hp --")   # ATTACK LIST
                    print("=============================================================================================")
        
                while True:
                    gorlock_answer5 = input("Choose Fireball, Zap, Wack: ").lower()
                    if gorlock_answer5 == "fireball":
                        gorlock_the_destroyer -= fireball
                        print("-- FIRE IN THE HOLE HOPEFULLY NOT HIS THO --")
                        print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                        print (f'=============================================================================================')
                        break
                    elif gorlock_answer5 == "zap":
                        gorlock_the_destroyer -= zap
                        print("-- ZAP YOUTR WAY TO VICTORY! I BELIEVE. --")
                        print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                        print (f'=============================================================================================')
                        break
                    elif gorlock_answer5 == "wack":
                        gorlock_the_destroyer -= wack
                        print("-- OKAY IM NOT SAYING ANYTHING ANYMORE..... --")
                        print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                        print (f'=============================================================================================')
                        break
                    elif gorlock_answer5 == "rolling thunder":
                        gorlock_the_destroyer -= rolling_thunder
                        print("-- BOOM POW YOU GOT HIM WITH THAT ONE! PROUD COMMENTATOR :D --")
                        print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                        print (f'=============================================================================================')
                        break
                    elif gorlock_answer4 == "rolling thunder" and gorlock_answer5 == "rolling thunder":
                        print("-- YOU CANT USE THIS RIGHT NOW YOU NEED TO WAIT UNTIL NEXT ROUND TO USE AGAIN! --")
                        gorlock_answer3 = input("Choose Fireball, Zap, Wack: ").lower()
                        print (f'=============================================================================================')
                        break
                    else:
                        print ("Invalid move! Please choose from: fireball, zap, wack, rolling thunder.")
                        gorlock_answer3 = input("Choose Fireball, Zap, Wack: ").lower()
                    
                    if gorlock_the_destroyer <= 0:
                        show_ending_section()
                        break
                        
                    if character <= 0:
                        show_charcter_Death()
                        break

#---------------------------------------------------------------------------------------------------------------------------------#
    
    
def first_sectionP2():
    character = 100
    goblin = 100
    
    #players attacks
    fireball = 30
    zap = 40
    wack = 20

    # moves goblin
    spit = 15
    slap = 25
    bite = 20
    print (f'-- YOU HAVE ENCOUNTRERED A GOBLIN HE SWINGS BUT MISSES WHATS YOUR NEXT MOVE? --')
    print (f'-- fireball -30HP == zap -40HP == wack -20HP')
    print (f'GOBLIN [ {goblin} HP] YOU [ {character} HP]')
    print (f'=============================================================================================')

    while True:
        answer1 = input("choose fireball, zap or wack  : ").lower()
        print (f'=============================================================================================')
        if answer1 == "fireball":
            goblin -= fireball
            time.sleep(half)
            print (f'-- GOOD SHOT THE GOBLIN FELT THE BURN THERE! --')
            print (f'GOBLIN [ {goblin} HP] YOU [ {character} HP]')
            print (f'=============================================================================================')
            time.sleep(second)
        elif answer1 == "zap":
            goblin -= zap
            time.sleep(half)
            print (f'-- GOOD SHOT GOBLIN IS ELECTRIFIED ABOUT THAT ONE! --')
            print (f'GOBLIN [ {goblin} HP] YOU [ {character} HP]') 
            print (f'=============================================================================================')
            time.sleep(second)
        elif answer1 == "wack":
            goblin -= wack
            time.sleep(half)
            print (f'-- YEAH WACK EM UP SOMTIMES YOU GOTTA BE OLDSCHOOL!')
            print (f'GOBLIN [ {goblin} HP] YOU [ {character} HP]') 
            print (f'=============================================================================================')
            time.sleep(second)
        else:
            print ("Invalid move! Please choose from: fireball, zap or wack.")
            answer1 = input("choose fireball, zap or wack  : ").lower()
            
        if goblin <= 0:
            kill_section()
            goblin_killP3()
            break


        time.sleep(second)

        print (f'-- HE FIGHTS WITH SPIT AND IT HITS YOUR DOME!! --')
        character -= spit
        time.sleep(half)
        print (f'GOBLIN [ {goblin} HP] YOU [ {character} HP]') 
        print (f'=============================================================================================')
        time.sleep(second)

        print (f'-- HOW DO YOU RESPOND? --')
        print (f'-- fireball -30HP == zap -40HP == wack -20HP --')
        print (f'-- GOBLIN [ {goblin} HP] YOU [ {character} HP] --')
        print (f'=============================================================================================')

        while True:
            answer2 = input("choose fireball, zap or wack  : ")
            if answer2 == "fireball":
                goblin -= fireball
                time.sleep(half)
                print (f"-- AMAZING WORK! A FEW MORE AND HE WILL BE DONE WITH! --")
                print (f'-- GOBLIN [ {goblin} HP] YOU [ {character} HP] --')
                print (f'=============================================================================================')
            elif answer2 == "zap":
                goblin -= zap
                time.sleep(half)
                print (f"-- THAT KIDS IS WHY YOU KEEP THE KNIFE OUT THE TOASTER! --")
                print (f'-- GOBLIN [ {goblin} HP] YOU [ {character} HP] --')
                print (f'=============================================================================================')
            elif answer2 == "wack":
                goblin -= wack
                time.sleep(half)
                print (f"-- BOOOOOOOO LOW DAMAGE LOW IMPACT YAWWWNNNN! --")
                print (f'-- GOBLIN [ {goblin} HP] YOU [ {character} HP] --')
                print (f'=============================================================================================')
            else:
                print ("Choose Fireball, Zap, Wack: ")
                answer2 = input("choose fireball, zap or wack  : ")
            if goblin <= 0:
                kill_section()
                goblin_killP3()  
                break

            time.sleep(second)
            print (f'=============================================================================================')
            random_reponse = random.choice(goblin_attack1)
            print (random_reponse)
            print (f'=============================================================================================')
            time.sleep(second)

            if random_reponse == "-- HE REPLIES WITH SLAP BUT HE MISSES THANK GOD --":
                print ("-- LOOKS LIKE YOU GET A SECOND GO FOR FREE LUCKY YOU!")
                print (f'=============================================================================================')
                time.sleep(second)
                print ("-- YOUR TURN TO SHOW EM WHO IS BOSS! --")
                print (f"-- fireball -{fireball}HP == zap -{zap}HP == Wack -{wack}HP --")
                print (f'-- GOBLIN [ {goblin} HP] YOU [ {character} HP] --')
                print (f'=============================================================================================')  

            if random_reponse == "-- HE REPLIES WITH SLAP AND LANDS OOOFF THAT HURTS --":
                character -= slap
                print ("-- WELL YOU WIN SOME YOU LOOSE SOME --")
                print (f'-- GOBLIN [ {goblin} HP] YOU [ {character} HP] --')
                print (f'=============================================================================================')
                time.sleep(second)
                print ("-- YOUR TURN TO SHOW EM WHO IS BOSS! --")
                print (f"-- fireball -{fireball}HP == zap -{zap}HP == Wack -{wack}HP --")
                print (f'-- GOBLIN [ {goblin} HP] YOU [ {character} HP] --')
                print (f'=============================================================================================')    
        
        
            while True:
                answer3 = input("choose fireball, zap or wack  : ").lower()
                if answer3 == "fireball":
                    goblin -= fireball
                    time.sleep(half)
                    print (f'-- {name} THAT MOVE WAS "FIRE" GET IT.... HA..HA..HA') #TITLE
                    print (f'-- GOBLIN [ {goblin} HP] YOU [ {character} HP] --')
                    print (f'=============================================================================================')
                elif answer3 == "zap":
                    goblin -= zap
                    time.sleep(half)
                    print (f'-- {name} BBBZZZZZZZ BBZZZZZZZZ ALL I HEAR IS SIZLING GOBLIN! --') #TITLE
                    print (f'-- GOBLIN [ {goblin} HP] YOU [ {character} HP] --')
                    print (f'=============================================================================================')
                elif answer3 == "wack":
                    goblin -= wack
                    time.sleep(half)
                    print (f'-- {name} THIS IS SO NO DEMURE YOU REALLY NEED TO PICK UP THE DAMAGE! --') #TITLE
                    print (f'-- GOBLIN [ {goblin} HP] YOU [ {character} HP] --')
                    print (f'=============================================================================================')
                else:
                    print("Choose Fireball, Zap, Wack")
                    answer3 = input("choose fireball, zap or wack  : ").lower()
                    
                if goblin <= 0:
                    kill_section()
                    goblin_killP3()  
                    break

                time.sleep(second)
                print (f'=============================================================================================')
                random_response2 = random.choice(goblin_attack2)
                print(random_response2)
                print (f'=============================================================================================')
                time.sleep(second)

                if random_response2 == "-- GOBLIN USES BITE AND MISSES! --":
                    print("-- LOOKS LIKE YOU GET A SECOND GO FOR FREE LUCKY YOU! --")
                    print("=============================================================================================")
                    time.sleep(second)
                    print("-- SURELY THIS WILL BE THE FINAL ATTACK FOR SURE THIS TIME I JUST KNOW IT! --")  # TITLE
                    print("-- fireball -30HP == zap -40HP == wack -20HP --")  # ATTACK LIST
                    print("=============================================================================================")

                if random_response2 == "-- GOBLIN USES BITE AND LANDS IT! --":
                    character -= bite
                    print("-- WELL YOU WIN SOME YOU LOSE SOME --")
                    print(f"-- GOBLIN [ {goblin} HP] YOU [ {character} HP] --")
                    print("=============================================================================================")
                    time.sleep(second)
                    print("-- SURELY THIS WILL BE THE FINAL ATTACK FOR SURE THIS TIME I JUST KNOW IT! --")  # TITLE
                    print("-- fireball -30HP == zap -40HP == wack -20HP --")  # ATTACK LIST
                    print("=============================================================================================")
                    
                while True:
                    answer4 = input("Choose fireball, zap or wack: ").lower()
                    if answer4 == "fireball":
                        goblin -= fireball
                        time.sleep(half)
                        print (f'-- A TRUE WIZARD SICKING TO HIS FIREBALL! --') #TITLE
                        print (f'-- GOBLIN [ {goblin} HP] YOU [ {character} HP] --')
                        print (f'=============================================================================================')
                    elif answer4 == "zap":
                        goblin -= zap
                        time.sleep(half)
                        print (f'-- DOES HE NEED A DOCTOR OR AN ELECTRITION... MAYBE BOTH XD --') #TITLE
                        print (f'-- GOBLIN [ {goblin} HP] YOU [ {character} HP] --')
                        print (f'=============================================================================================')
                    elif answer4 == "wack":
                        goblin -= wack
                        time.sleep(half)
                        print (f'-- BRO IS LAUGHING AT YOU PERSONALLY I WOULDNT TAKE THAT.... --') #TITLE
                        print (f'-- GOBLIN [ {goblin} HP] YOU [ {character} HP] --')
                        print (f'=============================================================================================')
                    else:
                        print("Choose Fireball, Zap, Wack")
                        
                    if goblin <= 0:
                        kill_section()
                        goblin_killP3()  
                        break
                
                    time.sleep(second)
                    print (f'=============================================================================================')
                    random_reponse3 = random.choice(goblin_attack3)
                    print(random_reponse3)
                    print (f'=============================================================================================')
                    time.sleep(second)

                    if random_reponse3 == "-- GOBLIN USES SPIT AND MISSES! --":
                        print ("-- LOOKS LIKE YOU GET A SECOND GO FOR FREE LUCKY YOU! --")
                        print ("-- SURLEY THIS WILL BE THE FINAL ATTACK FOR SURE THIS TIME I JUST KNOW IT! --") #TITLE
                        print (f'-- fireball -30HP == zap -40HP == wack -20HP --') # ATTACK LIST
                        print (f'=============================================================================================')
                        
                    if random_reponse3 == "-- GOBLIN USES SPIT AND LANDS IT --":
                        character -= spit
                        print ("-- WELL YOU WIN SOME YOU LOOSE SOME --")
                        print (f'-- GOBLIN [ {goblin} HP] YOU [ {character} HP] --')
                        print ("-- SURLEY THIS WILL BE THE FINAL ATTACK FOR SURE THIS TIME I JUST KNOW IT! --") #TITLE
                        print (f'-- fireball -30HP == zap -40HP == wack -20HP --') # ATTACK LIST
                        print (f'=============================================================================================')


                    while True:
                        answer5 = input("Choose fireball, zap or wack  : ").lower()
                        if answer5 == "fireball":
                            goblin -= fireball
                            time.sleep(half)
                            print (f'-- GOOD CHOICE CANT BEAT A GOOD OLD FIREBALL! --') #TITLE
                            print (f'-- GOBLIN [ {goblin} HP] YOU [ {character} HP] --')
                            if goblin <= 0:
                                kill_section()
                                goblin_killP3()  
                                break
                        elif answer5 == "zap":
                            goblin -= zap
                            time.sleep(half)
                            print (f'-- ZAPPER MC ZAPPINGTON IMA CALL YOU FROM NOW ON! --') #TITLE
                            print (f'-- GOBLIN [ {goblin} HP] YOU [ {character} HP] --')
                            if goblin <= 0:
                                kill_section()
                                goblin_killP3()  
                                break
                        elif answer5 == "wack":
                            goblin -= wack
                            time.sleep(half)
                            print (f'-- USING WACK IS LIKE PUTTING EGGS IN THE FREEZER..... USELESS! --') #TITLE
                            print (f'-- GOBLIN [ {goblin} HP] YOU [ {character} HP] --')
                            if goblin <= 0:
                                kill_section()
                                goblin_killP3()  
                                break
                        else:
                            print("Choose Fireball, Zap, Wack")
                            answer5 = input("choose fireball, zap or wack  : ").lower()
                            
                            
    #------------------------------------------------------------------------------------------------------------------------------------#
