import random, time
from Gamelists import shield_bash_response ,raging_strike_response, whirlwind_slash_response, frostwraith_attack_list, bloodreaver_attack_list, voidstalker_attack_list, plaguespitter_attack_list, buff_list
from GameFunctions import kill_section3, show_charcter_Death
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
    spectral_blade = 20



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
            elif random_buff == "+10ATK":
                GameVariables.shield_bash += 5
                GameVariables.raging_strike += 5
                GameVariables.whirlwind_slash += 5
                GameVariables.spectral_blade += 5
                print ("YOU HAVE GOT AN ATTACK BUFF OF 10 ALL YOUR ATTACKS DO 5 MORE DAMAGE == ")
            elif random_buff == "-10HP":
                GameVariables.Warrior -= 10
                print(f"== YOU HAVE BEEN GIVEN A DEBUFF OF -10HP YOU ARE NOW AT {GameVariables.Warrior}")
            elif random_buff == "-10ATK":
                GameVariables.shield_bash -= 5
                GameVariables.raging_strike -= 5
                GameVariables.whirlwind_slash -= 5
                GameVariables.spectral_blade -= 5
                print("== YOU HAVE BEEN GIVEN A DEBUFF YOU NOW HAVE -10ATK ALL ATTACKS TO 5 LESS DAMAGE ==")
        elif answer2 == "b" and charanswer == "c":
            print("== YOU HAVE ENCOUNTERED A HEALING TOKEN +30 HP! ==")
            character += 30
            print(f"== YOUR HP IS NOW {rogue} ==")
            print (f'=============================================================================================')
            time.sleep(3)
            print ("== NEW ATTACK LEARNED ROLLING THUNDER")
            print ("== This attack that stuns the enemy for one round and allows you to land 2 attacks without getting hit. You can only use this once every other round.")
            time.sleep(1)
            #playing boss room
            print ("== ONTO THE FINAL BOSS LEVEL ALL YOUR TRAINING HAS LEAD UP TO THIS! ==")
            print (f'=============================================================================================')
            time.sleep(3)
            #announcing a new attack that the charcter learns
            print ("== NEW ATTACK LEARNED SOUL BURST ==")
            print ("== IF YOU WOULD LIKE MORE DETAILS ON THE ATTACK TYPE MOVES :) ==")
            time.sleep(1)
        elif answer2 == "c" and charanswer == "c":
    
    def enemys_attack_func(self):
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
                
    def Spawner(self):
        print (f"== {GameVariables.enemy_count} ENEMIES HAS SPAWNED! ==")
        for _ in range(GameVariables.enemy_count):
            self.name = random.choice(GameVariables.name_list)
            GameVariables.name_list.remove(self.name)
            GameVariables.chosen_names.append(self.name)
            self.health = random.randint(20, 40)
            creationtext = f"== NAME: {self.name} HEALTH: {self.health} =="
            GameVariables.chosen_hp.append(self.health)
            GameVariables.enemycreation.append(creationtext)
            
    def EnemyMenu(self):
        for name, health in zip(GameVariables.chosen_names, GameVariables.chosen_hp):
            print(f"== NAME: {name} HEALTH: {health} ==")
            continue
        
    def EnemyAttack(self):
        print("== WHO DO YOU WANT TO ATTACK ==")
        while True:
            self.EnemyMenu()
            print(f"== WARRIOR == HP: {GameVariables.Warrior} ==")
            answer = input("Choose Enemy > ").lower()
            if answer == "1":
                print(f"== YOU CHOSE TO ATTACK {GameVariables.chosen_names[0]} ==")
                print(f"== HOW WILL YOU ATTACK ==\n Name: {GameVariables.chosen_names[0]} HP: {GameVariables.chosen_hp[0]} ==")
                print(f"== CHOOSE SHIELD BASH - {GameVariables.shield_bash}DMG - RAGING STRIKE {GameVariables.shield_bash}DMG - WHIRLWIND STRIKE {GameVariables.whirlwind_slash}DMG ==")
                attack_answer = input("Choose Atack > ")
                if attack_answer == "shield bash":
                    GameVariables.chosen_hp[0] -= GameVariables.shield_bash
                    shield_bash_print = random.choice(shield_bash_response)
                    print(shield_bash_print)
                    self.enemys_attack_func()
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                elif attack_answer == "raging strike":
                    GameVariables.chosen_hp[0] -= GameVariables.raging_strike
                    raging_strike_print = random.choice(raging_strike_response)
                    print(raging_strike_print)
                    self.enemys_attack_func()
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                elif attack_answer == "whirlwind strike":
                    GameVariables.chosen_hp[0] -= GameVariables.whirlwind_slash
                    whirlwind_strike_print = random.choice(whirlwind_slash_response)
                    print(whirlwind_strike_print)
                    self.enemys_attack_func()
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                else:
                    print("== PLEASE ENTER A VALID INPUT ==")
                    attack_answer = input("Choose Atack > ")
            elif answer == "2":
                print(f"== YOU CHOSE TO ATTACK {GameVariables.chosen_names[1]} ==")
                print(f"== HOW WILL YOU ATTACK ==\n Name: {GameVariables.chosen_names[1]} HP: {GameVariables.chosen_hp[1]} ==")
                print(f"== Choose Shield Bash - {GameVariables.shield_bash}Dmg - Raging Strike {GameVariables.shield_bash}Dmg - Whirlwind Strike {GameVariables.whirlwind_slash}Dmg ==")
                attack_answer = input("Choose Atack > ")
                if attack_answer == "shield bash":
                    GameVariables.chosen_hp[1] -= GameVariables.shield_bash
                    print(shield_bash_print)
                    self.enemys_attack_func()
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                elif attack_answer == "raging strike":
                    GameVariables.chosen_hp[1] -= GameVariables.raging_strike
                    raging_strike_print = random.choice(raging_strike_response)
                    print(raging_strike_print)
                    self.enemys_attack_func()
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                elif attack_answer == "whirlwind strike":
                    GameVariables.chosen_hp[1] -= GameVariables.whirlwind_slash
                    whirlwind_strike_print = random.choice(whirlwind_slash_response)
                    print(whirlwind_strike_print)
                    self.enemys_attack_func()
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                else:
                    print("== PLEASE ENTER A VALID INPUT ==")
                    attack_answer = input("Choose Atack > ")
            elif answer == "3":
                print(f"== YOU CHOSE TO ATTACK {GameVariables.chosen_names[2]} ==")
                print(f"== HOW WILL YOU ATTACK ==\n Name: {GameVariables.chosen_names[2]} HP: {GameVariables.chosen_hp[2]} ==")
                print(f"== Choose Shield Bash - {GameVariables.shield_bash}Dmg - Raging Strike {GameVariables.shield_bash}Dmg - Whirlwind Strike {GameVariables.whirlwind_slash}Dmg ==")
                attack_answer = input("Choose Atack > ")
                if attack_answer == "shield bash":
                    GameVariables.chosen_hp[2] -= GameVariables.shield_bash
                    shield_bash_print = random.choice(shield_bash_response)
                    print(shield_bash_print)
                    self.enemys_attack_func()
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                elif attack_answer == "raging strike":
                    GameVariables.chosen_hp[2] -= GameVariables.raging_strike
                    raging_strike_print = random.choice(raging_strike_response)
                    print(raging_strike_print)
                    self.enemys_attack_func()
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                elif attack_answer == "whirlwind strike":
                    GameVariables.chosen_hp[2] -= GameVariables.whirlwind_slash
                    whirlwind_strike_print = random.choice(whirlwind_slash_response)
                    print(whirlwind_strike_print)
                    self.enemys_attack_func()
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                else:
                    print("== PLEASE ENTER A VALID INPUT ==")
                    attack_answer = input("Choose Atack > ")
            elif answer == "4":
                print(f"== YOU CHOSE TO ATTACK {GameVariables.chosen_names[3]} ==")
                print(f"== HOW WILL YOU ATTACK ==\n Name: {GameVariables.chosen_names[3]} HP: {GameVariables.chosen_hp[3]} ==")
                print(f"== Choose Shield Bash - {GameVariables.shield_bash}Dmg - Raging Strike {GameVariables.shield_bash}Dmg - Whirlwind Strike {GameVariables.whirlwind_slash}Dmg ==")
                attack_answer = input("Choose Atack > ")
                if attack_answer == "shield bash":
                    GameVariables.chosen_hp[3] -= GameVariables.shield_bash
                    shield_bash_print = random.choice(shield_bash_response)
                    print(shield_bash_print)
                    self.enemys_attack_func()
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                elif attack_answer == "raging strike":
                    GameVariables.chosen_hp[3] -= GameVariables.raging_strike
                    raging_strike_print = random.choice(raging_strike_response)
                    print(raging_strike_print)
                    self.enemys_attack_func()
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                elif attack_answer == "whirlwind strike":
                    GameVariables.chosen_hp[3] -= GameVariables.whirlwind_slash
                    whirlwind_strike_print = random.choice(whirlwind_slash_response)
                    print(whirlwind_strike_print)
                    self.enemys_attack_func()
                    print("== WHO DO YOU CHOOSE TO ATTACK NEXT! ==")
                else:
                    print("== PLEASE ENTER A VALID INPUT ==")
                    attack_answer = input("Choose Atack > ")
            else:
                print("== PLEASE TYPE A VALID INPUT :) ==")
                answer = input("Choose Enemy > ").lower()
                
            if all(hp <= 0 for hp in GameVariables.chosen_hp):
                kill_section3()
                self.bossfight()
                break
            elif GameVariables.Warrior <= 0:
                show_charcter_Death()
                break
                    
if __name__ == "__main__":
    test = Enemies(0, "", 4, 2)
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