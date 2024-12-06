# import random
# import time
# import inspect
# second = 2
# class goblin:
#     def __init__(self, slap, bite, wack, character_health):
#         self.slap = slap
#         self.bite = bite
#         self.wack = wack
#         self.character_health = character_health


#     def use_slap(self):
#         self.character_health -= self.slap
#         print ("================================================================================================")
#         print (f'HE USES SLAP YOUR HP IS NOW {self.character_health}')
#     def use_bite(self):
#         self.character_health -= self.bite
#         print ("================================================================================================")
#         print (f'HE USES BITE YOUR HP IS NOW {self.character_health}')
#     def use_wack(self):
#         self.character_health -= self.wack
#         print ("================================================================================================")
#         print (f'HE USES WACK YOUR HP IS NOW {self.character_health}')


# goblin = goblin(slap=20, bite=30, wack=10, character_health = 100)

# attack_list = [
# goblin.use_slap, 
# goblin.use_bite, 
# goblin.use_wack
# ]

# goblin_attack_choice = random.choice(attack_list)

# goblin_attack_choice()

# if goblin_attack_choice == goblin.use_slap:
#     print("--CANT LIE THAT WAS A GOOD SHOT FROM HIM")
#     print ("================================================================================================")
#     time.sleep(second)
# elif goblin_attack_choice == goblin.use_bite:
#     print("--CANT LIE THAT WAS A GOOD SHOT FROM HIM12")
#     print ("================================================================================================")
#     time.sleep(second)
# elif goblin_attack_choice == goblin.use_wack:
#     print("--CANT LIE THAT WAS A GOOD SHOT FROM HIM123")
#     print ("================================================================================================")
#     time.sleep(second)
# elif goblin.character_health == 0:
#     print("YOU ARE DEAD! THANK YOU FOR PLAYING")











# print ("HO DO YOU CHOOSE TO ATTACK ?")
# print ("fireball -30HP -- zap -40HP -- wack - 20HP")

# answer1 = input("Choose Fireball, Zap, Wack: ").lower()

# class character:

#     def __init__(self, fireball, zap, wack, goblin_health):
#         self.fireball = fireball
#         self.zap = zap
#         self.wack = wack
#         self.goblin_health = goblin_health

#     def use_fireball(self):
#         self.goblin_health -= self.fireball
#         print ("================================================================================================")
#         print (f'YEAH THATS RIGHT MELT HIM!')
#         print(f'GOOD SHOT HE IS NOW AT {self.goblin_health}HP')
#         print ("================================================================================================")

#     def use_zap(self):
#         self.goblin_health -= self.zap
#         print ("================================================================================================")
#         print (f'BZZZZZZZZZZZZZZZZZZZZZZZZZ!!!!!')
#         print(f'GOOD SHOT HE IS NOW AT {self.goblin_health}HP')
#         print ("================================================================================================")

#     def use_wack(self):
#         self.goblin_health -= self.wack
#         print ("================================================================================================")
#         print (f'MUST HAVE A CONCUSION FROM THAT ONE FOR SURE!')
#         print (f'GOOD SHOT HE IS NOW AT {self.goblin_health}HP')
#         print ("================================================================================================")

# character = character(fireball = 30, zap = 40, wack = 20, goblin_health = 100)#
# import time
# while True:
#     if answer1 == "fireball":
#         print (character.use_fireball())
#         time.sleep
#         break
#     elif answer1 == "zap":
#         print (character.use_zap())
#         time.sleep
#         break
#     elif answer1 == "wack":
#         print (character.use_wack())
#         time.sleep
#         break
#     elif character.goblin_health == 0:
#         print ("YOU HAVE KILLED THE BEAST GOOD JOB ONTO THE NEXT!")
#         break
#     else:
#         print ("Invalid input please eneter fireball, zap or wack.")



# print ("--GOBLINS TURN NOW I WONDER WHAT HE DOES?")


# if goblin_attack_choice == goblin.use_bite:
#     print (goblin.use_bite())
# elif goblin_attack_choice == goblin.use_slap:
#     print (goblin.use_slap())
# elif goblin_attack_choice == goblin.use_wack:
#     print (goblin.use_wack())



# #List Menus



# Menu = [
#     "1.New Game"
#     "2.difficulty"
#     "3.Options"
#     "4.Exit"
# ]

# difficulty_list = [
#     "3.easy", 
#     "2.medium", 
#     "1.hard"]



# class Menu:
#     def __init__(self,main_menu, new_game, difficulty):
#         self.new_game = new_game
#         self.difficulty = None
#         self.main_menu = main_menu

#     def select_newgame(self):
#         if self.difficulty is None:
#             print ("YOU NEED TO CHOOSE A DIFFICULTY FIRST")
#         else:
#             print(f"STARTING NEW GAME / Difficulty:{self.difficulty}")

#     def select_difficulty(self):
#             main_menu = print("1.New Game\n2.Difficulty\n3.Options\n4.Exit")
#             print("CHOOSE A DIFFICULTY")
#             diffculy_menu = "1.easy\n2.medium\n3.hard"
#             while True:
#                 difficulty_answer = input("Choose an option (1,2,3): ")
#                 if difficulty_answer == "1":
#                     print("EASY MODE SELECTED")
#                     self.difficulty = "Easy"
#                     print (main_menu)
#                     break
#                     # from testing import easy
#                 elif difficulty_answer == "2":
#                     print("MEDIUM MODE SELECTED")
#                     self.difficulty = "Medium"
#                     print (main_menu)
#                     break
#                     # from testing import medium
#                 elif difficulty_answer == "3":
#                     print("HARD MODE SELECTED")
#                     self.difficulty = "Hard"
#                     print (main_menu)
#                     break
#                     # from testing import hard
#                 else:
#                     print("INVALID ANSWER TRY AGAIN!")
#                     print (diffculy_menu)


# select_exit = True

# Menu = Menu (new_game = None, difficulty = None, main_menu = "1.New Game\n2.Difficulty\n3.Options\n4.Exit")

# # print (Menu.show_main_menu())
# menu_answer = input("Choose an option (1,2,3): ").lower()
# while select_exit:
#     if menu_answer == "new game" or menu_answer == "1":
#         Menu.select_newgame()
#     elif menu_answer == "2":
#         Menu.select_difficulty()
#     elif menu_answer == "exit" or menu_answer == "3":
#         select_exit = False
#         print("QUITTING GAME...")
#     else:
#         print("PLEASE CHOOSE A VALID OPTION")







# import time
# second = 1
# class Main_Menu:
#dont need to add vairables into the (self section everytime depends on what you need to do)
    # def __init__ (self):
        #is a functions but is waiting to be assigned to something
        # self.diffficulty = None
        # self.exit = False

    # def show_main_menu(self):
        #If self.exit is False, then not self.exit becomes True, and the loop will continue running.
        # while not self.exit:
        #     print ("=====================================================================")
        #     main_menu = print("1.New Game\n2.Difficulty\n3.Exit")
        #     print ("=====================================================================")
        #     answer1 = input("Please select an option: ").lower()
        #     if answer1 == "difficulty" or answer1 == "2":
        #         self.show_difficulty()
        #         time.sleep(second)
        #     elif answer1 == "new game" or answer1 == "1":
        #         if self.diffficulty is None:
        #             print ("-- YOU NEED TO SELECT A DIFFICULTY FIRST --")
        #             time.sleep(second)
        #         else:
        #             print (F"-- STARTING NEW GAME IN {self.diffficulty} MODE!")
        #             # from testing import easy
        #             time.sleep(second)
        #             break
        #     elif answer1 == "exit" or answer1 == "3":
        #         self.exit = True
        #         print ("-- EXITING GAME -- ")
        #         time.sleep(second)
        #         break
        #     else:
        #         print("-- Invalid Answer Try Again --")
        #         time.sleep(second)
        #         self.show_main_menu()
            
            


    # def show_difficulty(self):
    #     print("CHOOSE A DIFFICULTY")
    #     diffculy_menu = "1.easy\n2.medium\n3.hard"
    #     print (diffculy_menu)
    #     self.diffficulty = None
    #     while True:
    #         answer2 = input("Please Select a Difficulty: ").lower()
    #         if answer2 == "easy" or answer2 == "1":
    #             print ("-- EASY MODE SELECTED --")
    #             self.diffficulty = "Easy"
    #             time.sleep(second)
    #             break
    #         elif answer2 == "medium" or answer2 == "2":
    #             print("-- MEDIUM MODE SELECTED --")
    #             self.diffficulty = "medium"
    #             time.sleep(second)
    #             break
            #do not incluse self.show_main_menu to return it will do it on its own just needs a break
            # elif answer2 == "hard" or answer2 == "3":
            #     print ("-- HARD MODE SELECTED")
            #     self.diffficulty = "hard"
            #     time.sleep(second)
            #     break
            # else:
            #     print ("Invalid option please select a difficulty.")
            #     time.sleep(second)

#You need to do this to print the variable outside the class
# menu = Main_Menu()
# menu.show_main_menu()



#health system
# def changehealth(currenthealth, healthchangeamount):
#     if healthchangeamount > 0:
#         currenthealth += healthchangeamount
#         print(f"Your health has increased by {healthchangeamount} and is now {currenthealth}")
#     elif healthchangeamount < 0:
#         currenthealth += healthchangeamount
#         print(f"Your health has decreased by {healthchangeamount} and is now {currenthealth}")
#     else:
#         print(f"Your health has not changed. You currently have {currenthealth} health")
#     return currenthealth

# currenthealth = int(100)
# healthchangeamount = int(-20)

# currenthealth = changehealth(currenthealth, healthchangeamount)

# healthchangeamount = int(40)

# currenthealth  = changehealth(currenthealth,healthchangeamount)
# from goto import with_goto, label, goto
# @with_goto
# def skipping():
#     text = "CONRGATULATIONS YOU WIN!"
#     if text == "CONGRATULATIONS YOU WIN!":
        
        
        
        
        
        
        
        
# # print ("you have encoutered a shrine!")
# from GORLOCKFIGHTING import kill_section1

# kill = kill_section1()

# goblin_hp = 20
# fireball = 20

# def goblin_kill_section():
#     if goblin_hp <= 0:
#         kill.show_kill_section1()

# print ("next on the attack")
# print ("choose fireball")
# answer = input("choose:").lower()


# if answer == "fireball":
#     goblin_hp -= fireball
#     print (f"goblin hp is now {goblin_hp}HP and you are now at 100HP")
#     goblin_kill_section()



# def goblin_kill_section():
#     if goblin <= 0:
#         kill.show_kill_section1()

# class character2:
#     def __init__(self, hp):
#         self.hp = hp
        
# player = character2(hp = 100)
        
# class goblin_health:
#     def __init__(self, ghp):
#         self.ghp = ghp
        
# attacker = goblin_health(ghp = 100)


# def boss_starting():
#     from gorlockv1 import kill_section1
#     kill = kill_section1()
#     kill.show_kill_section1()
    
# def goblin_kill():
#     if goblin <= 0:
#         boss_starting()
    
# def goblin_kill():
#     if goblin <= 0:
#         kill = kill_section1
#         kill.show_kill_section1()
    

# def over_hp():
#     global character

# def goblin_kill():
#     if goblin <= 0:
#         print (f'=============================================================================================')
#         time.sleep(second)
#         print (f'-- AMAZING YOU HAVE ENCOUNTERED A SHRINE BUFF ADDED')
#         time.sleep(second)
#         character += 25
#         print (f'-- +25HPP HAS BEEN ADDED YOU NOW HAVE {character}')
#         time.sleep(second)
#         print ("-- ONTO THE FINAL BOSS LEVEL ALL YOUR TRAINING HAS LEAD UP TO THIS!")
#         print (f'=============================================================================================')
#         time.sleep(second3)
#         print ("-- NEW ATTACK LEARNED ROLLING THUNDER")
#         print ("-- This attack that stuns the enemy for one round and allows you to land 2 attacks without getting hit. You can only use this once every other round.")

#         print (f'======================================================================================================================================================')
#         print ("-- ENTERING THE DUNGEON GORLOCK THE DESTROYER")
#         print (f'=============================================================================================')
#         #shrine healed +10 entering boss fight with gorlock
#         gorlock_the_destroyer = 100

#         #player attacks
#         fireball = 30
#         zap = 40
#         wack =20
#         rolling_thunder = 50

#         #gorlovk attacks
#         poke = 20
#         body_slam =  30
#         Electric_Hammer = 35
#         Hammer_swing = 30


#         #first attack
#         print (f'=============================================================================================')
#         print ("-- YOU FIRST WHICH ATTACK WILL YOU CHOOSE?")
#         print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
#         print ("-- fireball -30HP == zap -40HP == Wack -20HP == rolling thunder -50HP")
#         print (f'=============================================================================================')
#         while True:
#             gorlock_answer = input("Choose Fireball, Zap, Wack: ").lower()
#             if gorlock_answer == "fireball":
#                 gorlock_the_destroyer -= fireball
#                 print (f'=============================================================================================')
#                 print("-- OOOOO BOSS MAN IS FEELING THAT ONE LOOK AT HIM STUMBLE!")
#                 print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
#                 print (f'=============================================================================================')
#                 break
#             elif gorlock_answer == "zap":
#                 gorlock_the_destroyer -= zap
#                 print (f'=============================================================================================')
#                 print("-- OOOOO BOSS MAN IS FEELING THAT ONE LOOK AT HIM STUMBLE!")
#                 print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
#                 print (f'=============================================================================================')
#                 break
#             elif gorlock_answer == "wack":
#                 gorlock_the_destroyer -= wack
#                 print (f'=============================================================================================')
#                 print("-- OOOOO BOSS MAN IS FEELING THAT ONE LOOK AT HIM STUMBLE!")
#                 print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
#                 print (f'=============================================================================================')
#                 break
#             elif gorlock_answer == "rolling thunder":
#                 gorlock_the_destroyer -= rolling_thunder
#                 print (f'=============================================================================================')
#                 print("-- OOOOO BOSS MAN IS FEELING THAT ONE LOOK AT HIM STUMBLE!")
#                 print (f'GOBLIN [ {gorlock_the_destroyer} HP] YOU [ {character} HP]') 
#                 print (f'=============================================================================================')
#                 break
#             else:
#                 print ("Invalid move! Please choose from: fireball, zap, wack, rolling thunder.")


import random
import time

Rogue = 100

poision_purge = 35
infect = 20
poision_rain = 30

attack_description ={}

xyrif = 100

light_beam = 30
anitmatter_pulse = 20
punch = 10

def kill_section2():
    print("== GOBLIN IS DEAD! GOOD JOB ONTO THE NEXT ROOM. ==")

xyrif_random_attacks = [
    f"== HE USES LIGHT BEAM AND LANDS IT! ==",
    f"== HE USES LIGHT BEAM AND MISSES! ==",
    f"== XYRIF ATTACKS WITH ANITMATTER PULSE AND LANDS IT!",
    f"== XYRIF ATTACKS WITH ANITMATTER PULSE AND MISSES, LUCKY YOU! ==",
    f"== HE PUNCHES YOU AND LANDS IT, UNLUCKY! ==",
    f"== HE PUNCHES YOU AND MISSES, WE WILL COUNT THAT ONE AS A WIN! =="
]

def xyrif_attack_func():
        global Rogue
        xyrif2 = random.choice(xyrif_random_attacks)
        print(xyrif2)
        if xyrif_random_attacks == "HE USES LIGHT BEAM AND LANDS IT!":
            Rogue -= 30
            print (f"== XYRIF HAS {xyrif}HP | YOU ARE AT {Rogue}HP ==")
        elif xyrif_random_attacks == "== XYRIF ATTACKS WITH ANITMATTER PULSE AND LANDS IT! ==":
            rogue -= 20
            print (f"== XYRIF HAS {xyrif}HP | YOU ARE AT {Rogue}HP ==")
        elif xyrif_random_attacks == "== HE PUNCHES YOU AND LANDS IT, UNLUCKY! ==":
            Rogue -= 10
            print (f"== XYRIF HAS {xyrif}HP | YOU ARE AT {Rogue}HP ==")
        else:
            if xyrif_random_attacks == "== HE USES LIGHT BEAM AND MISSES! ==" or "== XYRIF ATTACKS WITH ANITMATTER PULSE AND MISSES, LUCKY YOU! ==" or "== HE PUNCHES YOU AND LANDS IT, UNLUCKY! ==":
                print (f"== XYRIF HAS {xyrif}HP | YOU ARE AT {Rogue}HP ==")
                
xyrif_attack_func()