#imports
import time
from PIL import Image
import random
from Gamelists import goblin_attack2, goblin_attack1, goblin_attack3, gorlock_list, gorlock_list2, gorlock_list3, gorlock_list4, buff_list
from GameFunctions import show_ending_section, show_charcter_Death, kill_section
from wizardP3 import first_sectionP3
from wizardP2 import first_sectionP2
from RogueP1 import roguepath1
from RogueP2 import roguepath2
from RogueP3 import roguepath3
from WarriorP1 import warriorpaths


#character selection
a = "wizard"
b = "Rogue"
c = "Warrior"

#path choice
path1 = "left"
path2 = "middle"
path3 = "right"

#player and goblin health
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

#map image to display based on the character you choose
im = Image.open(r'r.png')
im2 = Image.open(r'wi.png')
im3 = Image.open(r'w.png')

#seconds for time.sleep
second3 = 3
second5 = 5
second = 1.3
half = 0.4

#================================================================================================================================-#
#when goblin dies the shrine section runs with this function
def goblin_kill():
    global name
    global gorlock_list, gorlock_list2, gorlock_list3, gorlock_list4
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
    #makes the charcter health global. to be able to be used in functions.
    global character
    #if the goblins hp is 0 or less this is the shrine room that exicutes.
    if goblin <= 0:
        print (f'=============================================================================================')
        time.sleep(second)
        print (f'== AMAZING YOU HAVE ENCOUNTERED A SHRINE A BUFF OR DEBUFF COULD BE ADDED LETS HOPE WE GET LUCKY! ==')
        time.sleep(second)
        random_buff = random.choice(buff_list)
        print(random_buff)
        while True:
            #random buff or debuff is applied to character
            if random_buff == "+25HP":
                character += 25
                print (f"== YOU HAVE RECEIVED A HEALTH BONUS OF 25HP YOUR HP IS NOW {character} ==")
                break
            elif random_buff == "+10ATK":
                fireball += 5
                zap += 5
                wack += 5
                rolling_thunder += 5
                print ("YOU HAVE GOT AN ATTACK BUFF OF 10 ALL YOUR ATTACKS DO 5 MORE DAMAGE == ")
                break
            elif random_buff == "-10HP":
                character -= 10
                print(f"== YOU HAVE BEEN GIVEN A DEBUFF OF -10HP YOU ARE NOW AT {character}")
                break
            elif random_buff == "-10ATK":
                fireball -= 5
                zap -= 5
                wack -= 5
                rolling_thunder -= 5
                print("== YOU HAVE BEEN GIVEN A DEBUFF YOU NOW HAVE -10ATK ALL ATTACKS TO 5 LESS DAMAGE ==")
        time.sleep(second)
        #playing boss room
        print ("== ONTO THE FINAL BOSS LEVEL ALL YOUR TRAINING HAS LEAD UP TO THIS!")
        print (f'=============================================================================================')
        time.sleep(second3)
        #announcing a new attack that the charcter learns
        print ("== NEW ATTACK LEARNED ROLLING THUNDER")
        print ("== This attack that stuns the enemy for one round and allows you to land 2 attacks without getting hit. You can only use this once every other round.")
        time.sleep(second)
        
        #boss room entrance
        print (f'======================================================================================================================================================')
        print ("== ENTERING THE DUNGEON GORLOCK THE DESTROYER")
        print (f'=============================================================================================')
        
        #first attack
        print ("== YOU FIRST WHICH ATTACK WILL YOU CHOOSE?")
        print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
        print (f"== fireball -{fireball}HP == zap -{zap}HP == Wack -{wack}HP == rolling thunder -{rolling_thunder}HP ==")
        print (f'=============================================================================================')
        while True:
            #attack selection fireball,zap,wack or rolling thunder.
            gorlock_answer = input("Choose Fireball, Zap, Wack: ").lower()
            if gorlock_answer == "fireball":
                gorlock_the_destroyer -= fireball
                print("== OOOOO BOSS MAN IS FEELING THAT ONE LOOK AT HIM STUMBLE! ==")
                print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                print (f'=============================================================================================')
                break
            elif gorlock_answer == "zap":
                gorlock_the_destroyer -= zap
                print("== DAYUM I WOULDNT WANT TO BE THAT GUY! ==")
                print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                print (f'=============================================================================================')
                break
            elif gorlock_answer == "wack":
                gorlock_the_destroyer -= wack
                print("== WACKING A GUY THIS BUG SHOULD BE ILLEGAL AND SHOULD ALSO BE A BANISHABLE OFFENSE! ==")
                print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                print (f'=============================================================================================')
                break
            elif gorlock_answer == "rolling thunder":
                gorlock_the_destroyer -= rolling_thunder
                print("== WAYYYYYY THE NEW ATTACK IS WHERE IT IS AT! GOOD JOB :) ==")
                print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                print (f'=============================================================================================')
                break
            else:
                print ("Invalid move! Please choose from: fireball, zap, wack, rolling thunder.")
                gorlock_answer = input("Choose Fireball, Zap, Wack: ").lower()
                
            
        #printing random response.
        gorlock_response = random.choice(gorlock_list)
        print(gorlock_response)
        print (f'=============================================================================================')
        
        #choosing what to do depending what answer is given
        if gorlock_response == "== HE REPLIES WITH ELECTRIC HAMMER AND MISSES *JESUS NOISES START PLAYING* ==":
            print("== OKAY FIRST ONE DOWN GOOD JOB ON NOT GETTING HIT ==")  # TITLE
            time.sleep(second)
            print("== WHAT ELSE YOU GOT TO SHOW EM MAKE SURE IT HITS HARD TO PUT THIS GUY DOWN! ==")
            print(f"== fireball -{fireball}HP == zap -{zap}HP == Wack -{wack}HP == rolling thunder -{rolling_thunder}HP ==")  # ATTACK LIST
            print("=============================================================================================")
        if gorlock_response == "== HE SWINGS WITH ELECTRIC HAMMER AND HITS YOU :O ==":
            character -= Electric_Hammer
            print("== WELL FIRST ONE DOWN AND ITS NOT LOOKING AMAZING IS IT... ==")
            print(f"== GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP] ==")
            print("=============================================================================================")
            time.sleep(second)
            #attack2
            print("== WHAT ELSE YOU GOT TO SHOW EM MAKE SURE IT HITS HARD TO PUT THIS GUY DOWN! ==") # TITLE
            print(f"== fireball -{fireball}HP == zap -{zap}HP == Wack -{wack}HP == rolling thunder -{rolling_thunder}HP ==")  # ATTACK LIST
            print("=============================================================================================")
                
        #attack choices
        while True:
            gorlock_answer2 = input("Choose Fireball, Zap, Wack: ").lower()
            if gorlock_answer2 == "fireball":
                gorlock_the_destroyer -= fireball
                print("== SOMEONE CALL A FIREMAN BECAUSE YOUR ON FIREE !!.... or he is :/ ==")
                print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                print (f'=============================================================================================')
            elif gorlock_answer2 == "zap":
                gorlock_the_destroyer -= zap
                print("== ZAPPY ZAAPIDY ZAP ZAP WE LOVE EM! GOOD SHOT. ==")
                print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                print (f'=============================================================================================')
            elif gorlock_answer2 == "wack":
                gorlock_the_destroyer -= wack
                print("== ITS MOMENTS LIKE THIS WHERE I WISH I WASN'T THE COMMENTATOR YAWWWNNNN. ==")
                print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                print (f'=============================================================================================')
            elif gorlock_answer2 == "rolling thunder":
                gorlock_the_destroyer -= rolling_thunder
                print("== ROLLING ROLLING ROLLING KEEP IT ROLLING ROLLING ROLLING! ==")
                print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                print (f'=============================================================================================')
            elif gorlock_answer == "rolling thunder" and gorlock_answer2 == "rolling thunder":
                print("== YOU CANT USE THIS RIGHT NOW YOU NEED TO WAIT UNTIL NEXT ROUND TO USE AGAIN! ==")
                print("=============================================================================================")
                gorlock_answer2 = input("Choose Fireball, Zap, Wack: ").lower()
            else:
                print ("Invalid move! Please choose from: fireball, zap, wack, rolling thunder.")
                gorlock_answer2 = input("Choose Fireball, Zap, Wack: ").lower()
                #if gorlock dies play this function 
            if gorlock_the_destroyer <= 0:
                show_ending_section()
                break
                #if charcter dies play this function
            if character <= 0:
                show_charcter_Death()
                break
                #print random response
            gorlock_response2 = random.choice(gorlock_list2)
            print (gorlock_response2)
            print (f'=============================================================================================')
            #chooses what to do depending what response is given from random response2
            if gorlock_response2 == "== HERE IT COMES... HERE IT LANDS AND HE MISSES POKE IM HAPPY FOR YOU PAL! ==":
                print ("== OKAY WELL THANK GOD YOU DIDN'T GET POKED TO DEATH AYE WOULD OF BEEN EMBARASSING! ==")
                print("=============================================================================================")
                time.sleep(second)
                print("== BUT WE ARE ALMOST THERE I KNOW YOU CAN DO THIS WHAT YOU GOT NEXT? ==")  # TITLE
                print(f"== fireball -{fireball}HP == zap -{zap}HP == Wack -{wack}HP == rolling thunder -{rolling_thunder}HP ==")  # ATTACK LIST
                print("=============================================================================================")

            if gorlock_response2 == "== INCOMING! A HUGE POKE FROM THE BIG MAN HIMSELF! ==":
                character -= poke
                print ("== THATS EMBARRASSING IMAGINE GETTING POKED LMAO ==")
                print(f"== GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP] ==")
                print("=============================================================================================")
                time.sleep(second)
                #attack3
                print("== BUT WE ARE ALMOST THERE I KNOW YOU CAN DO THIS WHAT YOU GOT NEXT? ==")  # TITLE
                print(f"== fireball -{fireball}HP == zap -{zap}HP == Wack -{wack}HP == rolling thunder -{rolling_thunder}HP ==")   # ATTACK LIST
                print("=============================================================================================")
            #choosing your attack
            while True:
                gorlock_answer3 = input("Choose Fireball, Zap, Wack: ").lower()
                if gorlock_answer3 == "fireball":
                    gorlock_the_destroyer -= fireball
                    print("== SOMEBODY CALL 9-1-1 SOMEBODY KILLED SOMEONE ON THE DANCE FLOOR!... not really but close. ==")
                    print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                    print (f'=============================================================================================')
                    break
                elif gorlock_answer3 == "zap":
                    gorlock_the_destroyer -= zap
                    print("== BLINDED BY THE LIGHTTTTSSSSS! THAT WAS A BIRGHT ZAP KEEP IT UP! ==")
                    print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                    print (f'=============================================================================================')
                    break
                elif gorlock_answer3 == "wack":
                    gorlock_the_destroyer -= wack
                    print("== DO YOU THINK THIS IS WACK-A-MOLE OR A LIFE OR DEATH SITUATION IM CONFUSED? ==")
                    print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                    print (f'=============================================================================================')
                    break
                elif gorlock_answer3 == "rolling thunder":
                    gorlock_the_destroyer -= rolling_thunder
                    print("== ROLLING THUNDER HAS HIT HIM HARD AND HEAVY LIKE ALWAYS HEHEHE ==")
                    print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                    print (f'=============================================================================================')
                    break
                elif gorlock_answer2 == "rolling thunder" and gorlock_answer3 == "rolling thunder":
                    print("== YOU CANT USE THIS RIGHT NOW YOU NEED TO WAIT UNTIL NEXT ROUND TO USE AGAIN! ==")
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
                #random response
                gorlock_response3 = random.choice(gorlock_list3)
                print (gorlock_response3)
                print (f'=============================================================================================')
                #chooses what to do depending on what response was given.
                if gorlock_response3 == "== HERE IT COMES... HERE IT LANDS AND HE MISSES HAMMER SWING IM HAPPY FOR YOU PAL! ==":
                    print(f"== {name} YOU KNOW I DIDN'T SEE YOU DODGING THAT ONE BUT YOU DID!==")  # TITLE
                    print("=============================================================================================")
                    time.sleep(second)
                    print("== YOU ARE RUNNING OUT OF CHANCES BETTER DO SOMETHING! ==")  # TITLE
                    print(f"== fireball -{fireball}HP == zap -{zap}HP == Wack -{wack}HP == rolling thunder -{rolling_thunder}HP ==")  # ATTACK LIST
                    print("=============================================================================================")

                if gorlock_response3 == "== PLEASE NO NOT THE HAMMER AGAIN! BOOM YOUR SQUISHED WITH HIS HAMMER SWING ==":
                    character -= Hammer_swing
                    print(f"== {name} DAMN YOUR TAKING A BEATING BETTER END THIS QUICK! ==")
                    print(f"== GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP] ==")
                    print("=============================================================================================")
                    time.sleep(second)
                    print("== YOU ARE RUNNING OUT OF CHANCES BETTER DO SOMETHING! ==")  # TITLE
                    print(f"== fireball -{fireball}HP == zap -{zap}HP == Wack -{wack}HP == rolling thunder -{rolling_thunder}HP ==")   # ATTACK LIST
                    print("=============================================================================================")
                #choose attacks
                while True:
                    gorlock_answer4 = input("Choose Fireball, Zap, Wack: ").lower()
                    if gorlock_answer4 == "fireball":
                        gorlock_the_destroyer -= fireball
                        print("== PEEK A BOO THE FIREBALL SEES HIM AND HOPEFULLY WILL KILL HIM!")
                        print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                        print (f'=============================================================================================')
                        break
                    elif gorlock_answer4 == "zap":
                        gorlock_the_destroyer -= zap
                        print("== ITS SHOCKING YOU MANAGED TO LAND THAT ONE! ==")
                        print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                        print (f'=============================================================================================')
                        break
                    elif gorlock_answer4 == "wack":
                        gorlock_the_destroyer -= wack
                        print("== YIKERSS NOT THIS AGAIN *ROLLS EYES* ==")
                        print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                        print (f'=============================================================================================')
                        break
                    elif gorlock_answer4 == "rolling thunder":
                        gorlock_the_destroyer -= rolling_thunder
                        print("== BOW WOW WOW THATS WHAT THE THUNDER SAYS BOW WOW WOW AND MY HEART KEEPS PUMPING! ==")
                        print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                        print (f'=============================================================================================')
                        break
                    elif gorlock_answer3 == "rolling thunder" and gorlock_answer4 == "rolling thunder":
                        print("== YOU CANT USE THIS RIGHT NOW YOU NEED TO WAIT UNTIL NEXT ROUND TO USE AGAIN! ==")
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
                
                if gorlock_response4 == "== OMG HE IS IN THE AIR... HES FALLING OMG HE MISSED BODY SLAM YAYYYYYY ==":
                    print("=============================================================================================")
                    print("== THANK GOD THAT BIG LARD DIDN'T LAND ON YOUR HEAD! ==") 
                    time.sleep(second)
                    print("== THIS FIGHT IS GOING ON A BIT LONGER THAN I ANTICIPATED! ==")  # TITLE
                    print(f"== fireball -{fireball}HP == zap -{zap}HP == Wack -{wack}HP == rolling thunder -{rolling_thunder}HP ==")  # ATTACK LIST
                    print("=============================================================================================")

                if gorlock_response4 == "==== OMG HE IS IN THE AIR... AND BOOOOOMMM RIGHT IN HIS BELLY BUTTON HE USES BODY SLAM AND LANDS IT! ==":
                    character -= body_slam
                    print("== THAT HONESTLY CANT OF BEEN FUN I FEEL FOR YOU :/ ==")
                    print(f"== GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP] ==")
                    print("=============================================================================================")
                    time.sleep(second)
                    print("== THIS FIGHT IS GOING ON A BIT LONGER THAN I ANTICIPATED! ==")  # TITLE
                    print(f"== fireball -{fireball}HP == zap -{zap}HP == Wack -{wack}HP == rolling thunder -{rolling_thunder}HP ==")   # ATTACK LIST
                    print("=============================================================================================")
        
                while True:
                    gorlock_answer5 = input("Choose Fireball, Zap, Wack: ").lower()
                    if gorlock_answer5 == "fireball":
                        gorlock_the_destroyer -= fireball
                        print("== FIRE IN THE HOLE HOPEFULLY NOT HIS THO ==")
                        print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                        print (f'=============================================================================================')
                        break
                    elif gorlock_answer5 == "zap":
                        gorlock_the_destroyer -= zap
                        print("== ZAP YOUTR WAY TO VICTORY! I BELIEVE. ==")
                        print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                        print (f'=============================================================================================')
                        break
                    elif gorlock_answer5 == "wack":
                        gorlock_the_destroyer -= wack
                        print("== OKAY IM NOT SAYING ANYTHING ANYMORE..... ==")
                        print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                        print (f'=============================================================================================')
                        break
                    elif gorlock_answer5 == "rolling thunder":
                        gorlock_the_destroyer -= rolling_thunder
                        print("== BOOM POW YOU GOT HIM WITH THAT ONE! PROUD COMMENTATOR :D ==")
                        print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
                        print (f'=============================================================================================')
                        break
                    elif gorlock_answer4 == "rolling thunder" and gorlock_answer5 == "rolling thunder":
                        print("== YOU CANT USE THIS RIGHT NOW YOU NEED TO WAIT UNTIL NEXT ROUND TO USE AGAIN! ==")
                        gorlock_answer3 = input("Choose Fireball, Zap, Wack: ").lower()
                        print (f'=============================================================================================')
                        break
                    else:
                        print ("Invalid move! Please choose from: fireball, zap, wack, rolling thunder.")
                        gorlock_answer3 = input("Choose Fireball, Zap, Wack: ").lower()
                    
                    if gorlock_the_destroyer <= 0:
                        show_ending_section()
                        break
                    elif character <= 0:
                        show_charcter_Death()
                        break

#================================================================================================================================-#
def main():
    #welcoming you to the game
    print (f'=============================================================================================')   

    print (f'== WELCOME TO THE CHOSEN WARRIOR ==')

    print (f'=============================================================================================')    
    time.sleep(second)
    #selecting character from a choice of wizard, rogue, warrior
    print (f'== CHOOSE CHARACTER ==')

    print (f'a' + f'-'+(a), f'b'+f'-'+(b), f'c'+f'-'+(c))


    #depending what character is chose it shows you a map with your characters stats and the path options.
    charanswer=input("enter A, B or C  : ").lower()
    if charanswer == "a":
        print (f'=============================================================================================')    
        print (f'Healthy choice strong for his spells and powers you can be sure to stand your are ground as long as you keep your distance :)')
        print (f'also here is your map for your travels you can access this at any time just keep it open im the background')
        print (f'=============================================================================================')    
        time.sleep(second3)
        im.show() 
    elif charanswer == "b":
        print (f'=============================================================================================')    
        print (f'Rogue: Agile and stealthy, excels in quick attacks and evasion. Use your speed to outmaneuver enemies.')
        print (f'also here is your map for your travels you can access this at any time just keep it open im the background')
        print (f'=============================================================================================') 
        time.sleep(second3)
        im2.show()
    elif charanswer == "c":
        print (f'=============================================================================================')    
        print (f'Warrior: Strong and resilient, capable of withstanding heavy attacks. Use your strength to overpower foes.')
        print (f'also here is your map for your travels you can access this at any time just keep it open im the background')
        print (f'=============================================================================================')
        im3.show()       
    #choosing username and then it get saved into a folder called usernames to be able to be used across work sheets.
    print (f'== TIME TO CHOOSE YOUR USERNAME ==')
    name = input("type your username  : ").upper()
    time.sleep(second)

    with open(r'username.txt', 'w') as file:
        file.write(name)
    print (f'=============================================================================================')   

    print (f'== NICE TO MEET YOU {name} ==')
    time.sleep(second)
    print (f'=============================================================================================')   


    print(f'== OK {name} ITS TIME TO PLAY THE GAME OF DIRECTIONS AND CHOICES')

    print (f'=============================================================================================')

    time.sleep(second)
    #choosing a path
    print(f'== WHICH WAY WOULD YOU LIKE TO GO? ==')
    #path selection options.
    print (f'a' + f'-'+(path1), f'b'+f'-'+(path2), f'c'+f'-'+(path3))

    print (f'=============================================================================================')
    #first encounter/attack with the goblin.
    time.sleep(second)
    while True:
        answer2=input("enter a,b or c  : ").lower()
        if answer2 == "a" and charanswer == "a": 
            print (f'== YOU HAVE ENCOUNTERED A GOBLIN HE SWINGS BUT MISSES WHATS YOUR NEXT MOVE? ==')
            print (f'== fireball -30HP == zap -40HP == wack -20HP')
            print (f'GOBLIN [ {goblin} HP] YOU [ {character} HP]')
            print (f'=============================================================================================')
            break
        elif answer2 == "b" and charanswer == "a": 
            print("== YOU HAVE CHOSE PATH 2 LETS SEE WHAT LURKS AHEAD! ==")
            print (f'=============================================================================================')
            time.sleep(second)
            first_sectionP2()
        elif answer2 == "c" and charanswer == "a":
            print("== YOU HAVE CHOSE PATH 3 WHAT WILL WE FIND? ==")
            print (f'=============================================================================================')
            time.sleep(second)
            first_sectionP3()
        elif answer2 == "a" and charanswer == "b": 
            print("== YOU HAVE CHOSE PATH 1 LETS SEE WHAT LURKS AHEAD! ==")
            print (f'=============================================================================================')
            time.sleep(second)
            roguepath1()
        elif answer2 == "b" and charanswer == "b":
            print("== YOU HAVE CHOSE PATH 2 WHAT WILL WE FIND? ==")
            print (f'=============================================================================================')
            time.sleep(second)
            roguepath2()
        elif answer2 == "c" and charanswer == "b":
            print("== YOU HAVE CHOSE PATH 3 WHAT WILL WE ENCOUNTER? ==")
            print (f'=============================================================================================')
            time.sleep(second)
            roguepath3()
        elif answer2 =="a" and charanswer == "c":
            print("== YOU HAVE CHOSE PATH 1 LETS SEE WHAT LURKS AHEAD! ==")
            print (f'=============================================================================================')
            time.sleep(second)
            warriorpaths()
        elif answer2 =="a" and charanswer == "c":
            print("== YOU HAVE CHOSE PATH 2 WHAT WILL WE FIND? ==")
            print (f'=============================================================================================')
            time.sleep(second)
            warriorpaths()
        elif answer2 =="a" and charanswer == "c":
            print("== YOU HAVE CHOSE PATH 3 WHAT WILL WE ENCOUNTER? ==")
            print (f'=============================================================================================')
            time.sleep(second)
            warriorpaths()
        else:
            print ("== PLEASE CHOOSE A,B OR C ==")
            answer2=input("enter a,b or c  : ").lower()

    while True:
        answer1 = input("choose fireball, zap or wack  : ").lower()
        print (f'=============================================================================================')
        if answer1 == "fireball":
            goblin -= fireball
            time.sleep(half)
            print (f'== GOOD SHOT THE GOBLIN FELT THE BURN THERE! ==')
            print (f'GOBLIN [ {goblin} HP] YOU [ {character} HP]')
            print (f'=============================================================================================')
            time.sleep(second)
        elif answer1 == "zap":
            goblin -= zap
            time.sleep(half)
            print (f'== GOOD SHOT GOBLIN IS ELECTRIFIED ABOUT THAT ONE! ==')
            print (f'GOBLIN [ {goblin} HP] YOU [ {character} HP]') 
            print (f'=============================================================================================')
            time.sleep(second)
        elif answer1 == "wack":
            goblin -= wack
            time.sleep(half)
            print (f'== YEAH WACK EM UP SOMeTIMES YOU GOTTA BE OLD SCHOOL!')
            print (f'GOBLIN [ {goblin} HP] YOU [ {character} HP]') 
            print (f'=============================================================================================')
            time.sleep(second)
        else:
            print ("Invalid move! Please choose from: fireball, zap or wack.")
            answer1 = input("choose fireball, zap or wack  : ").lower()
            #if goblin dies play kill_section() and goblin_kill()
        if goblin <= 0:
            kill_section()
            goblin_kill()
            break

        #stops time for a second
        time.sleep(second)

        #goblins first attack.
        print (f'== HE FIGHTS WITH SPIT AND IT HITS YOUR DOME!! ==')
        character -= spit
        time.sleep(half)
        print (f'GOBLIN [ {goblin} HP] YOU [ {character} HP]') 
        print (f'=============================================================================================')
        time.sleep(second)

        print (f'== HOW DO YOU RESPOND? ==')
        print (f'== fireball -30HP == zap -40HP == wack -20HP ==')
        print (f'== GOBLIN [ {goblin} HP] YOU [ {character} HP] ==')
        print (f'=============================================================================================')

        while True:
            answer2 = input("choose fireball, zap or wack  : ")
            if answer2 == "fireball":
                goblin -= fireball
                time.sleep(half)
                print (f"== AMAZING WORK! A FEW MORE AND HE WILL BE DONE WITH! ==")
                print (f'== GOBLIN [ {goblin} HP] YOU [ {character} HP] ==')
                print (f'=============================================================================================')
            elif answer2 == "zap":
                goblin -= zap
                time.sleep(half)
                print (f"== THAT KIDS IS WHY YOU KEEP THE KNIFE OUT THE TOASTER! ==")
                print (f'== GOBLIN [ {goblin} HP] YOU [ {character} HP] ==')
                print (f'=============================================================================================')
            elif answer2 == "wack":
                goblin -= wack
                time.sleep(half)
                print (f"== BOOOOOOOO LOW DAMAGE LOW IMPACT YAWWWNNNN! ==")
                print (f'== GOBLIN [ {goblin} HP] YOU [ {character} HP] ==')
                print (f'=============================================================================================')
            else:
                print ("Choose Fireball, Zap, Wack: ")
                answer2 = input("choose fireball, zap or wack  : ")
            if goblin <= 0:
                kill_section()
                goblin_kill()  
                break

            #random attack from the goblin
            time.sleep(second)
            print (f'=============================================================================================')
            random_reponse = random.choice(goblin_attack1)
            print (random_reponse)
            print (f'=============================================================================================')
            time.sleep(second)
            #chooses what to do depending on what the answer from the random list is.
            if random_reponse == "== HE REPLIES WITH SLAP BUT HE MISSES THANK GOD ==":
                print ("== LOOKS LIKE YOU GET A SECOND GO FOR FREE LUCKY YOU!")
                print (f'=============================================================================================')
                time.sleep(second)
                print ("== YOUR TURN TO SHOW EM WHO IS BOSS! ==")
                print ("== fireball -30HP == zap -40HP == wack -20HP")
                print (f'== GOBLIN [ {goblin} HP] YOU [ {character} HP] ==')
                print (f'=============================================================================================')  

            if random_reponse == "== HE REPLIES WITH SLAP AND LANDS OOOFF THAT HURTS ==":
                character -= slap
                print ("== WELL YOU WIN SOME YOU LOOSE SOME ==")
                print (f'== GOBLIN [ {goblin} HP] YOU [ {character} HP] ==')
                print (f'=============================================================================================')
                time.sleep(second)
                print ("== YOUR TURN TO SHOW EM WHO IS BOSS! ==")
                print ("== fireball -30HP == zap -40HP == wack -20HP")
                print (f'== GOBLIN [ {goblin} HP] YOU [ {character} HP] ==')
                print (f'=============================================================================================')    
        
        
            while True:
                answer3 = input("choose fireball, zap or wack  : ").lower()
                if answer3 == "fireball":
                    goblin -= fireball
                    time.sleep(half)
                    print (f'== {name} THAT MOVE WAS "FIRE" GET IT.... HA..HA..HA') #TITLE
                    print (f'== GOBLIN [ {goblin} HP] YOU [ {character} HP] ==')
                    print (f'=============================================================================================')
                elif answer3 == "zap":
                    goblin -= zap
                    time.sleep(half)
                    print (f'== {name} BBBZZZZZZZ BBZZZZZZZZ ALL I HEAR IS SIZiLING GOBLIN! ==') #TITLE
                    print (f'== GOBLIN [ {goblin} HP] YOU [ {character} HP] ==')
                    print (f'=============================================================================================')
                elif answer3 == "wack":
                    goblin -= wack
                    time.sleep(half)
                    print (f'== {name} THIS IS SO NO DEMURE YOU REALLY NEED TO PICK UP THE DAMAGE! ==') #TITLE
                    print (f'== GOBLIN [ {goblin} HP] YOU [ {character} HP] ==')
                    print (f'=============================================================================================')
                else:
                    print("Choose Fireball, Zap, Wack")
                    answer3 = input("choose fireball, zap or wack  : ").lower()
                    
                if goblin <= 0:
                    kill_section()
                    goblin_kill()  
                    break

                time.sleep(second)
                print (f'=============================================================================================')
                random_response2 = random.choice(goblin_attack2)
                print(random_response2)
                print (f'=============================================================================================')
                time.sleep(second)

                if random_response2 == "== GOBLIN USES BITE AND MISSES! ==":
                    print("== LOOKS LIKE YOU GET A SECOND GO FOR FREE LUCKY YOU! ==")
                    print("=============================================================================================")
                    time.sleep(second)
                    print("== SURELY THIS WILL BE THE FINAL ATTACK FOR SURE THIS TIME I JUST KNOW IT! ==")  # TITLE
                    print(f"== fireball -{fireball}HP == zap -{zap}HP == Wack -{wack}HP ==")  # ATTACK LIST
                    print("=============================================================================================")

                if random_response2 == "== GOBLIN USES BITE AND LANDS IT! ==":
                    character -= bite
                    print("== WELL YOU WIN SOME YOU LOSE SOME ==")
                    print(f"== GOBLIN [ {goblin} HP] YOU [ {character} HP] ==")
                    print("=============================================================================================")
                    time.sleep(second)
                    print("== SURELY THIS WILL BE THE FINAL ATTACK FOR SURE THIS TIME I JUST KNOW IT! ==")  # TITLE
                    print(f"== fireball -{fireball}HP == zap -{zap}HP == Wack -{wack}HP ==")  # ATTACK LIST
                    print("=============================================================================================")
                    
                while True:
                    answer4 = input("Choose fireball, zap or wack: ").lower()
                    if answer4 == "fireball":
                        goblin -= fireball
                        time.sleep(half)
                        print (f'== A TRUE WIZARD SICKING TO HIS FIREBALL! ==') #TITLE
                        print (f'== GOBLIN [ {goblin} HP] YOU [ {character} HP] ==') #goblin and character health
                        print (f'=============================================================================================')
                    elif answer4 == "zap":
                        goblin -= zap
                        time.sleep(half)
                        print (f'== DOES HE NEED A DOCTOR OR AN ELECTROCUTION... MAYBE BOTH XD ==') #TITLE
                        print (f'== GOBLIN [ {goblin} HP] YOU [ {character} HP] ==')
                        print (f'=============================================================================================')
                    elif answer4 == "wack":
                        goblin -= wack
                        time.sleep(half)
                        print (f'== BRO IS LAUGHING AT YOU PERSONALLY I WOULD NOT TAKE THAT.... ==') #TITLE
                        print (f'== GOBLIN [ {goblin} HP] YOU [ {character} HP] ==')
                        print (f'=============================================================================================')
                    else:
                        print("Choose Fireball, Zap, Wack")
                        
                    if goblin <= 0:
                        kill_section()
                        goblin_kill()  
                        break
                
                    time.sleep(second)
                    print (f'=============================================================================================')
                    random_reponse3 = random.choice(goblin_attack3)
                    print(random_reponse3)
                    print (f'=============================================================================================')
                    time.sleep(second)

                    if random_reponse3 == "== GOBLIN USES SPIT AND MISSES! ==":
                        print ("== LOOKS LIKE YOU GET A SECOND GO FOR FREE LUCKY YOU! ==")
                        print ("== SURLY THIS WILL BE THE FINAL ATTACK FOR SURE THIS TIME I JUST KNOW IT! ==") #TITLE
                        print (f'== fireball -30HP == zap -40HP == wack -20HP ==') # ATTACK LIST
                        print (f'=============================================================================================')
                        
                    if random_reponse3 == "== GOBLIN USES SPIT AND LANDS IT ==":
                        character -= spit
                        print ("== WELL YOU WIN SOME YOU LOOSE SOME ==")
                        print (f'== GOBLIN [ {goblin} HP] YOU [ {character} HP] ==')
                        print ("== SURLY THIS WILL BE THE FINAL ATTACK FOR SURE THIS TIME I JUST KNOW IT! ==") #TITLE
                        print (f'== fireball -30HP == zap -40HP == wack -20HP ==') # ATTACK LIST
                        print (f'=============================================================================================')


                    while True:
                        answer5 = input("Choose fireball, zap or wack  : ").lower()
                        if answer5 == "fireball":
                            goblin -= fireball
                            time.sleep(half)
                            print (f'== GOOD CHOICE CANT BEAT A GOOD OLD FIREBALL! ==') #TITLE
                            print (f'== GOBLIN [ {goblin} HP] YOU [ {character} HP] ==')
                        elif answer5 == "zap":
                            goblin -= zap
                            time.sleep(half)
                            print (f'== ZAPPER MC ZAPPINGTON IMA CALL YOU FROM NOW ON! ==') #TITLE
                            print (f'== GOBLIN [ {goblin} HP] YOU [ {character} HP] ==')
                        elif answer5 == "wack":
                            goblin -= wack
                            time.sleep(half)
                            print (f'== USING WACK IS LIKE PUTTING EGGS IN THE FREEZER..... USELESS! ==') #TITLE
                            print (f'== GOBLIN [ {goblin} HP] YOU [ {character} HP] ==')
                        else:
                            print("Choose Fireball, Zap, Wack")
                            answer5 = input("choose fireball, zap or wack  : ").lower()
                        
                        if goblin <= 0:
                            kill_section()
                            goblin_kill()  
                            break
                                
                            
    #====================================================================================================================================#
main()