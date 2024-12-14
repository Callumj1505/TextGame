
class GameVariables:
    Cursed_Knight = 100

    cursed_slash = 15
    wailing_souls = 20
    unholy_roar = 35

    Warrior = 100

    shield_bash = 20
    raging_strike = 30
    whirlwind_slash = 15



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
        print("2. Hard")
        
        Choice = input("Choose Option > ")
        if Choice == "1":
            self.difficulty = "EASY"
            time.sleep(1.4)
            self.NewGame()
        elif Choice == "2":
            GameVariables.cursed_slash -= 5
            GameVariables.wailing_souls -= 5
            GameVariables.unholy_roar -= 5

            GameVariables.shield_bash += 2
            GameVariables.raging_strike += 2
            GameVariables.whirlwind_slash += 2
            self.difficulty = "MEDIUM"
            print("== ENEMY ATTACKS HAVE BEEN INCREASED BY 2! ==\n== YOUR ATTACKS HAVE BEEN DECREASED BY 5! ==")
            time.sleep(1.4)
            self.NewGame()
        elif Choice == "3":
            GameVariables.cursed_slash -= 7
            GameVariables.wailing_souls -= 7
            GameVariables.unholy_roar -= 7

            GameVariables.shield_bash += 5
            GameVariables.raging_strike += 5
            GameVariables.whirlwind_slash = 5
            self.difficulty = "HARD"
            print("== ENEMY ATTACKS HAVE BEEN INCREASED BY 5! ==\n== YOUR ATTACKS HAVE BEEN DECREASED BY 7! ==")
            time.sleep(1.4)
            self.NewGame()
            


        
                
    
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