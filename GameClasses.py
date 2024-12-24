import random
class GameVariables:
    # Frostwraith 
    ice_shard_barrage = 2
    frozen_grasp = 4
    blizzard_veil = 3
    # Bloodreaver 
    blood_frenzy = 2
    lifedrain_slash = 4
    bloodlust_roar = 3
    # Voidstalker 
    shadowstep = 2
    ethereal_strike = 4
    void_rift = 3
    # Plaguespitter 
    toxic_spit = 5
    pestilence_cloud = 4
    viral_burst = 6
    
    varnyx_the_shardwoven = 100
    fractured_rift = 20
    prismatic_overload = 10
    shardstorm_barrage = 15
    resonant_collapse = 25

    chosen_hp = []
    enemycreation = []
    enemy_count = random.randint(2,4)
    chosen_names = []
    name_list = ["FROST WRAITH", "BLOOD REAVER", "VOID STALKER", "PLAGUE SPITTER"]
    frostwraith_attack_list = [ice_shard_barrage, frozen_grasp, blizzard_veil]
    bloodreaver_attack_list = [blood_frenzy, lifedrain_slash, bloodlust_roar]
    voidstalker_attack_list = [shadowstep, ethereal_strike, void_rift]
    plaguespitter_attack_list = [toxic_spit, pestilence_cloud, viral_burst]
    
    Warrior = 170

    shield_bash = 10
    raging_strike = 15
    whirlwind_slash = 5

class Menu():
    def __init__(self):
        self.difficulty = None
    def NewGame(self):
        if self.difficulty is not None:
            print(F"== STARTING GAME IN {self.difficulty} MODE ==")
        else:
            print("== PLEASE CHOOSE A DIFFICULTY ==")
            self.Difficulty_Selection()
        
    def Difficulty_Selection(self):
        import time
        print("\n--- Difficulty ---")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        
        Choice = input("Choose Option > ")
        if Choice == "1":
            self.difficulty = "EASY"
            time.sleep(1.4)
            self.NewGame()
        elif Choice == "2":
            #frostwraith
            GameVariables.ice_shard_barrage +=2
            GameVariables.frozen_grasp += 2
            GameVariables.blizzard_veil += 2
            # BloodReaver
            GameVariables.blood_frenzy += 2
            GameVariables.lifedrain_slash += 2
            GameVariables.bloodlust_roar += 2
            # VoidStalker
            GameVariables.shadowstep += 2
            GameVariables.ethereal_strike += 2
            GameVariables.void_rift += 2
            #PlagueSpitter
            GameVariables.toxic_spit+= 2
            GameVariables.pestilence_cloud+= 2
            GameVariables.viral_burst += 2

            GameVariables.shield_bash -= 5
            GameVariables.raging_strike -= 5
            GameVariables.whirlwind_slash -= 5
            self.difficulty = "MEDIUM"
            print("== ENEMY ATTACKS HAVE BEEN INCREASED BY 2! ==\n== YOUR ATTACKS HAVE BEEN DECREASED BY 5! ==")
            time.sleep(1.4)
            self.NewGame()
        elif Choice == "3":
            #frostwraith
            GameVariables.ice_shard_barrage +=5
            GameVariables.frozen_grasp += 5
            GameVariables.blizzard_veil += 5
            # BloodReaver
            GameVariables.blood_frenzy += 5
            GameVariables.lifedrain_slash += 5
            GameVariables.bloodlust_roar += 5
            # VoidStalker
            GameVariables.shadowstep += 5
            GameVariables.ethereal_strike += 5
            GameVariables.void_rift += 5
            #PlagueSpitter
            GameVariables.toxic_spit+= 5
            GameVariables.pestilence_cloud+= 5
            GameVariables.viral_burst += 5

            GameVariables.shield_bash += 7
            GameVariables.raging_strike += 7
            GameVariables.whirlwind_slash = 7
            self.difficulty = "HARD"
            print("== ENEMY ATTACKS HAVE BEEN INCREASED BY 5! ==\n== YOUR ATTACKS HAVE BEEN DECREASED BY 7! ==")
            time.sleep(1.4)
            self.NewGame()
            

class Enemies():
    def __init__(self, health , name, min_enemies, max_enemies):
        self.name = name
        self.health = health
        self.min_enemies = min_enemies
        self.max_enemies = max_enemies
        
        
    def bossfight(self):
        import time
    #     global GameVariables
    #     from Gamelists import buff_list
    #     if GameVariables.varnyx_the_shardwoven <= 0:                    
    #         time.sleep(1)
    #         #playing boss room
    #         print ("== ONTO THE FINAL BOSS LEVEL ALL YOUR TRAINING HAS LEAD UP TO THIS! ==")
    #         print (f'=============================================================================================')
    #         time.sleep(3)
    #         #announcing a new attack that the character learns
    #         print ("== NEW ATTACK LEARNED SOUL BURST ==")
    #         print ("== IF YOU WOULD LIKE MORE DETAILS ON THE ATTACK TYPE MOVES :) ==")
    #         time.sleep(1)
            
    #         #boss room entrance
    #         print (f'=============================================================================================')
    #         print ("== ENTERING THE DUNGEON WITH THE TEMPEST GUARDIAN ==")
    #         print (f'=============================================================================================')
                
    #         time.sleep(1)
    #         while GameVariables.varnyx_the_shardwoven > 0:
    #             if not stored_response:
    #                 last_response = (random.choice(response_list2))
    #                 print (last_response)
    #             else:
    #                 print(stored_response)
    #                 stored_response = None
    #             print (f"== TEMPEST GUARDIAN HAS {tempest_guardian}HP | YOU ARE AT {rogue}HP ==")
    #             print (f'=============================================================================================')   
    #             answer = input("Choose Attack > ").lower()
    #             if answer in attack_description:
    #                 print(attack_description[answer])
    #                 stored_response = last_response
    #                 continue
            
    #             last_response = None
    #             if answer == "a":
    #                 print (f'=============================================================================================')   
    #                 print (random.choice(poison_attack_purge))
    #                 xyrif -= 35
    #                 print(f"== TEMPEST GUARDIAN HAS {tempest_guardian}HP | YOU ARE AT {rogue}HP ==")
    #                 print (f'=============================================================================================')   
    #                 time.sleep(1)
    #                 Boss_attack_func()
    #                 print (f'=============================================================================================')   
    #             elif answer == "b":
    #                 print (f'=============================================================================================')  
    #                 print (random.choice(infect_attack))
    #                 xyrif -= 20
    #                 print(f"== TEMPEST GUARDIAN HAS {tempest_guardian}HP | YOU ARE AT {rogue}HP ==")
    #                 print (f'=============================================================================================')  
    #                 time.sleep(1)
    #                 Boss_attack_func()
    #                 print (f'=============================================================================================')  
    #             elif answer == "c":
    #                 xyrif -= 30
    #                 print (f'=============================================================================================')  
    #                 print (random.choice(poison_rain_attack))
    #                 print(f"== TEMPEST GUARDIAN HAS {tempest_guardian}HP | YOU ARE AT {rogue}HP ==")
    #                 print (f'=============================================================================================')  
    #                 time.sleep(1)
    #                 Boss_attack_func()
    #                 print (f'=============================================================================================')
    #             elif answer == "d":
    #                 xyrif -= 40
    #                 print (f'=============================================================================================')  
    #                 print (random.choice(soul_burst_attack))
    #                 print(f"== TEMPEST GUARDIAN HAS {tempest_guardian}HP | YOU ARE AT {rogue}HP ==")
    #                 print (f'=============================================================================================')  
    #                 time.sleep(1)
    #                 Boss_attack_func()
    #                 print (f'=============================================================================================') 
    #             else:
    #                 if answer:
    #                     print (f'=============================================================================================')  
    #                     print("== INVALID INPUT, PLEASE CHOOSE AN ATTACK! ==")
    #                     print (f'=============================================================================================')  
                    
    #         if tempest_guardian < 0:
    #             show_ending_section()
    #         elif rogue < 0:
    #             show_charcter_Death()
    
    def enemys_attack_func(self):
        from Gamelists import frostwraith_attack_list, bloodreaver_attack_list, voidstalker_attack_list, plaguespitter_attack_list
        which_enemy_attacks = random.choice(GameVariables.chosen_names)
        print(f"== {which_enemy_attacks} IS ATTACKING")
        if which_enemy_attacks == "FROST WRAITH":
            frostwraith_attack = random.choice(frostwraith_attack_list)
            print(frostwraith_attack)
            if frostwraith_attack == "== FROST WRAITH HAS USED ICE SHARD BARRAGE AND LANDS IT ==":
                GameVariables.Warrior -= GameVariables.ice_shard_barrage
            elif frostwraith_attack == "== FROST WRAITH HAS USED FROZEN GRASP AND LANDS IT ==":
                GameVariables.Warrior -= GameVariables.frozen_grasp
            elif frostwraith_attack == "== FROST WRAITH HAS USED BLIZZARD VEIL AND LANDS IT ==":
                GameVariables.Warrior -= GameVariables.blizzard_veil
            else:
                print("== LETS JUST BE GREATFULL HE MISSED! ==")
        elif which_enemy_attacks == "BLOOD REAVER":
            bloodreaver_attack = random.choice(bloodreaver_attack_list)
            print(bloodreaver_attack)
            if bloodreaver_attack == "== BLOOD REAVER HAS USED BLOOD FRENZY AND LANDS IT ==":
                GameVariables.Warrior -= GameVariables.blood_frenzy
            elif bloodreaver_attack == "== BLOOD REAVER HAS USED BLOOD FRENZY AND LANDS IT ==":
                GameVariables.Warrior -= GameVariables.lifedrain_slash
            elif bloodreaver_attack == "== BLOOD REAVER HAS USED BLOOD FRENZY AND LANDS IT ==":
                GameVariables.Warrior -= GameVariables.bloodlust_roar
            else:
                print("== LETS ALL BE GREATFULL HE MISSED! ==")
        elif which_enemy_attacks == "VOID STALKER":
            voidstalker_attack = random.choice(voidstalker_attack_list)
            print(voidstalker_attack)
            if voidstalker_attack == "== VOID STALKER HAS USED SHADOW STEP AND LANDS IT ==":
                GameVariables.Warrior -= GameVariables.shadowstep
            elif voidstalker_attack == "== VOID STALKER HAS USED ETHERNAL STRIKE AND LANDS IT ==":
                GameVariables.Warrior -= GameVariables.ethereal_strike
            elif voidstalker_attack == "== VOID STALKER HAS USED VOID RIFT AND LANDS IT ==":
                GameVariables.Warrior -= GameVariables.void_rift
            else:
                print("== LETS ALL BE GREATFUL HE MISSED! ==")
        elif which_enemy_attacks == "PLAGUE SPITTER":
            plaguespitter_attack = random.choice(plaguespitter_attack_list)
            print(plaguespitter_attack)
            if plaguespitter_attack == "== PLAGUE SPITTER HAS USED TOXIC SPIT AND LANDS IT ==":\
                GameVariables.Warrior -= GameVariables.toxic_spit
            elif plaguespitter_attack == "== PLAGUE SPITTER HAS USED PESTILANCE CLOUD AND LANDS IT ==":
                GameVariables.Warrior -= GameVariables.pestilence_cloud
            elif plaguespitter_attack == "== PLAGUE SPITTER HAS USED VIRAL BURST AND LANDS IT ==":
                GameVariables.Warrior -= GameVariables.viral_burst
            else:
                print("== WE CAN ALL BE GREATFUL HE MISSED! ==")
                
    def Spawner(self):
        import random
        print (f"== {GameVariables.enemy_count} ENEMIES HAS SPAWNED! ==")
        for _ in range(GameVariables.enemy_count):
            self.name = random.choice(GameVariables.name_list)
            GameVariables.name_list.remove(self.name)
            GameVariables.chosen_names.append(self.name)
            self.health = random.randint(20, 40)
            creationtext = f"== NAME: {self.name} HP: {self.health} =="
            GameVariables.chosen_hp.append(self.health)
            while GameVariables.enemycreation != GameVariables.enemy_count:
                print(creationtext)
                GameVariables.enemycreation.append(creationtext)
            else:
                if GameVariables.enemycreation == GameVariables.enemy_count:
                    continue

    def EnemyAttack(self):
        from Gamelists import shield_bash_response ,raging_strike_response, whirlwind_slash_response
        import random
        from GameFunctions import kill_section3, show_charcter_Death, EnemyMenu
        print("== STARTING ROUND ==")
        print("== WHO DO YOU WANT TO ATTACK ==")
        while any(hp > 0 for hp in GameVariables.chosen_hp):
            EnemyMenu()
            answer = input("Choose Enemy > ").lower()
            if answer == "1":
                print(f"== YOU CHOSE TO ATTACK {GameVariables.chosen_names[0]} ==")
                print(f"== HOW WILL YOU ATTACK ==\n Name: {GameVariables.chosen_names[0]} HP: {GameVariables.chosen_hp[0]} ==")
                print(f"== Choose Shield Bash - {GameVariables.shield_bash}Dmg - Raging Strike {GameVariables.shield_bash}Dmg - Whirlwind Strike {GameVariables.whirlwind_slash}Dmg ==")
                attack_answer = input("Choose Atack > ")
                if attack_answer == "shield bash":
                    GameVariables.chosen_hp[0] -= 10
                    shield_bash_print = random.shuffle(shield_bash_response)
                    print(shield_bash_print)
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                elif attack_answer == "raging strike":
                    GameVariables.chosen_hp[0] -= 15
                    raging_strike_print = random.shuffle(raging_strike_response)
                    print(raging_strike_print)
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                elif attack_answer == "whirlwind strike":
                    GameVariables.chosen_hp[0] -= 5
                    whirlwind_strike_print = random.shuffle(whirlwind_slash_response)
                    print(whirlwind_strike_print)
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                else:
                    print("== PLEASE ENTER A VALID INPUT ==")
            elif answer == "2":
                print(f"== YOU CHOSE TO ATTACK {GameVariables.chosen_names[1]} ==")
                print(f"== HOW WILL YOU ATTACK ==\n Name: {GameVariables.chosen_names[1]} HP: {GameVariables.chosen_hp[1]} ==")
                print(f"== Choose Shield Bash - {GameVariables.shield_bash}Dmg - Raging Strike {GameVariables.shield_bash}Dmg - Whirlwind Strike {GameVariables.whirlwind_slash}Dmg ==")
                attack_answer = input("Choose Atack > ")
                if attack_answer == "shield bash":
                    GameVariables.chosen_hp[1] -= 10
                    shield_bash_print = random.shuffle(shield_bash_response)
                    print(shield_bash_print)
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                elif attack_answer == "raging strike":
                    GameVariables.chosen_hp[1] -= 15
                    raging_strike_print = random.shuffle(raging_strike_response)
                    print(raging_strike_print)
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                elif attack_answer == "whirlwind strike":
                    GameVariables.chosen_hp[1] -= 5
                    whirlwind_strike_print = random.shuffle(whirlwind_slash_response)
                    print(whirlwind_strike_print)
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                else:
                    print("== PLEASE ENTER A VALID INPUT ==")
            elif answer == "3":
                print(f"== YOU CHOSE TO ATTACK {GameVariables.chosen_names[2]} ==")
                print(f"== HOW WILL YOU ATTACK ==\n Name: {GameVariables.chosen_names[2]} HP: {GameVariables.chosen_hp[2]} ==")
                print(f"== Choose Shield Bash - {GameVariables.shield_bash}Dmg - Raging Strike {GameVariables.shield_bash}Dmg - Whirlwind Strike {GameVariables.whirlwind_slash}Dmg ==")
                attack_answer = input("Choose Atack > ")
                if attack_answer == "shield bash":
                    GameVariables.chosen_hp[2] -= 10
                    shield_bash_print = random.shuffle(shield_bash_response)
                    print(shield_bash_print)
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                elif attack_answer == "raging strike":
                    GameVariables.chosen_hp[2] -= 15
                    raging_strike_print = random.shuffle(raging_strike_response)
                    print(raging_strike_print)
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                elif attack_answer == "whirlwind strike":
                    GameVariables.chosen_hp[2] -= 5
                    whirlwind_strike_print = random.shuffle(whirlwind_slash_response)
                    print(whirlwind_strike_print)
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                else:
                    print("== PLEASE ENTER A VALID INPUT ==")
            elif answer == "4":
                print(f"== YOU CHOSE TO ATTACK {GameVariables.chosen_names[3]} ==")
                print(f"== HOW WILL YOU ATTACK ==\n Name: {GameVariables.chosen_names[3]} HP: {GameVariables.chosen_hp[3]} ==")
                print(f"== Choose Shield Bash - {GameVariables.shield_bash}Dmg - Raging Strike {GameVariables.shield_bash}Dmg - Whirlwind Strike {GameVariables.whirlwind_slash}Dmg ==")
                attack_answer = input("Choose Atack > ")
                if attack_answer == "shield bash":
                    GameVariables.chosen_hp[3] -= 10
                    shield_bash_print = random.shuffle(shield_bash_response)
                    print(shield_bash_print)
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                elif attack_answer == "raging strike":
                    GameVariables.chosen_hp[3] -= 15
                    raging_strike_print = random.shuffle(raging_strike_response)
                    print(raging_strike_print)
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                elif attack_answer == "whirlwind strike":
                    GameVariables.chosen_hp[3] -= 5
                    whirlwind_strike_print = random.shuffle(whirlwind_slash_response)
                    print(whirlwind_strike_print)
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                else:
                    print("== PLEASE ENTER A VALID INPUT ==")
            else:
                print("== PLEASE TYPE A VALID INPUT :) ==")
                        
            if not all(x == 0 for x in GameVariables.chosen_hp):
                kill_section3()
                break
            elif GameVariables.Warrior <= 0:
                show_charcter_Death()
                break
                        
            
test = Enemies(0, "", 4, 2)
import time
test.Spawner()
test.EnemyAttack()

def Start():
    menu = Menu()
    print("\n--- Main Menu ---")
    print("1. New Game")
    print("2. Difficulty")
    print("3. Exit Game")   

    Menu_Input = input("Choose Option > ")

    if Menu_Input == "1":
        menu.NewGame()
    elif Menu_Input == "2":
        menu.Difficulty_Selection()
    elif Menu_Input == "3":
        print("== QUITTING THE GAME ==")
    else:
        print("== Please Choose an Option ==")