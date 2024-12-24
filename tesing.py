import random
from GameClasses import GameVariables

enemy_count = random.randint(2,4)
enemy_creation2 = []
for i in range(enemy_count):

    name = random.choice(GameVariables.name_list)
    GameVariables.name_list.remove(name)
    GameVariables.chosen_names.append(name)


    health = random.randint(2, 4)
    creationtext = f"Name: {name} HP: {health}"
    enemy_creation2.append(creationtext)
    enem1, enem2, enem3, enem4 = creationtext
    print (creationtext)
    
    for i in range(creationtext):
        print (f"{enem1}", i + 1 )

    
    
    
  print (f"== {name} IS AT {hp} - {name} IS AT {hp} - YOU ARE AT {GameVariables.Warrior} ==")
                print(f"== Choose Shield Bash - {GameVariables.shield_bash}Dmg - Raging Strike {GameVariables.shield_bash}Dmg - Whirlwind Strike {GameVariables.whirlwind_slash}Dmg ==")


    
    

    
