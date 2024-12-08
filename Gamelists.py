import random

#THIS LINKS TO THE ATTACK FUNCTION FOR THE FIRST ENEMY
#==============================================================================================================================#
xyrif_random_attacks = [
    "== HE USES LIGHT BEAM AND LANDS IT! ==",
    "== HE USES LIGHT BEAM AND MISSES! ==",
    "== XYRIF ATTACKS WITH ANITMATTER PULSE AND LANDS IT!",
    "== XYRIF ATTACKS WITH ANITMATTER PULSE AND MISSES, LUCKY YOU! ==",
    "== HE PUNCHES ON YOU AND LANDS IT, UNLUCKY! ==",
    "== HE PUNCHES ON YOU AND MISSES, WE WILL COUNT THAT ONE AS A WIN! =="
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
    f"== LETS SHOW THIS GUY WHO IS THE REAL OG IN THESE ENDS! ==\n== poison Purge -35HP == Infect -20HP == Poison Rain -30HP ==",#1
    f"== JUST BECAUSE HE IS BIGGER DOESN'T MEAN HE IS BETTER STAND STRONG! ==\n== poison Purge -35HP == Infect -20HP == Poison Rain -30HP ==", #2
    f"== TEMPEST GUARDIAN ISN'T READY FOR THE POWER YOU HAVE.. LETS SHOW HIM! ==\n== poison Purge -35HP == Infect -20HP == Poison Rain -30HP ==",#3
    f"== COMMANDER ME AND THE WHOLE TEAM BELIEVES IN YOU! ==\n== poison Purge -35HP == Infect -20HP == Poison Rain -30HP ==", #4
    f"== SIR WINNING IS IN YOUR BLOOD.. LETS SHOW THEM WHY! ==\n== poison Purge -35HP == Infect -20HP == Poison Rain -30HP ==", #5
    f"== THERE CAN ONLY BE ONE WINNER AND WE KNOW IT CAN BE YOU! ==\n== poison Purge -35HP == Infect -20HP == Poison Rain -30HP ==" #6
]

#THIS LINKS TO THE ATTACK FUNCTION FOR THE BOSS
#==============================================================================================================================#
tempest_random_attacks = [
    "== HE USES WRAITH STRIKE AND LANDS IT! ==",
    "== HE USES WRAITH STRIKE AND MISSES! ==",
    "== TEMPEST GUARDIAN IS CHARGING PULSE BLAST WITH HE SHOOTS AND LANDS IT!",
    "== TEMPEST GUARDIAN ATTACKS WITH PULSE BLAST AND MISSES, LUCKY YOU! ==",
    "== HE USES CALL OF GUARDIANS AND LANDS IT, UNLUCKY! ==",
    "== HE USES CALL OF GUARDIANS AND MISSES, WE WILL COUNT THAT ONE AS A WIN! =="
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

#THIS APPENDS THE RESPONSE FROM RESPONSE_LIST2 SO IT CAN SAVE IT IF THE ATTACK DESCRIPTION IS CALLED AN RESUME FROM WHERE IT LEFT OFF.
#==============================================================================================================================#
response_append =[]

#END OF ROGUE PATH LISTS
#==============================================================================================================================#


response_append =[]

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





#LISTS USED THROUGH ALL PATHS.
#==============================================================================================================================#

#RANDOM BUFF FROM SHRINE
#==============================================================================================================================#
buff_list = ["+25HP", "+10ATK", "-10HP", "-10ATK"]