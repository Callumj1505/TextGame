import random, time
from Gamelists import shield_bash_response ,raging_strike_response, whirlwind_slash_response, frostwraith_attack_list, bloodreaver_attack_list, voidstalker_attack_list, plaguespitter_attack_list, buff_list, chest_buffw,response_list3, varnyx_attack_list,spectral_blade_response,attack_description2,attack_list1,attack_list2,attack_list3,attack_list4,attack_list5,attack_list6
from GameFunctions import kill_section3, show_charcter_Death, show_ending_section, kill_section
from colorama import Style, Fore
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
    
    
    #Boss - varnyx_the_shardwoven    
    varnyx_the_shardwoven = 100
    fractured_rift = 20
    prismatic_overload = 10
    shardstorm_barrage = 15
    resonant_collapse = 25
    
    score = 0
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
    spectral_blade = 20

class Menu():
    def __init__(self):
        self.difficulty = None
    #this handles when the game starts
    def NewGame(self):
        if self.difficulty is not None:
            print(F"== STARTING GAME IN {self.difficulty} MODE ==")
            menu = Enemies(0, "", 4, 2)
            menu.Spawner()
            menu.EnemyAttack()
        else:
            print("== PLEASE CHOOSE A DIFFICULTY ==")
            self.Difficulty_Selection()
    #scoreboard for players to see there score
    def Scoreboard(self):
            with open(r'C:\Users\callu\Desktop\coding\game\score.txt', 'r') as file:
                score = file.read()
                print(score)
    #difficulty selection for the player
    def Difficulty_Selection(self):
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

#this class handles the enemies and the boss fight
class Enemies():
    def __init__(self, health, name, min_enemies, max_enemies):
        self.name = name
        self.health = health
        self.min_enemies = min_enemies
        self.max_enemies = max_enemies
#this function handles the boss fight
    def bossfight(self):
        from WizardP1 import answer2, charanswer
        if answer2 == "a" and charanswer == "c":
            print (f'=============================================================================================')
            time.sleep(1)
            print (f'== AMAZING YOU HAVE ENCOUNTERED A SHRINE A BUFF OR DEBUFF COULD BE ADDED LETS HOPE WE GET LUCKY! ==')
            time.sleep(1)
            random_buff = random.choice(buff_list)
            print(random_buff)
            if random_buff == "+25HP":
                GameVariables.Warrior += 25
                print (f"== YOU HAVE RECEIVED A HEALTH BONUS OF 25HP YOUR HP IS NOW {GameVariables.Warrior} ==")
                print (f'=============================================================================================')
            elif random_buff == "+10ATK":
                GameVariables.shield_bash += 5
                GameVariables.raging_strike += 5
                GameVariables.whirlwind_slash += 5
                GameVariables.spectral_blade += 5
                print ("YOU HAVE GOT AN ATTACK BUFF OF 10 ALL YOUR ATTACKS DO 5 MORE DAMAGE == ")
                print (f'=============================================================================================')
            elif random_buff == "-10HP":
                GameVariables.Warrior -= 10
                print(f"== YOU HAVE BEEN GIVEN A DEBUFF OF -10HP YOU ARE NOW AT {GameVariables.Warrior}")
                print (f'=============================================================================================')
            elif random_buff == "-10ATK":
                GameVariables.shield_bash -= 5
                GameVariables.raging_strike -= 5
                GameVariables.whirlwind_slash -= 5
                GameVariables.spectral_blade -= 5
                print("== YOU HAVE BEEN GIVEN A DEBUFF YOU NOW HAVE -10ATK ALL ATTACKS TO 5 LESS DAMAGE ==")
                print (f'=============================================================================================')
        elif answer2 == "b" and charanswer == "c":
            print (f'=============================================================================================')
            print("== YOU HAVE ENCOUNTERED A HEALING TOKEN +30 HP! ==")
            GameVariables.Warrior += 30
            print(f"== YOUR HP IS NOW {GameVariables.Warrior} ==")
            print (f'=============================================================================================')
        elif answer2 == "c" and charanswer == "c":
            print (f'=============================================================================================')
            print("== YOU HAVE BUMPED INTO A CHEST AND FIND A NEW PEICE OF EQUIPMENT! ==")
            chest_buff1 = random.choice(chest_buffw)
            print(chest_buff1)
            print (f'=============================================================================================')
            if chest_buff1 == "== YOU HAVE RECEIVED A NEW PEACE OF CHEST ARMOR WITH +10 ARMOR! ==":
                GameVariables.fractured_rift -= 5
                GameVariables.prismatic_overload -= 5
                GameVariables.shardstorm_barrage -= 5
                GameVariables.resonant_collapse -= 5
                print("== ALL ENEMY DAMAGE IS DECREASED BY FIVE ==")
                print (f'=============================================================================================')
            elif chest_buff1 == "== YOU HAVE RECEIVED NEW LONG SWORD! +3 ARMOR PHYSICAL DAMAGE! ==":
                GameVariables.shield_bash += 3
                GameVariables.raging_strike += 3
                GameVariables.whirlwind_slash += 3
                GameVariables.spectral_blade += 3
                print("== ALL OF YOUR ATTACKS HAS GAINED +5 ATTACK")
                print (f'=============================================================================================')
            elif chest_buff1 == "== YOU HAVE RECIEVED A METAL LEGGINGS +10 HEALTH ==":
                GameVariables.Warrior += 10
                print ("== YOU HAVE +10 HEALTH WOOP WOOP == ")
                print (f'=============================================================================================')
        print ("== NEW ATTACK LEARNED SPECTRAL BLADE ==")
        print ("== IF YOU WOULD LIKE MORE DETAILS ON THE ATTACK TYPE 'MOVES' :) ==")
        print ("== ENTERING THE FINAL BOSS FIGHT ==")
        print ("== YOU ATTACK FIRST WHAT WILL YOU CHOOSE? ==")
        print (f'=============================================================================================')
        while True:
            response = random.choice(response_list3)
            print (f'=============================================================================================')
            print(response)
            print (f'=============================================================================================')
            response_list3.pop(response)
            print(f"== VARNYX HP: {GameVariables.varnyx_the_shardwoven} WARRIOR HP: {GameVariables.Warrior} ==")
            Warrior_attack = input("Choose Attack [A, B, C, D] > ").lower()
            if Warrior_attack == "a":
                GameVariables.varnyx_the_shardwoven -= GameVariables.shield_bash
                sb_attack = random.choice(shield_bash_response)
                print(sb_attack)
                print (f'=============================================================================================')
                shield_bash_response.pop(sb_attack)
                GameVariables.score += random.randint(2,7)
                self.Boss_Attack()
                print (f'=============================================================================================')
            elif Warrior_attack == "b":
                GameVariables.varnyx_the_shardwoven -= GameVariables.raging_strike
                rs_attack = random.choice(raging_strike_response)
                print(rs_attack)
                print (f'=============================================================================================')
                raging_strike_response.pop(rs_attack)
                GameVariables.score += random.randint(2,7)
                self.Boss_Attack()
                print (f'=============================================================================================')
            elif Warrior_attack == "c":
                GameVariables.varnyx_the_shardwoven -= GameVariables.whirlwind_slash
                ws_attack = random.choice(whirlwind_slash_response)
                print(ws_attack)
                print (f'=============================================================================================')
                whirlwind_slash_response.pop(ws_attack)
                GameVariables.score += random.randint(2,7)
                self.Boss_Attack()
                print (f'=============================================================================================')
            elif Warrior_attack == "d":
                GameVariables.varnyx_the_shardwoven -= GameVariables.spectral_blade
                sb2_attack = random.choice(spectral_blade_response)
                print(sb2_attack)
                print (f'=============================================================================================')
                spectral_blade_response.pop(sb2_attack)
                GameVariables.score += random.randint(2,7)
                self.Boss_Attack()
                print (f'=============================================================================================')
            else:
                print("== PLEASE ENTER A VALID INPUT ==")
                Warrior_attack = input("Choose Attack [A, B, C, D] > ").lower() 
                
            if GameVariables.varnyx_the_shardwoven <= 0:
                kill_section()
                print (f'=============================================================================================')
                show_ending_section()
                print (f'=============================================================================================')
            elif GameVariables.Warrior <= 0:
                print (f'=============================================================================================')
                show_charcter_Death()
                print (f'=============================================================================================')
#this function handles the enemies attacks
    def Boss_Attack(self):
        print (f'=============================================================================================')
        print("== VARNYX THE SHARDWOVEN IS ATTACKING ==")
        boss_attack = random.choice(varnyx_attack_list)
        print(boss_attack)
        print (f'=============================================================================================')
        if boss_attack == "== VARNYX THE SHARDWOVEN HAS USED FRACTURED RIFT AND LANDS IT ==":
            GameVariables.Warrior -= GameVariables.fractured_rift
            print(f"== VARNYX HP: {GameVariables.varnyx_the_shardwoven} WARRIOR HP: {GameVariables.Warrior} ==")
        elif boss_attack == "== VARNYX THE SHARDWOVEN HAS USED PRISMATIC OVERLOAD AND LANDS IT ==":
            GameVariables.Warrior -= GameVariables.prismatic_overload
            print(f"== VARNYX HP: {GameVariables.varnyx_the_shardwoven} WARRIOR HP: {GameVariables.Warrior} ==")
        elif boss_attack == "== VARNYX THE SHARDWOVEN HAS USED SHARDSTORM BARRAGE AND LANDS IT ==":
            GameVariables.Warrior -= GameVariables.shardstorm_barrage
            print(f"== VARNYX HP: {GameVariables.varnyx_the_shardwoven} WARRIOR HP: {GameVariables.Warrior} ==")
        elif boss_attack == "== VARNYX THE SHARDWOVEN HAS USED RESONANT COLLAPSE AND LANDS IT ==":
            GameVariables.Warrior -= GameVariables.resonant_collapse
            print(f"== VARNYX HP: {GameVariables.varnyx_the_shardwoven} WARRIOR HP: {GameVariables.Warrior} ==")
        else:
            print("== VARNYX THE SHARDWOVEN MISSED HIS ATTACK ==")
#this function handles the enemies attacks
    def enemys_attack_func(self):
        which_enemy_attacks = random.choice(GameVariables.chosen_names)
        print (f'=============================================================================================')
        print(f"== {which_enemy_attacks} IS ATTACKING")
        if which_enemy_attacks == "FROST WRAITH":
            frostwraith_attack = random.choice(frostwraith_attack_list)
            print(frostwraith_attack)
            print (f'=============================================================================================')
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
            elif bloodreaver_attack == "== BLOOD REAVER HAS USED LIFEDRAIN SLASH AND LANDS IT ==":
                GameVariables.Warrior -= GameVariables.lifedrain_slash
            elif bloodreaver_attack == "== BLOOD REAVER HAS USED BLOODLUST ROAR AND LANDS IT ==":
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
            if plaguespitter_attack == "== PLAGUE SPITTER HAS USED TOXIC SPIT AND LANDS IT ==":
                GameVariables.Warrior -= GameVariables.toxic_spit
            elif plaguespitter_attack == "== PLAGUE SPITTER HAS USED PESTILANCE CLOUD AND LANDS IT ==":
                GameVariables.Warrior -= GameVariables.pestilence_cloud
            elif plaguespitter_attack == "== PLAGUE SPITTER HAS USED VIRAL BURST AND LANDS IT ==":
                GameVariables.Warrior -= GameVariables.viral_burst
            else:
                print("== WE CAN ALL BE GREATFUL HE MISSED! ==")
#this function handles the enemies spawning
    def Spawner(self):
        print (f"=== {GameVariables.enemy_count} ENEMIES HAS SPAWNED! ====")
        for _ in range(GameVariables.enemy_count):
            self.name = random.choice(GameVariables.name_list)
            GameVariables.name_list.remove(self.name)
            GameVariables.chosen_names.append(self.name)
            self.health = random.randint(20, 40)
            creationtext = f"== NAME: {self.name} HEALTH: {self.health} =="
            GameVariables.chosen_hp.append(self.health)
            GameVariables.enemycreation.append(creationtext)
#this function handles the enemies menu
    def EnemyMenu(self):
        indices_to_remove = [i for i, hp in enumerate(GameVariables.chosen_hp) if hp <= 0]
        for index in sorted(indices_to_remove, reverse=True):
            del GameVariables.chosen_names[index]
            del GameVariables.chosen_hp[index]
            del GameVariables.enemycreation[index]
        for name, health in zip(GameVariables.chosen_names, GameVariables.chosen_hp):
            print(f"== NAME: {name} HEALTH: {health} ==")
            continue
#this function handles the your attacks on the enmies.
    def EnemyAttack(self):
        print (f'=============================================================================================')
        print (Fore.CYAN + f"== TO CHOOSE ATTACK PLEASE TYPE 'A' - 'B' - 'C' ==" + Style.RESET_ALL)
        print (f"== YOU CAN VIEW YOUR ATTACKS AND THERE DESCRIPTION BY TYPING ANT OF THE FOLLOWING WHEN INGAME:")
        for item1, item2, item3, item4, item5 in zip(attack_list1, attack_list2, attack_list3, attack_list4, attack_list6):
            print (Fore.CYAN + f"{item1} - {item2} - {item3} - {item4} - {item5}" + Style.RESET_ALL)
        print (f'=============================================================================================')
        while True:
            print(f"======= WARRIOR HP: {GameVariables.Warrior} =======")
            self.EnemyMenu()
            print("===============================")
            answer = input("Choose Option [1 - 4] > ").lower()
            if answer == "1":
                print(f"== YOU CHOSE TO ATTACK {GameVariables.chosen_names[0]} ==")
                print(f"== CHOOSE SHIELD BASH - {GameVariables.shield_bash}DMG - RAGING STRIKE {GameVariables.shield_bash}DMG - WHIRLWIND STRIKE {GameVariables.whirlwind_slash}DMG ==")
                print (f'=============================================================================================')
                attack_answer = input("Choose Attack [A, B, C] > ")
                if attack_answer in attack_description2:
                    print (f'=============================================================================================')
                    print(attack_description2[attack_answer])
                    print (f'=============================================================================================')
                    continue
                if attack_answer == "a":
                    GameVariables.chosen_hp[0] -= GameVariables.shield_bash
                    shield_bash_print = random.choice(shield_bash_response)
                    print (f'=============================================================================================')
                    print(shield_bash_print)
                    print (f'=============================================================================================')
                    self.enemys_attack_func()
                    print (f'=============================================================================================')
                    GameVariables.score += random.randint(2,7)
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                    print (f'=============================================================================================')
                elif attack_answer == "b":
                    GameVariables.chosen_hp[0] -= GameVariables.raging_strike
                    raging_strike_print = random.choice(raging_strike_response)
                    print(raging_strike_print)
                    print (f'=============================================================================================')
                    self.enemys_attack_func()
                    print (f'=============================================================================================')
                    GameVariables.score += random.randint(2,7)
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                    print (f'=============================================================================================')
                elif attack_answer == "c":
                    GameVariables.chosen_hp[0] -= GameVariables.whirlwind_slash
                    whirlwind_strike_print = random.choice(whirlwind_slash_response)
                    print(whirlwind_strike_print)
                    print (f'=============================================================================================')
                    self.enemys_attack_func()
                    print (f'=============================================================================================')
                    GameVariables.score += random.randint(2,7)
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                    print (f'=============================================================================================')
                else:
                    print("== PLEASE ENTER A VALID INPUT ==")
                    attack_answer = input("Choose Attack [A, B, C] > ")
                    if GameVariables.chosen_hp[0] <= 0:
                        GameVariables.chosen_names.pop(0)
                        GameVariables.chosen_hp.pop(0)
                        GameVariables.enemycreation.pop(0)
            elif answer == "2":
                print(f"== YOU CHOSE TO ATTACK {GameVariables.chosen_names[1]} ==")
                print(f"== Choose Shield Bash - {GameVariables.shield_bash}Dmg - Raging Strike {GameVariables.shield_bash}Dmg - Whirlwind Strike {GameVariables.whirlwind_slash}Dmg ==")
                print (f'=============================================================================================')
                attack_answer = input("Choose Attack [A, B, C] > ")
                if attack_answer in attack_description2:
                    print (f'=============================================================================================')
                    print(attack_description2[answer])
                    print (f'=============================================================================================')
                    continue
                if attack_answer == "a":
                    GameVariables.chosen_hp[1] -= GameVariables.shield_bash
                    print(shield_bash_print)
                    print (f'=============================================================================================')
                    self.enemys_attack_func()
                    print (f'=============================================================================================')
                    GameVariables.score += random.randint(2,7)
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                    print (f'=============================================================================================')
                elif attack_answer == "b":
                    GameVariables.chosen_hp[1] -= GameVariables.raging_strike
                    raging_strike_print = random.choice(raging_strike_response)
                    print(raging_strike_print)
                    print (f'=============================================================================================')
                    self.enemys_attack_func()
                    print (f'=============================================================================================')
                    GameVariables.score += random.randint(2,7)
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                    print (f'=============================================================================================')
                elif attack_answer == "c":
                    GameVariables.chosen_hp[1] -= GameVariables.whirlwind_slash
                    whirlwind_strike_print = random.choice(whirlwind_slash_response)
                    print(whirlwind_strike_print)
                    print (f'=============================================================================================')
                    self.enemys_attack_func()
                    print (f'=============================================================================================')
                    GameVariables.score += random.randint(2,7)
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                    print (f'=============================================================================================')
                else:
                    print("== PLEASE ENTER A VALID INPUT ==")
                    attack_answer = input("Choose Attack [A, B, C] > ")
            elif answer == "3":
                print(f"== YOU CHOSE TO ATTACK {GameVariables.chosen_names[2]} ==")
                print(f"== Choose Shield Bash - {GameVariables.shield_bash}Dmg - Raging Strike {GameVariables.shield_bash}Dmg - Whirlwind Strike {GameVariables.whirlwind_slash}Dmg ==")
                print (f'=============================================================================================')
                attack_answer = input("Choose Attack [A, B, C] > ")
                if answer in attack_description2:
                    print (f'=============================================================================================')
                    print(attack_description2[answer])
                    print (f'=============================================================================================')
                    continue
                if attack_answer == "a":
                    GameVariables.chosen_hp[2] -= GameVariables.shield_bash
                    shield_bash_print = random.choice(shield_bash_response)
                    print(shield_bash_print)
                    print (f'=============================================================================================')
                    self.enemys_attack_func()
                    print (f'=============================================================================================')
                    GameVariables.score += random.randint(2,7)
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                    print (f'=============================================================================================')
                elif attack_answer == "b":
                    GameVariables.chosen_hp[2] -= GameVariables.raging_strike
                    raging_strike_print = random.choice(raging_strike_response)
                    print(raging_strike_print)
                    print (f'=============================================================================================')
                    self.enemys_attack_func()
                    print (f'=============================================================================================')
                    GameVariables.score += random.randint(2,7)
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                    print (f'=============================================================================================')
                elif attack_answer == "c":
                    GameVariables.chosen_hp[2] -= GameVariables.whirlwind_slash
                    whirlwind_strike_print = random.choice(whirlwind_slash_response)
                    print(whirlwind_strike_print)
                    print (f'=============================================================================================')
                    self.enemys_attack_func()
                    print (f'=============================================================================================')
                    GameVariables.score += random.randint(2,7)
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                    print (f'=============================================================================================')
                else:
                    print("== PLEASE ENTER A VALID INPUT ==")
                    attack_answer = input("Choose Attack [A, B, C] > ")
            elif answer == "4":
                print(f"== YOU CHOSE TO ATTACK {GameVariables.chosen_names[3]} ==")
                print(f"== Choose Shield Bash - {GameVariables.shield_bash}Dmg - Raging Strike {GameVariables.shield_bash}Dmg - Whirlwind Strike {GameVariables.whirlwind_slash}Dmg ==")
                print (f'=============================================================================================')
                attack_answer = input("Choose Attack [A, B, C] > ")
                if answer in attack_description2:
                    print (f'=============================================================================================')
                    print(attack_description2[answer])
                    print (f'=============================================================================================')
                    continue
                if attack_answer == "a":
                    GameVariables.chosen_hp[3] -= GameVariables.shield_bash
                    shield_bash_print = random.choice(shield_bash_response)
                    print(shield_bash_print)
                    print (f'=============================================================================================')
                    self.enemys_attack_func()
                    print (f'=============================================================================================')
                    GameVariables.score += random.randint(2,7)
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                    print (f'=============================================================================================')
                elif attack_answer == "b":
                    GameVariables.chosen_hp[3] -= GameVariables.raging_strike
                    raging_strike_print = random.choice(raging_strike_response)
                    print(raging_strike_print)
                    print (f'=============================================================================================')
                    self.enemys_attack_func()
                    print (f'=============================================================================================')
                    GameVariables.score += random.randint(2,7)
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                    print (f'=============================================================================================')
                elif attack_answer == "c":
                    GameVariables.chosen_hp[3] -= GameVariables.whirlwind_slash
                    whirlwind_strike_print = random.choice(whirlwind_slash_response)
                    print(whirlwind_strike_print)
                    print (f'=============================================================================================')
                    self.enemys_attack_func()
                    print (f'=============================================================================================')
                    GameVariables.score += random.randint(2,7)
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                    print (f'=============================================================================================')
                else:
                    print("== PLEASE ENTER A VALID INPUT ==")
                    attack_answer = input("Choose Attack [A, B, C] > ")
            else:
                print("== PLEASE TYPE A VALID INPUT :) ==")
                answer = input("Choose Enemy [1 - 4] > ").lower()
                
            if all(hp <= 0 for hp in GameVariables.chosen_hp):
                kill_section3()
                self.bossfight()
                break
            elif GameVariables.Warrior <= 0:
                show_charcter_Death()
                break

#this function starts the game, and all other menu functions.
def Start():
    menu = Menu()
    print("\n--- Main Menu ---")
    print("1. New Game")
    print("2. Difficulty")
    print("3. Scoreboard")
    print("4. Exit Game")

    Menu_Input = input("Choose Option > ")

    if Menu_Input == "1":
        menu.NewGame()
    elif Menu_Input == "2":
        menu.Difficulty_Selection()
    elif Menu_Input == "3":
        menu.Scoreboard()
    elif Menu_Input == "4":
        print("== QUITTING THE GAME ==")
    else:
        print("== Please Choose an Option ==")