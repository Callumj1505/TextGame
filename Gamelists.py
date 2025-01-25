import random

#THIS LINKS TO THE ATTACK FUNCTION FOR THE FIRST ENEMY
#==============================================================================================================================#
xyrif_random_attacks = [
    "== HE USES LIGHT BEAM AND LANDS IT! ==",
    "== XYRIF ATTACKS WITH ANITMATTER PULSE AND LANDS IT!",
    "== HE PUNCHES ON YOU AND LANDS IT, UNLUCKY! ==",
    "== HE HAS MISSED =="
]
#ROGUE THIS PRINTS WHEN POISON PURGE IS CHOSEN
#==============================================================================================================================#
poison_attack_purge = [
    "== DAMN THAT ISN'T FUN FOR HIM! LUCKILY I DONT FEEL BAD :D ==", #1
    "== I PERSONALLY WOULDN'T WANT TO EXPERIENCE THAT! GOOD JOB KEEP IT UP. ==", #2
    "== BEEP BOOP PURGING BEEP BOOP! ==", #3
    "== IF IT WAS ME I WOULDN'T PERSONALLY LIKE THAT! ==", #4
    "== GO CRAZY AHHHHHH GO STUPID AHHHHH.... GOOD JOB. ==", #5
    "== ENJOYING WATCHING YOU WIN.. FOR ONCE HAHAHAHAHA! ==" #6
]
#ROGUE THIS PRINTS WHEN INFECT IS CHOSEN
#==============================================================================================================================#
infect_attack = [
    f"== YOU INFECTED HIM -20 FOR HIM! ==",#1
    "== TRY NOT TO GET A CUT DONT WANT TO GO THAT FAR! ==",#2
    "== TRY NOT TO LAUGH CHALLENGE, OHN WAIT TO LATE HA HA HA ==",#3
    "== OMG HE JUST GOT INFECTED FROM YOUR LOVE :0 JKJK EZ -20 ==",#4
    "== YOUR SMASHING THIS KEEP IT UP! ==",#5
    "== BISH BASH BOSH YOU INFECTED HIM CARRY ON PUSHING ==",#6
]
#ROGUE PRINTS WHEN POISON RAIN IS CHOSEN
#==============================================================================================================================#
poison_rain_attack =[
    "== ITS RAINING POISON HALLELIJAH ITS RAINING POISON! ==",#1
    "== HITTING HIM WITH THE BIG GUNS KEEP HER GOING! ==",#2
    "== BEING POISONED THIS MUCH CANT BE FUN IN ALL FAIRNESS! ==",#3
    "== PINKY PONKO POISON! THERES NO WAY HE ISN'T FEELING THIS! FINISH HIM. ==",#4
    "== DONT LET HIM EFFECT YOU WITH HIS NONCHALANTNESS. ==",#5
    "== RUN EM DOWN AND POISON EM DOWN....",#6
]
#ROGUE PRINTS WHEN SOUL BURST IS CHOSEN
#==============================================================================================================================#
soul_burst_attack = [
    "== THATS THE FIRST I HAVE SEEN THAT AND I WAS IMPRESSED",
    "== BBBRRRRRRRRR SOUL BURST INITIATED! ==",
    "== QUICK QUESTION WHERE ARE YOU GETTING THESE SOULS FROM? NOT COMPLAINING JUST ASKING ==",
    "== BOOOOOOOOMMMM MASSIVE DAMAGE, IM SUCH A PROUD TUTOR :,) =="
    "== IF YOU KEEP UP WITH THESE NUMBERS THERE WILL BE A CHICKEN DINNER FOR US! =="
    "== KNOWLEDGE! STRENGTH! INTEGRITY! IS SOMETHING I DONT SEE IN YOU.... JK GOOD JOB!"
]
#ROGUE PRINTS AT THE START OF EVERY ROUND 
#==============================================================================================================================#
response_list = [
    f"== I WANNA SEE SOME SERIOUS S%*T! LETS SEE WHAT YOU CHOOSE NEXT!==\n== poison Purge -35HP == Infect -20HP == Poison Rain -30HP ==",#1
    f"== GOOD JOB WITH THAT ONE, LETS FINISH HIM OFF SOONER RATHER THAN LATER ==\n== poison Purge -35HP == Infect -20HP == Poison Rain -30HP ==", #2
    f"== OKAY ONTO THE NEXT ATTACK! BRING IT ON XYRIF ==\n== poison Purge -35HP == Infect -20HP == Poison Rain -30HP ==",#3
    f"== COMMANDER WE ARE ATTACKING WHAT ARE YOU GOING TO DO! ==\n== poison Purge -35HP == Infect -20HP == Poison Rain -30HP ==", #4
    f"== SIR WE ARE GOING TO ATTACK PREPARE! ==\n== poison Purge -35HP == Infect -20HP == Poison Rain -30HP ==", #5
    f"== THERE IS ONLY ONE VICTOR IN THIS REALM LETS HOPE ITS YOU! ==\n== poison Purge -35HP == Infect -20HP == Poison Rain -30HP ==" #6
]

#RANDOM RESPONSE LISRT FOR BOSS ROGUE
#==============================================================================================================================#
response_list2 = [
    f"== LETS SHOW THIS GUY WHO IS THE REAL OG IN THESE ENDS! ==\n== poison Purge -35HP == Infect -20HP == Poison Rain -30HP == soul_burst - 40hp ==",#1
    f"== JUST BECAUSE HE IS BIGGER DOESN'T MEAN HE IS BETTER STAND STRONG! ==\n== poison Purge -35HP == Infect -20HP == Poison Rain -30HP == soul_burst - 40hp ==", #2
    f"== TEMPEST GUARDIAN ISN'T READY FOR THE POWER YOU HAVE.. LETS SHOW HIM! ==\n== poison Purge -35HP == Infect -20HP == Poison Rain -30HP == soul_burst - 40hp ==",#3
    f"== COMMANDER ME AND THE WHOLE TEAM BELIEVES IN YOU! ==\n== poison Purge -35HP == Infect -20HP == Poison Rain -30HP == soul_burst - 40hp ==", #4
    f"== SIR WINNING IS IN YOUR BLOOD.. LETS SHOW THEM WHY! ==\n== poison Purge -35HP == Infect -20HP == Poison Rain -30HP == soul_burst - 40hp ==", #5
    f"== THERE CAN ONLY BE ONE WINNER AND WE KNOW IT CAN BE YOU! ==\n== poison Purge -35HP == Infect -20HP == Poison Rain -30HP == soul_burst - 40hp ==" #6
]

#THIS LINKS TO THE ATTACK FUNCTION FOR THE BOSS
#==============================================================================================================================#
tempest_random_attacks = [
    "== HE USES WRAITH SWING AND LANDS IT! ==",
    "== TEMPEST GUARDIAN IS CHARGING PULSE BLAST WITH HE SHOOTS AND LANDS IT!",
    "== HE USES CALL OF GUARDIANS AND LANDS IT, UNLUCKY! ==",
    "== HE USES WRAITH STRIKE AND LANDS IT! =="
    "== HE HAS MISSED =="
]

#ROGUE CHEST OPENING LIST
#================================================================================================================================#
chest_buffr = ["== YOU HAVE RECEIVED A NEW PEACE OF ARMOR WITH +10 ARMOR! ==", "== YOU HAVE RECEIVED NEW DAGGERS! +10 PHYSICAL DAMAGE! ==", "== YOU HAVE RECIEVED A METAL LEGGINGS +10 HEALTH =="]

# A DICTIONARY OF THE ATTACKS THAT THE ENEMIES HAVE AND THAT YOU HAVE.
#==============================================================================================================================#
attack_description ={
    "poison purge":"== LETS OUT A GROUND SHAKING PURPLE PULSE WHICH LIGHT SHINES THROUGH THE CRACKS OF THE EARTH,\nKNOCKING HIM OFF BALANCE. A HARD HITTER FOR SURE! ==\n=============================================================================================",
    "infect":"== THIS ATTACK SENDS OUT A PUFF OF GREEN SMOKE INFECTING THE ENEMY WITH POISON ==\n=============================================================================================",
    "poison rain":"== THIS CAUSES ACID RAIN TO COME DOWN AND LAND ON THE ENEMY SCOLDING HIM AND WEAKENING THERE OUTER SHELL ==\n=============================================================================================",
    "soul burst":"== EMPTY SOULS WILL FLY OUT OF YOUR BODY AND ATTACHING THEMSELVES TO THE ENEMY CAUSING HEAVY DAMAGE ==\n=============================================================================================",
    "light beam":"== THE ENEMY EMITS 2 BLUE LIGHT BEAMS FROM BOTH HANDS SCOLDING YOU ==\n=============================================================================================",
    "animatter pulse":"== THE ENEMY PULLS ANTIMATTER FROM THE SKY TO FIRE RIGHT AT YOU GIVING YOU RADIATION AND WEAKENING DEFENSES\n=============================================================================================",
    "punch":"== THE ENEMY THROWS A SIMPLE PUNCH THAT DOES DAMAGE ==\n=============================================================================================",
    "swing":"== A SIMPLE SWING FROM THE BOSS DEALING MINIMAL DAMAGE ==\n=============================================================================================",
    "Pulse Blast":"== A CHARGE FROM HIS THIRD EYE THAT WILL DAMAGE ARMOR ==\n=============================================================================================",
    "wraith strike":"== THE ENEMY CALLS ON HIS SPIRITS TO CHARGE FORWARD AND HIT YOU WITH THERE SPEAR! ==\n=============================================================================================",
    "call of guardians":"== FROM THE HEAVENS HIS SERVANT GUARDIANS SHINE AN INTENSE BEAM OF LIGHT DOWN THAT DOES HEAVY DAMAGE ==\n=============================================================================================",
    "xyrif":"LIFE FORM = ENERGY ROCK ELEMENT\nABILITIES = ELECTRIC\nHEALTH =100\n=============================================================================================",
    "tempest guardian":"LIFE FORM = LIGHT BRINGER \nABILITIES = HEAVENLY\nHEALTH =100\n============================================================================================="
    }

#THESE LISTS ARE USED SO THAT I AM ABLE YOU USE ZIP AND PACE THEM SIDE BY SIDE TO ONE ANOTHER.
#==============================================================================================================================#
option1 = ["YOUR ATTACKS","poison purge","infect      ","poison rain ","soul burst  "]
option2 = ["XYRIF ATTACKS","light beam      ","antimatter pulse","punch           ","xyrif           "]#
option3 = ["TEMPEST GUARDIAN ATTACKS","swing","pulse blast","call of guardians","wraith strike","tempest"]

#END OF ROGUE PATH LISTS
#==============================================================================================================================#




#WIZARD LISTS STARTS NOW
#================================================================================================================================#

#WIZARD GOBLIN ATTACKS
#==============================================================================================================================#
goblin_attack1 = ["== HE REPLIES WITH SLAP BUT HE MISSES THANK GOD ==", "== HE REPLIES WITH SLAP AND LANDS OOOFF THAT HURTS ==" ]
goblin_attack2 = ["== GOBLIN USES BITE AND MISSES! ==", "== GOBLIN USES BITE AND LANDS IT! =="]
goblin_attack3 = ["== GOBLIN USES SPIT AND LANDS IT ==", "== GOBLIN USES SPIT AND MISSES! ==" ]

#WIZARD GORLOCK ATTACKS
#==============================================================================================================================#
gorlock_list = ["== HE SWINGS WITH ELECTRIC HAMMER AND HITS YOU :O ==", "== HE REPLIES WITH ELECTRIC HAMMER AND MISSES *JESUS NOISES START PLAYING* =="]
gorlock_list2 = ["== INCOMING! A HUGE POKE FROM THE BIG MAN HIMSELF! ==", "HERE IT COMES... HERE IT LANDS AND HE MISSES IM HAPPY FOR YOU PAL! =="]
gorlock_list3 = ["== PLEASE NO NOT THE HAMMER AGAIN! BOOM YOUR SQUISHED WITH HIS HAMMER SWING ==", "== THERE IS EMANATE DANGER INBOUND ON YOUR HEAD TOP....... YIKES HE MISSED XD =="]
gorlock_list4 = ["== OMG HE IS IN THE AIR... AND BOOOOOMMM RIGHT IN HIS BELLY BUTTON HE USES BODY SLAM AND LANDS IT! ==", "== OMG HE IS IN THE AIR... HES FALLING OMG HE MISSED YAYYYYYY =="]

#path3 wizard chests opening.
#==================================================================================================================================#
chest_buffwi = ["== YOU HAVE RECEIVED A ROBE PEACE WITH +10 ARMOR! ==", "== YOU HAVE RECEIVED A NEW STAFF! +10 PHYSICAL DAMAGE! ==", "== YOU HAVE RECEIVED A NEW SPELLBOOK +10 MAGICAL DAMAGE =="]


#START OF WARRARIOR LISTS
#===================================================================================================================================#


spectral_blade_response = [
    "== SPECTRAL BLADE INITIATED...... BEEP....BOOP ==",
    "== I DIDN'T KNOW YOU HAD IT IN YOU! ==",
    "== WEEEEEE ARE THE CHAMPIONS MY FRIEND! ==",
    "== THIS IS A GOOD FARTHER SON MOMENT BUT IM NOT YOUR DAD AND YOUR NOT MY SON. GOOD JOB KEEP IT UP! ==",
    "== I WOULD SAY I AM IMPRESSED BUT I AM NOT ==",
    "== KEEP IT UP! ==",
]

shield_bash_response = [
    "== STRAIGHT INTO ACTION WITH A SHIELD BASH! ==",
    "== BOOM YOU AINT GOT THAT SHIELD FOR NO REASON! ==",
    "== USE THAT THANG LIKE YOUR MAMA TAUGHT YOU! ==",
    "== I NEVER KNEW A ROUND OBJECT COULD BE SO DEADLY ==",
    "== WE'VE GOT CAPTAIN AMERICA OVER HERE FOLKS ==",
    "== YOUR DEADLY WITH THAT! GOOD JOB :D =="
]

raging_strike_response = [
    "== GOING IN ABSOLUTLEY FUMING WITH RAGING STRIKE ==",
    "== I KNOW HE FELT THAT STRIKE! ==",
    "== GOOD JOB! HITTING THEM HARD KEEP IT UP! ==",
    "== RAGING SRIKE HAS GOT TO BE MY FAVORITE SO FAR! ==",
    "== KEEP GOING AT THIS PACE AND THEY WILL BE DEAD IN NO TIME ==",
    "== ROLLING LOUD AND PROUD! RAGING STRIKE LADIES AND GENTELMEN! ==",
]

whirlwind_slash_response = [
    "== A MAN THAT CONTROLS THE WIND! DESTROY HIM. ==",
    "== THE FASTER YOU SPIN THE HARDER YOU HIT ==",
    "== SONIC THE HEDGEHOG INCOMING! ==",
    "== NICE SHOT I BET HE FELT THAT ONE! ==",
    "== CATAGORY 5 HURICANE IMCOMING! ==",
    "== JUST KEEP SPINING JUST KEEP SPINNING! ==",
]
    
varnyx_attack_list = [
    "== VARNYX THE SHARDWOVEN HAS USED FRACTURED RIFT AND LANDS IT ==",
    "== VARNYX THE SHARDWOVEN HAS USED PRISMATIC OVERLOAD AND LANDS IT ==",
    "== VARNYX THE SHARDWOVEN HAS USED SHARDSTORM BARRAGE AND LANDS IT ==",
    "== VARNYX THE SHARDWOVEN HAS USED RESONANT COLLAPSE AND LANDS IT ==",
    "== VARNYX THE SHARDWOVEN USED FRACTURED RIFT AND MISSES IT ==",
    "== VARNYX THE SHARDWOVEN USED PRISMATIC OVERLOAD AND MISSES IT ==",
    "== VARNYX THE SHARDWOVEN USED SHARDSTORM BARRAGE AND MISSES IT ==",
    "== VARNYX THE SHARDWOVEN USED RESONANT COLLAPSE AND MISSES IT =="
]

frostwraith_attack_list = [
    "== FROST WRAITH HAS USED ICE SHARD BARRAGE AND LANDS IT ==",
    "== FROST WRAITH HAS USED FROZEN GRASP AND LANDS IT ==",
    "== FROST WRAITH HAS USED BLIZZARD VEIL AND LANDS IT ==",
    "== FROST WRAITH USED ICE SHARD BARRAGE AND MISSES IT ==",
    "== FROST WRAITH USED FROZEN GRASP AND MISSES IT ==",
    "== FROST WRAITH USED BLIZZARD VEIL AND MISSES IT ==",
]

bloodreaver_attack_list =[
    "== BLOOD REAVER HAS USED BLOOD FRENZY AND LANDS IT ==",
    "== BLOOD REAVER HAS USED LIFEDRAIN SLASH AND LANDS IT ==",
    "== BLOOD REAVER HAS USED BLOODLUST ROAR AND LANDS IT ==",
    "== BLOOD REAVER USED BLOOD FRENZY AND MISSES IT ==",
    "== BLOOD REAVER USED LIFEDRAIN SLASH AND MISSES IT ==",
    "== BLOOD REAVER USED BLOOD LUST ROAR AND MISSES IT ==",
]

voidstalker_attack_list = [
    "== VOID STALKER HAS USED SHADOW STEP AND LANDS IT ==",
    "== VOID STALKER HAS USED ETHERNAL STRIKE AND LANDS IT ==",
    "== VOID STALKER HAS USED VOID RIFT AND LANDS IT ==",
    "== VOID STALKER USED SHADOW STEP AND MISSES IT ==",
    "== VOID STALKER USED ETHERNAL STRIKE AND MISSES IT ==",
    "== VOID STALKER USED VOID RIFT AND MISSES IT ==",
]

plaguespitter_attack_list = [
    "== PLAGUE SPITTER HAS USED TOXIC SPIT AND LANDS IT ==",
    "== PLAGUE SPITTER HAS USED PESTILANCE CLOUD AND LANDS IT ==",
    "== PLAGUE SPITTER HAS USED VIRAL BURST AND LANDS IT ==",
    "== PLAGUE SPITTER USED TOXIC SPIT AND MISSES IT ==",
    "== PLAGUE SPITTER USED PESTILANCE CLOUD AND MISSES IT ==",
    "== PLAGUE SPITTER USED VIRAL BURST AND MISSES IT ==",
]

response_list3 = [
    f"== I WANNA SEE SOME SERIOUS S%*T! LETS SEE WHAT YOU CHOOSE NEXT!==",#1
    f"== GOOD JOB WITH THAT ONE, LETS FINISH HIM OFF SOONER RATHER THAN LATER ==", #2
    f"== OKAY ONTO THE NEXT ATTACK! BRING IT ON XYRIF ==",#3
    f"== COMMANDER WE ARE ATTACKING WHAT ARE YOU GOING TO DO! ==", #4
    f"== SIR WE ARE GOING TO ATTACK PREPARE! ==", #5
    f"== THERE IS ONLY ONE VICTOR IN THIS REALM LETS HOPE ITS YOU! ==" #6
]

chest_buffw = [
    
    "== YOU HAVE RECEIVED A NEW PEACE OF CHEST ARMOR WITH +10 ARMOR! ==",
    "== YOU HAVE RECEIVED NEW LONG SWORD! +3 ARMOR PHYSICAL DAMAGE! ==", 
    "== YOU HAVE RECIEVED A METAL LEGGINGS +10 HEALTH =="
]

# LISTS USED THROUGH ALL PATHS.
#==============================================================================================================================#

#RANDOM BUFF FROM SHRINE
#==============================================================================================================================#
buff_list = ["+25HP", "+10ATK", "-10HP", "-10ATK"]

attack_list1 = ["FROST WRAITH      ","Ice Shard Barrage ", "Frozen Grasp      ", "Blizzard Veil     "]
attack_list2 = ["BLOOD REAVER    ","Blood Frenzy    ", "Lifedrain Slash ", "Bloodlst Roar   "]
attack_list3 = ["VOID STALKER    ","Shadow Step     ", "ethernal strike ", "void rift       "]
attack_list4 = ["PLAGUE SPITTER    ","Toxic Spit        ", "Pestilence Cloud  ", "Viral Burst       "]
attack_list6 = ["YOUR MOVES","Shield Bash", "Ragin Strike", "Whirlind Slash", "Spectral Blade" ]
attack_list5 = ["VARNYX THE DESTROER","Fractured Rift","Prismatic Overload","Resonance Collapse"]

attack_description2 = {
    "ice shard barrage":"This attack involves the user flash-freezing chunks of ice and hurling them at the target. It’s a rapid, multi-hit move that can overwhelm opponents with a barrage of ice shards",
    "frozen grasp":"This spell envelops a target in harsh winter cold, leaving them frozen for a time. It’s a powerful frost spell that immobilizes the target, making them vulnerable to further attacks",
    "blizzard veil":"This move unleashes a blizzard that strikes opponents with icy winds, potentially freezing them solid. It’s a devastating attack that can cover a wide area and hinder the movement of enemies",
    "blood frenzy":"This attack drives the user into a bloodlust frenzy, granting advantage on melee attacks against enemies that are not at full health. It's a powerful move that can turn the tide of battle when used strategically.",
    "lifedrain slash":": This attack delivers a precise and powerful slash infused with dark energy, causing the target to suffer lingering pain and reduced physical abilities. The wound inflicted by this slash continuously saps the target's strength, making them weaker over time and leaving them vulnerable to subsequent attacks.",
    "bloodlust roar":"This move unleashes a powerful roar that increases the user's attack power and may cause enemies to become enraged or fearful, potentially lowering their defenses",
    "shadow step":"This attack allows the user to move swiftly and silently through the shadows, reappearing behind their target with a deadly strike. It's a teleportation move that can catch enemies off guard and is perfect for positioning or escaping danger",
    "ethernal strike":"This attack delivers a powerful blow imbued with otherworldly energy. It strikes with such force that it disrupts the target's very essence, causing lasting damage that transcends physical wounds",
    "void rift":"This move tears open a rift to the void, unleashing dark, chaotic energy that can engulf and damage all enemies within its vicinity. The attack distorts reality itself, making it a devastating area-of-effect move.",
    "toxic spit":"This attack involves the user spitting a corrosive, toxic substance at the target. The venom burns and poisons the target on contact, causing continuous damage over time and weakening their defenses.",
    "pestilence cloud":"This move creates a swirling cloud of noxious gas that spreads out and envelops enemies. The toxic miasma not only deals damage but also inflicts various debilitating effects, such as slowing movement and reducing attack power.",
    "viral burst":"This attack releases a concentrated burst of viral energy, infecting all nearby enemies with a fast-spreading disease. The infection rapidly depletes the health of those affected and has a chance to spread to others who come into contact with the infected.",
    "fractured rift":"This attack creates a tear in the fabric of reality, causing chaotic energy to surge through the rift and damage enemies caught in its wake. The fracture destabilizes the area, leading to unpredictable and powerful bursts of energy that can severely harm anyone nearby.",
    "prismatic overload":"This move harnesses the full spectrum of light, channeling prismatic energy into a devastating attack. The overloaded energy refracts and explodes upon impact, blinding and disorienting enemies while dealing significant damage across a wide area.",
    "resonance collapse":"This attack generates powerful resonant waves that cause a catastrophic collapse in the target’s structure. The waves build up a harmonic frequency that leads to a sudden and destructive implosion, dealing heavy damage to all affected enemies and leaving them vulnerable to further attacks.",
    "shield bash":"This attack involves the user forcefully striking the target with their shield. The impact can stun and stagger the opponent, leaving them momentarily disoriented and vulnerable to follow-up attacks.",
    "raging strike":"This move channels the user's anger into a powerful melee strike. Fueled by rage, the attack delivers a devastating blow that can break through defenses and deal significant damage.",
    "whirlwind slash":"This attack sees the user spinning with their weapon, creating a deadly whirlwind of slashes. The move hits all nearby enemies, making it effective for crowd control and dealing multiple hits in quick succession.",
    "spectral blade":"This attack summons a blade of ethereal energy that can cut through both physical and magical defenses. The spectral blade strikes with a ghostly precision, leaving a chilling effect on the target.",
}