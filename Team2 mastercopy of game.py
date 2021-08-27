import time
import random
name="Ftmcr" #fill to make code run
#Dale

def sneak():
    print("\nDo you try to sneak in or speak with a guard")
    a=input("\nSneak[Y/N] ")
    if a[0].upper() == "Y":
        return(int(1))
    elif a[0].upper() == "N" :
        return(int(0))
    else:
        print("\nDon't be silly. Please try again")
        return(sneak())

def game_q(d):
    a=input("\nWhile you wait for a response the guard asks you to play noughts and crosses because he's 12 on the inside. Do you accept [Y/N]")
    if a[0].upper() == "Y" and d==0:
        print("\n\"Game on\" says the stupid guard")
        oandx()
        print("\nJust after you finish the game you get buzzed in. \nWell done.")
    elif a[0].upper() == "Y" and d==1:
        print("\nFor to me to let you in, you need to pass a test")
        print("\n\"What is the test then\" you reply")
        print("\nA game of noughts and crosses. Muhahaha")
        print("\n\"Oh, easy\" you reply")
        print("\nWe will see about that")
        oandx()
    elif a[0].upper() == "N" and d==0:
        print("\nYou both stare at each other lovingly but break your gaze when you're buzzed in.")
    elif a[0].upper() == "N" and d==1:
        print("\nFor to me to let you in you need to pass a test")
        print("\n\"What is the test then\" you reply")
        print("\nA game of noughts and crosses. Muhahaha")
        print("\n\"Oh, easy\" you reply")
        print("\nWe will see about that")
        oandx()
        print("\nAsshole, if HQ gives the ok i can let you in")
        time.sleep(2)
        print("\n*You get get buzzed in*")


def game_over(d,b):
    print("\nYOU LOSE")
    print("""                             ...----....
                         ..-:"''         ''"-..
                      .-'                      '-.
                    .'              .     .       '.
                  .'   .          .    .      .    .''.
                .'  .    .       .   .   .     .   . ..:.
              .' .   . .  .       .   .   ..  .   . ....::.
             ..   .   .      .  .    .     .  ..  . ....:IA.
            .:  .   .    .    .  .  .    .. .  .. .. ....:IA.
           .: .   .   ..   .    .     . . .. . ... ....:.:VHA.
           '..  .  .. .   .       .  . .. . .. . .....:.::IHHB.
          .:. .  . .  . .   .  .  . . . ...:.:... .......:HIHMM.
         .:.... .   . ."::"'.. .   .  . .:.:.:II;,. .. ..:IHIMMA
         ':.:..  ..::IHHHHHI::. . .  ...:.::::.,,,. . ....VIMMHM
        .:::I. .AHHHHHHHHHHAI::. .:...,:IIHHHHHHMMMHHL:. . VMMMM
       .:.:V.:IVHHHHHHHMHMHHH::..:" .:HIHHHHHHHHHHHHHMHHA. .VMMM.
       :..V.:IVHHHHHMMHHHHHHHB... . .:VPHHMHHHMMHHHHHHHHHAI.:VMMI
       ::V..:VIHHHHHHMMMHHHHHH. .   .I":IIMHHMMHHHHHHHHHHHAPI:WMM
       ::". .:.HHHHHHHHMMHHHHHI.  . .:..I:MHMMHHHHHHHHHMHV:':H:WM
       :: . :.::IIHHHHHHMMHHHHV  .ABA.:.:IMHMHMMMHMHHHHV:'. .IHWW
       '.  ..:..:.:IHHHHHMMHV" .AVMHMA.:.'VHMMMMHHHHHV:' .  :IHWV
        :.  .:...:".:.:TPP"   .AVMMHMMA.:. "VMMHHHP.:... .. :IVAI
       .:.   '... .:"'   .   ..HMMMHMMMA::. ."VHHI:::....  .:IHW'
       ...  .  . ..:IIPPIH: ..HMMMI.MMMV:I:.  .:ILLH:.. ...:I:IM
     : .   .'"' .:.V". .. .  :HMMM:IMMMI::I. ..:HHIIPPHI::'.P:HM.
     :.  .  .  .. ..:.. .    :AMMM IMMMM..:...:IV":T::I::.".:IHIMA
     'V:.. .. . .. .  .  .   'VMMV..VMMV :....:V:.:..:....::IHHHMH
       "IHH:.II:.. .:. .  . . . " :HB"" . . ..PI:.::.:::..:IHHMMV"
        :IP""HHII:.  .  .    . . .'V:. . . ..:IH:.:.::IHIHHMMMMM"
        :V:. VIMA:I..  .     .  . .. . .  .:.I:I:..:IHHHHMMHHMMM
        :"VI:.VWMA::. .:      .   .. .:. ..:.I::.:IVHHHMMMHMMMMI
        :."VIIHHMMA:.  .   .   .:  .:.. . .:.II:I:AMMMMMMHMMMMMI
        :..VIHIHMMMI...::.,:.,:!"I:!"I!"I!"V:AI:VAMMMMMMHMMMMMM'
        ':.:HIHIMHHA:"!!"I.:AXXXVVXXXXXXXA:."HPHIMMMMHHMHMMMMMV
          V:H:I:MA:W'I :AXXXIXII:IIIISSSSSSXXA.I.VMMMHMHMMMMMM
            'I::IVA ASSSSXSSSSBBSBMBSSSSSSBBMMMBS.VVMMHIMM'"'
             I:: VPAIMSSSSSSSSSBSSSMMBSSSBBMMMMXXI:MMHIMMI
            .I::. "H:XIIXBBMMMMMMMMMMMMMMMMMBXIXXMMPHIIMM'
            :::I.  ':XSSXXIIIIXSSBMBSSXXXIIIXXSMMAMI:.IMM
            :::I:.  .VSSSSSISISISSSBII:ISSSSBMMB:MI:..:MM
            ::.I:.  ':"SSSSSSSISISSXIIXSSSSBMMB:AHI:..MMM.
            ::.I:. . ..:"BBSSSSSSSSSSSSBBBMMMB:AHHI::.HMMI
            :..::.  . ..::":BBBBBSSBBBMMMB:MMMMHHII::IHHMI
            ':.I:... ....:IHHHHHMMMMMMMMMMMMMMMHHIIIIHMMV"
              "V:. ..:...:.IHHHMMMMMMMMMMMMMMMMHHHMHHMHP'
               ':. .:::.:.::III::IHHHHMMMMMHMHMMHHHHM"
                 "::....::.:::..:..::IIIIIHHHHMMMHHMV"
                   "::.::.. .. .  ...:::IIHHMMMMHMV"
                     "V::... . .I::IHHMMV"'
                       '"VHVHHHAHHHHMMV:"'

    """)
    print("\nWould you like to try again?")
    a=input("\nA: Retry \nB: Start from the begining \nC:Quit")
    if a[0].upper() == "R" and b==0:
        factory_sellout(d)
    elif a[0].upper() == "R" and b==1:
        factory_notAsellout(d)
    elif a[0].upper()=="B" :
        start_game() #placeholder for game start loop
    else:
        quit()

def factory():
    print("""                                 d8888888888888888888888"
                                888888888888888888PYP"'
                               d88888888888888888D  
                               8888888888888888P'
                                Y8888888888888b
                               C8888888Y888888P
                                Y88888'd88888"      
                                8888P d8888P 
                               d8888D 88888   
                              d888P'  Y88dP   
                             nY88Pn    Y88            8\"""-----....._____
                             N   +N    88'            8                  NNNNNN8
                             N   +N  nd88n            P                  NNNNNNP
                             N   +N  N  +N           d  dNN   ...       dNNNNNN
     __...---"Nn.            N   +N  N  +N           8  NNP  dNNP  dNN  NNNNNNN
  8""         NNNNn          N   +N  N  +N           8       ""'   NNP  NNNNNNN
  8       oo  NNNNN          N   +N  N  +N           8                  NNNNNNP
  Y  dN   NN  NNNNN          N   +N  N  +N           P       ooo       dNNNNNN
   b NY   ""  YNNNN          N   +N  N  +N          d       dNN'  dNN  NNNNNNN
   8        _  bNNNb         N   +N  N  +N          8       \"""   NNP  NNNNNNN
   8  o8   88  NNNNN         N   +N  N  +N          8                  NNNNNNN
   Y  BP   ""  NNNNN         N   +N  N  +N          8            nnn   NNNNNNP
    b          NNNNN         N   +N  N  +N          P            NNP  dNNNNNN
    8          YNNNN         N   +N  M  +N         d             ""   NNNNNNN
    8           NNNNb        N   +N  N  +N         8                  NNNNNNN
    Y           NNNNN      __N___+N__N  +N         8                  NNNNNNP
     b          NNNNNooooodP\"""\"""\""YNNNNNNbcgmmnnn8                 dNNNNNN
     8          \"""'                         `\"""\""8                 NNNNNNN
     8                                             P                 NNNNNNN
     Y                          NNNNNNNNN         d                  NNNNNNN
      b                         NNNNNNNNN         8                  NNNNNNP
      8                         NNNNNNNNP         8                 dNNNNNN
      8                         NNNNNNNN;         8                 NNNNNNN
      Y                         NNNNNNNN:         P                 NNNNNNN
       b                        NNNNNNNN;        d                  NNNNNNP
       8                        NNNNNNNN         8                 dNNNNNN 
 ______8__........----------\"""\"""\"""\"""------...8..______         NNNNNNN
_________........----------\"""\"""\"""\"""------......_____  \""\"""----NNNNNNN
                                                         \"""\""----....___ \"""--
                                                                         \"""---
    """)

def computer():
    print("""
                           .,,uod8B8bou,,.
              ..,uod8BBBBBBBBBBBBBBBBRPFT?l!i:.
         ,=m8BBBBBBBBBBBBBBBRPFT?!||||||||||||||
         !...:!TVBBBRPFT||||||||||!!^^""'   ||||
         !.......:!?|||||!!^^""'            ||||
         !.........||||                     ||||
         !.........||||  ##                 ||||
         !.........||||                     ||||
         !.........||||                     ||||
         !.........||||                     ||||
         !.........||||                     ||||
         `.........||||                    ,||||
          .;.......||||               _.-!!|||||
   .,uodWBBBBb.....||||       _.-!!|||||||||!:'
!YBBBBBBBBBBBBBBb..!|||:..-!!|||||||!iof68BBBBBb....
!..YBBBBBBBBBBBBBBb!!||||||||!iof68BBBBBBRPFT?!::   `.
!....YBBBBBBBBBBBBBBbaaitf68BBBBBBRPFT?!:::::::::     `.
!......YBBBBBBBBBBBBBBBBBBBRPFT?!::::::;:!^"`;:::       `.
!........YBBBBBBBBBBRPFT?!::::::::::^''...::::::;         iBBbo.
`..........YBRPFT?!::::::::::::::::::::::::;iof68bo.      WBBBBbo.
  `..........:::::::::::::::::::::::;iof688888888888b.     `YBBBP^'
    `........::::::::::::::::;iof688888888888888888888b.     `
      `......:::::::::;iof688888888888888888888888888888b.
        `....:::;iof688888888888888888888888888888888899fT!
          `..::!8888888888888888888888888888888899fT|!^"'
            `' !!988888888888888888888888899fT|!^"'
                `!!8888888888888888899fT|!^"'
                  `!988888888899fT|!^"'
                    `!9899fT|!^"'
                      `!^"'
    """)

def bang(d):
    print("""
     \\
 /                                 />
 \\__+_____________________/\\/\\___/ /|
 ()______________________      / /|/\\
             /0 0  ---- |----    /---\\
            |0 o 0 ----|| - \ --|      \\
             \0_0/____/ |    |  |\      \\
                         \__/__/  |      \\
Bang! Bang!                       |       \\
                                  |         \\
                                  |__________|
    """)
    print("You where killed by the Boss")
    print("\nWould you like to try again?")
    a=input("\nA: Retry \nB: Start from the begining \nC:Quit")
    if a[0].upper() == "R":
        factory_notAsellout(d)
    elif a[0].upper()=="B" :
        start_game() #placeholder for game start loop
    else:
        quit()

def factory_sellout(d):
    factory()
    print("\nAs you make your way to the vaccine factory you notice there isn't much secuirty tonight. They must be saying goodbye to their loved ones.")
    time.sleep(2)
    print("\nYou forgot your ID, you'll have to sneak in")
    a=sneak()
    if a==1 and d==0:
        print("\nNot just a pretty face.\nYou're in.")
    elif a==1 and d==1 :
        print("\nWow, you call that sneaking in?\nA guard shot you.\nYou die.")
        game_over(d,int(0))
    elif a== 0 and d==0 :
        print("\nYou walk up to the entrance and start talking to the guard, the guard recognizes you but can't let you in without your ID, he calls up for clearance")
        time.sleep(1)
        game_q(d)
    else:
        print("\nYou walk up to the entrance and start talking to the guard, the guard recognizes you but can't let you in without your ID, he calls up for clearance")
        game_q(d)
    time.sleep(2)
    print("\nAs you are walking to the production line you hear your Boss talking on the phone \n\"£100,000,000 is only a drop in the ocean compared to what we're going to make\"")
    question_boss()

def factory_notAsellout(d):
    factory()
    print("\nAs you make your way to the vaccine factory you notice there isn't much secuirty tonight. They must be saying goodbye to their loved ones.")
    time.sleep(2)
    print("\nYou forgot your ID, you'll have to sneak in")
    a=sneak()
    if a==1 and d==0:
        print("\nNot just a pretty face.\nYou're in.")
    elif a==1 and d==1 :
        print("\nWow, you call that sneaking in?\nA guard shot you.\nYou die.")
        game_over(d,int(1))
    elif a== 0 and d==0 :
        print("\nYou walk up to the entrance and start talking to the guard, the guard recognizes you but can't let you in without your ID, he calls up for clearance")
        time.sleep(1)
        game_q(d)
    else:
        print("\nYou walk up to the entrance and start talking to the guard, the guard recognizes you but can't let you in without your ID, he calls up for clearance")
        game_q(d)
    time.sleep(2)
    print("\nAs you are walking to the production line you hear your Boss talking on the phone \n\"£100,000,000 is only a drop in the ocean compared to what we're going to make\"")
    question_boss_n(d)

def question_boss_n(d):
    print("""\nWhat are you going to do? [A,B or C]
    
    A - Ask your boss for help
    B - Carry on listening
    C - Continue to the production line
    """)
    a=input("A, B or C")
    if a[0].upper()=="A" or a[0].upper()=="B" or a[0].upper()=="C":
        boss_a_n()
    elif a[0].upper()=="B" :
        boss_b_n()
    elif a[0].upper()=="C" :
        boss_c_n()
    else:
        return(question_boss_n())

def boss_a():
    print("\n\"Fancy meeting you here, Boss. Let me give you a hand\"")
    print("\nYour Boss turns around as white a ghost.\n\"I take it you heard that\"")
    time.sleep(2)
    print("\n\"I need you to swap the vaccine formala with this one. 50 percent of all the people that take it will die. You can pin it on Ivan.\"")
    control_room(int(1))

def boss_a_n(d):
    print("\n\"Fancy meeting you here, Boss. Let me give you a hand\"")
    print("\nYour Boss turns around as white a ghost.\n\"I take it you heard that\"")
    time.sleep(2)
    print("\n\"I need you to swap the vaccine formala with this one. 50 percent of all the people that take it will die. You can pin it on Ivan.\"")
    bang(d)

def boss_b_n():
    print("\nYou hear of a plan to swap the vaccine for a version that will kill 50 percent of people that take it, using Ivan as the fall guy")
    time.sleep(1)
    print("\nAfter a few more seconds of the conversation you decide that you liked Ivan anyway so you carry on shilst whistling the tune of WAP by Cardi B")
    control_room_n(int(2))

def boss_c_n():
    print("You carry on thinking to yourself so the boss is the person behind the women who would of thought")
    control_room_n(int(3))

def control_room_n(a):
    print("\nAs you enter the main production room you spot the super-old control PC and fancy some nostalgia")
    time.sleep(2)
    computer()
    global boss_reply
    if a == 2 :
        print(f"As you start to log into your account you think to back to the interaction you had with the Boss earler in the day {boss_reply}")
        print("You have opened the file containing the instuctions on how to make the vaccine what will you do")
        vaccine_edit_pharma_n(a,boss_reply)
    else:
        print(f"As you start to log into your account you think to back to the interaction you had with the Boss earler in the day {boss_reply}")
        print("You have opened the file containing the instuctions on how to make the vaccine what will you do")
        vaccine_edit_pharma_n(a,boss_reply)

def input_cheek_n(a,b,c):
    if (c[0].upper()=="A" or c[0].upper()=="B" or c[0].upper()=="C") and b=="C":
        ""
    elif (c[0].upper()=="A" or c[0].upper()=="B") and b!="C":
        ""
    else:
        return(vaccine_edit_pharma_n(a,b))

def vaccine_edit_pharma_n(a,b):
    if a==2 and b!="C":
        print("""
        A - Fix the vaccine and report the Boss
        B - Fix the vaccine but don't report the Boss
        C - Don't fix the vaccine and report the Boss
        """)
        c=input()
        input_cheek_n(a,b,c)
        c=c[0].upper()
        end_game_pharma_n(a,c)
    elif a==2:
        print("""
        A - Fix the vaccine but don't report the Boss
        B - Don't fix the vaccine and don't report the Boss
        """)
        c=input()
        input_cheek_n(a,b,c)
        if c[0].upper()=="A":
            c="B"
        else:
            c="D"
        c=c[0].upper()
        end_game_pharma_n(a,c)
    elif a==3:
        print("After looking thought the vaccine you notice it has been changed")
        print("""
        A - Fix the vaccine and report the Boss
        B - Fix the vaccine but don't report the Boss
        C - Don't fix the vaccine and report the Boss
        """)
        c=input()
        input_cheek(a,b,c)
        c=c[0].upper()
        end_game_pharma_n(a,c)
   
def end_game_pharma(a,c):
    if a==1 and c=="A":
        print("\nYou carry out the plan. \nA few days go by and you see news on the TV that the company have a cure for Covid 50.")
        time.sleep(1)
        print("\nA week since mass vaccination.\nThe vaccine is killing half the people who take it")
        time.sleep(1)
        print("\nA month passes. An investagation finds the vaccine lethal and pins the blame on Ivan")
        print("Your mother rings you telling you that she has just been vaccinated.")
        time.sleep(1)
        print("RIP Mum.")
        end_game()
    elif a==1 and c=="B":
        print("\nYou carry out the plan. \nA few days go by and you see news on the TV that the company have a cure for Covid 50.")
        time.sleep(1)
        print("\nA week since mass vaccination.\nThe vaccine is killing half the people who take it")
        time.sleep(1)
        print("\nA month passes. An investagation finds the vaccine lethal and pins the blame on Ivan and your Boss. You get away with it.")
        time.sleep(1)
        print("Your mother rings you telling you that she has just been vaccinated.")
        time.sleep(1)
        print("RIP Mum.")
        end_game()
    elif c=="C":
        print("The police storm into the factory. At first you think it is a strippergram but realise it's real when they arrest the Boss")
        time.sleep(1)
        print("\nYou carry out the plan. \nA few days go by and you see news on the TV that the company have a cure for Covid 50.")
        time.sleep(1)
        print("A week after vaccine rollout, everybody is cured")
        print("Well done. You did it.")
        end_game()
    elif (a==2 or a==3) and c=="A":
        print("\nYou carry out the plan. \nA few days go by and you see news on the TV that the company have a cure for Covid 50.")
        time.sleep(1)
        print("\nA week since mass vaccination.\nThe vaccine is killing half the people who take it")
        time.sleep(1)
        print(f"It has now been a mouth since the vaccine roll out. An investagation found the vaccine was modified by a Boss named Pants Mc'Pantyface and employee named {name}")
        time.sleep(1)
        print("Enjoy jail, murderer.")
        end_game()
    elif (a==2 or a==3) and c=="B":
        print("\nYou carry out the plan. \nA few days go by and you see news on the TV that the company have a cure for Covid 50.")
        time.sleep(1)
        print("\nA week since mass vaccination.\nThe vaccine is killing half the people who take it")
        time.sleep(1)
        print(f"It has now been a mouth since the vaccine roll out. An investagation found the vaccine was modified by a Boss named Pants Mc'Pantyface and employee named {name}")
        time.sleep(1)
        print("Enjoy jail, murderer.")
        end_game()

def end_game_pharma_n(a,c):
    if (a== 2 or a==3) and c=="A":
        print("You have fixed the vaccine. \n The police storm into the factory. At first you think it is a strippergram but realise it's real when they arrest the Boss")
        time.sleep(1)
        print("\nA few days go by and you see news on the TV that the company have a cure for Covid 50.")
        time.sleep(1)
        print("A week after vaccine rollout, everybody is cured")
        print("Well done. You did it.")
        end_game()
    elif (a== 2 or a==3) and c=="B":
        print("You have fixed the vaccine")
        time.sleep(1)
        print("\nA few days go by and you see news on the TV that the company have a cure for Covid 50.")
        time.sleep(1)
        print("A week after vaccine rollout, everybody is cured")
        print("Well done. You did it.")
        end_game()
    elif (a== 2 or a==3) and c=="C":
        print("You could have fixed the vaccine but you didn't. \nGreat.. \nThe police arrive at the factory and arrest the Boss")
        time.sleep(1)
        print("It has now been a few days since the vaccine roll out. An investagation found the vaccine was modified by a Boss named Pants Mc'Pantyface")
        time.sleep(1)
        print("A week since the \'vaccine\' rollout. Mass deaths reported globally.")
        print("Your mother rings to tell you she has contracted Covid 50")
        time.sleep(1)
        print("RIP Mum.")
        end_game()
    else:
        print("You could have fixed the vaccine but you didn't. \nGreat.. ")
        time.sleep(1)
        print("It has been a few days since the incident at the factory, nobody has a clue who did it. ")
        time.sleep(1)
        print("A week since the \'vaccine\' rollout. Mass deaths reported globally.")
        print("Your mother rings to tell you she has contracted Covid 50")
        time.sleep(1)
        print("RIP Mum.")
        end_game()


def question_boss():
    print("""\nWhat are you going to do? [A,B or C]
    
    A - Ask your boss for help
    B - Carry on listening
    C - Continue to the production line
    """)
    a=input("A, B or C")
    if a[0].upper()=="A" or a[0].upper()=="B" or a[0].upper()=="C":
        boss_a()
    elif a[0].upper()=="B" :
        boss_b()
    elif a[0].upper()=="C" :
        boss_c()
    else:
        return(question_boss())


def boss_b():
    print("\nAs you keep listening you hear of the plan to swap the vaccine for a version that will kill 50 percent of people and he is planing to use Ivan as the fall guy")
    time.sleep(1)
    print("\nAfter a few more seconds of the conversation you decide that you liked Ivan anyway so you carry on shilst whistling the tune of WAP by Cardi B")
    control_room(int(2))

def boss_c():
    print("\nYou carry on to the production line, unphased\nBecasue you're as cold as ice, baby.")
    control_room(int(3))

def control_room(a):
    print("\nAs you enter the main production room you spot the super-old control PC and fancy some nostalgia")
    time.sleep(2)
    computer()
    global boss_reply
    if a == 1 :
        print(f"\nAs you log into the PC with Ivan's details (hehe) account you are happy in the knowledge he will get the blame {boss_reply}")
        time.sleep(2)
        print("\nYou gain access to the vaccine formulation part of the PC program or whatever.")
        vaccine_edit_pharma(a,boss_reply)
    elif a == 2 :
        print(f"\nAs you log into your account you realise that it's probably time for a career change. Remember what the boss said, {boss_reply}")
        print("\nYou gain access to the vaccine formulation part of the PC program or whatever.")
        vaccine_edit_pharma(a,boss_reply)
    else:
        print(f"\nAs you log into your account you realise that you're happy half the world will die because they're probably weirdos anyway. Remember what the boss said, {boss_reply}")
        print("\nYou gain access to the vaccine formulation part of the PC program or whatever")
        vaccine_edit_pharma(a,boss_reply)

def vaccine_edit_pharma(a,b):
    if (a==1 or a==2) and b!="C":
        print("""What do you do?[A, B or C]
        
        A - Carry out the plan
        B - Carry out the plan but take the Boss' cut
        C - Don't carry out the plan and report the Boss
        """)
        c=input()
        input_cheek(a,b,c)
    elif a==1:
        print("""What do you do?[A or B]
        
        A - Carry out the plan
        B - Don't carry out the plan and report the Boss
        """)
        c=input()
        input_cheek(a,b,c)
        if c[0].upper()=="B":
            c="C"
        c=c[0].upper()
        end_game_pharma(a,c)
    elif a==3 and b!="C":
        print("""What do you do?[A, B or C]
        
        A - Carry out the plan
        B - Carry out the plan but take the Boss' cut
        C - Don't carry out the plan and report the Boss
        """)
        c=input()
        input_cheek(a,b,c)
        c=c[0].upper()
        end_game_pharma(a,c)
    else:
        print("""What do you do?[A or B]
        
        A - Carry out the plan
        B - Don't carry out the plan and report the Boss
        """)
        c=input()
        input_cheek(a,b,c)
        if c[0].upper()=="B":
            c="C"
        c=c[0].upper()
        end_game_pharma(a,c)

def input_cheek(a,b,c):
    if (c[0].upper()=="A" or c[0].upper()=="B" or c[0].upper()=="C") and b!="C":
        ""
    elif (c[0].upper()=="A" or c[0].upper()=="B") and b=="C":
        ""
    else:
        return(vaccine_edit_pharma(a,b))

def end_game():
    print("""
___________.__                   __     _____.___.                _____                     .__                .__                 
\__    ___/|  |__ _____    ____ |  | __ \__  |   | ____  __ __  _/ ____\___________  ______ |  | _____  ___.__.|__| ____    ____   
  |    |   |  |  \\__  \  /    \|  |/ /  /   |   |/  _ \|  |  \ \   __\/  _ \_  __ \ \____ \|  | \__  \<   |  ||  |/    \  / ___\  
  |    |   |   Y  \/ __ \|   |  \    <   \____   (  <_> )  |  /  |  | (  <_> )  | \/ |  |_> >  |__/ __ \\___  ||  |   |  \/ /_/  > 
  |____|   |___|  (____  /___|  /__|_ \  / ______|\____/|____/   |__|  \____/|__|    |   __/|____(____  / ____||__|___|  /\___  /  
                \/     \/     \/     \/  \/                                          |__|             \/\/             \//_____/   
___________                     ________     ________                                                                              
\__    ___/___ _____    _____   \_____  \   /  _____/_____    _____   ____                                                         
  |    |_/ __ \\__  \  /     \   /  ____/  /   \  ___\__  \  /     \_/ __ \                                                        
  |    |\  ___/ / __ \|  Y Y  \ /       \  \    \_\  \/ __ \|  Y Y  \  ___/                                                        
  |____| \___  >____  /__|_|  / \_______ \  \______  (____  /__|_|  /\___  >                                                       
             \/     \/      \/          \/         \/     \/      \/     \/                                                        
_________            .___      _______          __  .__                _________                                                   
\_   ___ \  ____   __| _/____  \      \ _____ _/  |_|__| ____   ____   \_   ___ \  ____  __ _________  ______ ____                 
/    \  \/ /  _ \ / __ |/ __ \ /   |   \\__  \\   __\  |/  _ \ /    \  /    \  \/ /  _ \|  |  \_  __ \/  ___// __ \                
\     \___(  <_> ) /_/ \  ___//    |    \/ __ \|  | |  (  <_> )   |  \ \     \___(  <_> )  |  /|  | \/\___ \\  ___/                
 \______  /\____/\____ |\___  >____|__  (____  /__| |__|\____/|___|  /  \______  /\____/|____/ |__|  /____  >\___  >               
        \/            \/    \/        \/     \/                    \/          \/                         \/     \/                
________   .________     /\   ______       /\ ________  ____________                                                               
\_____  \  |   ____/    / /  /  __  \     / / \_____  \/_   \_____  \                                                              
 /  ____/  |____  \    / /   >      <    / /   /  ____/ |   |/  ____/                                                              
/       \  /       \  / /   /   --   \  / /   /       \ |   /       \                                                              
\_______ \/______  / / /    \______  / / /    \_______ \|___\_______ \                                                             
        \/       \/  \/            \/  \/             \/            \/                                                             
    """)
    
def answ():
    user_answer=input()
    if user_answer.upper()=="Y":
        oandx()
    
def win_check():
    for x in win_lines:
        #print("test",x)
        xt.clear()
        yt.clear()
        if turn==10:
            print("\nThe game was a draw")
            print("\nWould you like to play again [Yes/Y] or move on? on [type anything to continue]")
            answ()
            return(1)
        for y in range(len(x)):
            #print("y",y)
            #print("x",x)
            xt.append(grid_replace[x[y]-1][0])
            yt.append(grid_replace[x[y]-1][1])
            #print(yt)
        if grid[xt[0]][yt[0]]==grid[xt[1]][yt[1]]==grid[xt[2]][yt[2]] and not grid[xt[0]][yt[0]]==" " and not grid[xt[1]][yt[1]]==" " and not grid[xt[2]][yt[2]]==" ":

            if grid[xt[0]][yt[0]] == "X":
                print(f"\n{name}, you have won, you big winner, you")
            else:
                print("\nThe guard has won")  
            print("\nWould you like to play again [Yes/Y] or move on? [type anything to continue]")
            answ()
            return(1)
    return(0)
           
def O_input():
    #print(unused_space)
    pick=""
    pick=random.choice(unused_space)
    print(pick)
    if int(pick) in unused_space:
        space[int(pick)-1]="O"
        lx=grid_replace[int(pick)-1][0]
        ly=grid_replace[int(pick)-1][1]
        return(lx,ly)
    else:
        print("\nSomething has gone wrong")
        #exit()

def X_input():
    print(unused_space)
    pick=input()
    if pick=="":
        print("\nChoose a valid number, idiot")
        l=X_input()
        return(l[0],l[1])
    if not int(pick) in unused_space:
        print("\nChoose a valid number, idiot")
        l=X_input()
        return(l[0],l[1])
    elif int(pick) in unused_space:
        space[int(pick)-1]="X"
        lx=grid_replace[int(pick)-1][0]
        ly=grid_replace[int(pick)-1][1]
        return(lx,ly)
    else:
        print("\nSomething has gone wrong")
        #exit()

def oandx():
    global space
    global grid
    global grid_replace
    global win_lines
    global turn
    global unused_space
    global pick
    global lx
    global ly
    global line
    global eline
    global esline
    global xt
    global yt
    space=[1,2,3,4,5,6,7,8,9]
    grid=[[],[],[],[],[],[],[],[],[],[],[]]
    grid_replace=[[1,1],[1,5],[1,9],[5,1],[5,5],[5,9],[9,1],[9,5],[9,9]]
    win_lines=[[1,2,3],[1,5,9],[1,4,7],[2,5,8],[3,5,7],[3,6,9],[4,5,6],[7,8,9]]
    turn= int(0)
    unused_space=[]
    pick=""
    lx=int(0)
    ly=int(0)
    line=[]
    eline=[]
    esline=""
    xt=[]
    yt=[]
    for x in [0,1,2,4,5,6,8,9,10]:
        grid[x]=" "" "" ""|"" "" "" ""|"" "" "" "
    for x in [3,7]:
        grid[x] ="------------"
    for x in range(11):
        print(grid[x])
    print("\nThe grid is numbered from left to right")
    print("\n1 2 3")
    print("\n4 5 6")
    print("\n7 8 9")
    for x in range(9):
        if turn%2 ==0:
            print(turn)
            #unused_space=[]
            print(f"\n{name}'s turn")
            for x in range(9):
                if not (space[x]=="X" or space[x]=="O"):
                    unused_space.append(space[x])
                else:
                    ""
            print("\nType the number of the sapce in which you would like to place your X")
            #print(unused_space)
            l=X_input()
            line=grid[l[0]]
            eline.clear()
            for x in range(len(line)):
                if x==l[1]:
                    eline+="X"
                else:
                    eline+=line[x]
            esline="".join(eline)
            grid[int(l[0])]=esline
            for x in range(11):
                print(grid[x])
            unused_space=[]
            turn += 1
        elif turn%2 != 0:
            unused_space=[]
            print("\nGuard's turn")
            for x in range(9):
                if not (space[x]=="X" or space[x]=="O"):
                    unused_space.append(space[x]) 
                else:
                    ""
            print("\nType the number of the sapce in which you would like to place your X")
            #print(unused_space)
            l=O_input()
            line=grid[l[0]]
            eline.clear()
            for x in range(len(line)):
                if x==l[1]:
                    eline+="O"
                else:
                    eline+=line[x]
            esline="".join(eline)
            grid[int(l[0])]=esline
            for x in range(11):
               print(grid[x])
            unused_space=[]
            turn+=1
        cheek=win_check()
        if cheek==1:
            return()

def reply():
    i=input("\nDo you accept? [Y/N] ")
    if i[0].upper() == "Y" :
        print("\nYou make a good offer, I accept.")
        return(int(1))
    elif i[0].upper() == "N" :
        print("\nSorry but no matter what, I will never betray my company. I'm a droid and a jobsworth, hehe.")
        return(int(0))
    else:
        print("\Invalid input. Please try again")
        return(reply())

def drink_r(r, drink):
    if r == 1 :
        print("\nAfter accepting the deal do you celebrate some more or get to work?")
        i=input("\nCelebrate [Y] \nGet to work [N]")
        if i[0].upper() == "Y" :
            print(f"\nBartender get me another {drink}")
            return(int(1))
        elif i[0].upper() == "N" :
            print("\nWell thanks for the drink I best get going.")
            return(int(0))
        else:
            print("\Invalid input. Please try again")
            return(drink_r())
    elif r == 0 :
        print("\nCarry on celebrating, ignoring what she said or go to the factory to make sure everything is fine")
        i=input("\nCelebrate [Y] \nGet to work [N]")
        if i[0].upper() == "Y" :
            print(f"\nBartender get me another {drink}")
            time.sleep(1)
            print("\nAfter a few drinks you realize that they are planning to do something at the factory")
            return(int(1))
        elif i[0].upper() == "N" :
            print("\nWell thanks for the drink I best get going.")
            return(int(0))
        else:
            print("\nInvalid input. Please try again")
            return(drink_r())

def next_area(r,d) :
    if r == 1 :
        factory_sellout(d)
    else:
        factory_notAsellout(d) 

def bar_big_pharma() :
    print("\nAs you enter the bar you notice that there aren't many people here. You notice a woman wearing a fancy shmancy suit")
    time.sleep(1)
    print("""      .======================================.
      | ___ ___ ___               _   _   _  |
      | \_/ \_/ \_/ C|||C|||C||| |-| |-| |-| |
      | _|_ _|_ _|_  ||| ||| ||| |_| |_| |_| |
      '===================================== ,sSSSs
                DUFFY'S WATERING HOLE       SSSS "(
           .:.                              SSS@ =/  \~/
          C|||'                             SSSS_(_  _Y_
        ___|||______________________________SS/ _)_) /.-
       [____________________________________] \   /\//
        |   ____    ____    ____    ____   | \|==(\_/
        |  (____)  (____)  (____)  (____)  | (/   ;
        |  |    |  |    |  |    |  |    |  | |____|
        |  |    |  |    |  |    |  |    |  |  \  |\\
        |  |    |  |    |  |    |  |    |  |   ) ) )
        |  |____|  |____|  |____|  |____|  |  (  |/
        |  I====I  I====I  I====I  I====I  |  /\ |
           |    |  |    |  |    |  |    |  | /.(=\\
                                               Y\_\\
    """)
    print("\nYou make your way over to the bar to order a drink")
    drink=input("\nBeer, Wiskey, Wine ")
    print(f"\nThe bartender hands you your {drink}, \"That'll be £10\"")
    time.sleep(2)
    print(f"\nAs you reach for your wallet the woman stops you and adds it to her tab, \n\"I will pay for {name}\'s drink\", \n \"How did you know my name?\" you ask")
    time.sleep(2)
    print("\nShe laughs and points at your nametag")
    time.sleep(2)
    print("\nYou reach for your tag, realizing it isn't there")
    time.sleep(2)
    print("\nMy boss sent me with an opportunity for you. \nWe know that you finished your work on the vaccine and we are willing to pay you a large sum of money for the formlioli, ravoili, ravioli")
    time.sleep(2)
    print("\n*She slides a note across the bar*")
    time.sleep(2)
    print(""".-=~=-.                                                                 .-=~=-.
(__  _)-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-(__  _)
( _ __)                                                                 ( _ __)
(__  _)                                                                 (__  _)
(_ ___)                                                                 (_ ___)
(__  _)                                                                 (__  _)
( _ __)      ___  __  ___   ___   ___   ___   ___   ___   ___   ___     ( _ __)
(__  _)     / ,_\/_ |/ _ \ / _ \ / _ \ / _ \ / _ \ / _ \ / _ \ / _ \    (__  _)
(_ ___)   _| |_   | | | | | | | | | | | | | | | | | | | | | | | | | |   (_ ___)
(__  _)  |__ __|  | | | | | | | | | | | | | | | | | | | | | | | | | |   (__  _)
( _ __)    | |____| | |_| | |_| | |_| | |_| | |_| | |_| | |_| | |_| |   ( _ __)
(__  _)   (_,_____|_|\___/ \___/ \___/ \___/ \___/ \___/ \___/ \___/    (__  _)
(_ ___)                                                                 (_ ___)
(__  _)                                                                 (__  _)
( _ __)                                                                 ( _ __)
( _ __)                                                                 ( _ __)
(__  _)                                                                 (__  _)
(_ ___)-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-=-._.-(_ ___)
`-._.-'                                                                 `-._.-'
   """)
    time.sleep(1)
    print("\nYou take a moment to process that sum. You haven't seen that many zeros since the girls rated your looks in highschool.")
    r=reply()
    if r == 1:
        print("\nMy boss will be very pleased.\nYou need to stop your company factory from making the vaccine and bring us a copy")
    elif r == 0:
        print("\nMy boss won't be happy. You'll regret this. \n Enjoy watching everyone you love die of this virus, sweetheart.")
    d=drink_r(r,drink)
    if r==1:
        factory_sellout(d)
    elif r== 0 :
        factory_notAsellout(d)

def riddle_q():
    i=int(0)
    return(q_r(i))
    
def q_r(i):
    if  i>=3:       
        print("\n*Ivan angrily walks off*")
        return(int(0))
    print("\n3 answers come to mind")
    print("""\nA - Clown
\nB - Human
\nC - Stool""")
    riddle=input("\nIs your answer A, B or C? ")  
    if riddle[0].upper() == "A":
        print("\nA Clown. They have 4 wheels on their way to work, 2 legs at work and 3 wheels on the tricycle")
        time.sleep(1)
        print("\n*Ivan facepalms* \n\"How the hell did you get a job here?\"")
        return(int(0))
    elif riddle[0].upper() == "B":
        print("\nA Human. They crawl on all fours as a baby, walk on two as an adult and use a walking sticks in old age")
        time.sleep(1)
        print("\nIvan begrudgingly gives you the forula he has, but tell you it isn't perfect")
        return(int(1))
    elif riddle[0].upper() == "C" :
        print("\nA Stool, 4 legs when sat on properly, 2 legs when leaned back on, and 3 legs when one breaks")
        time.sleep(1)
        print("\nIvan call you stupid. \nBut you already knew that.")
        return(int(0))
    elif i<=3 :
        print("\nYou stop your self before any sound could come out, realizing what you were about to say made no sense.")
        i+=1
        return(q_r(i))
    

def questions(a):
    if a == 1 :
        print("\nAs you look at Ivan's work you think to yourself, \'He might be an ass but he is good at what he does.\'")
        time.sleep(1)
        print("\nAs some time passes you notice that the Dihydrogen Monoxide levels are too high")
        a+=q_1()
        a+=q_2()
    else:
        print("\nAs Ivan walks off you thgink yo yourself, \'Ivan is an ass.\'")
        print("\nAs some time passes you cool off. \nYou notice the Dihydrogen Monoxide levels are too high")
        a+=q_1()
        a+=q_2()
    return(int(a))

def q_1():
    print("\nDo you \nA - increase \nB - decrease the protin levels")
    q=input("\n[A/B] ")
    if q[0].upper() == "A" :
        print("\nYou have increased the protein levels")
        return(int(1))
    elif q[0].upper() == "B" :
        print("\nYou have decreased the protein levels")
        return(int(0))

def q_2():
    print("\nDo you decrease the Dihydrogen Monoxide levels by \nA - 10 percent or \nB - 20 percent")
    q=input("\n[A/B] ")
    if q[0].upper() == "A" :
        print("\nYou have decreased the Dihydrogen Monoxide levels by 10%")
        return(int(1))
    elif q[0].upper() == "B" :
        print("\nYou have decreased the Dihydrogen Monoxide levels by 20%")
        return(int(0))

def Lab():
    a = int(0)
    print("\nAs you enter your lab you are greeted by the usual sounds of lab mice and Ivan making too much noise. \nAs usual.")
    time.sleep(1)
    print("""                    _..._                  
                   //''\\\                 
                   ||. .||                 
                   |\ _ /|      (          
                  .-/\ /\-.     )   |      
                 |  ` \ '  |    _   |      
           (     | |  |  | |    H=--+-     
           ))    | |__|[ | |    U   |      
           __    \___(_3/ /     )   |      
-|_H_H_|---||---------|!|/------|---|---.  
 |_U_U_|  /__\        |_|      _[_ _|__  \ 
------------------------------------------`
    """) 
    time.sleep(1)
    print("\nAs you walk past the mice you notice they are more lively than usual. Maybe Ivan has done something")
    time.sleep(1)
    print("\nAfter waiting 5 seconds for a reply you clear your throat and ask again")
    print("\nIvan acts surprised \n\"Ho I didn't notice you come in\"")
    time.sleep(1)
    print("\nMaybe I did something to the mice, maybe I didn't. \nAnswer this questions and I will tell you")
    print("\nWhat has 4 legs in the morning 2 in the afternoon and 3 at night")
    time.sleep(1)
    a+=riddle_q()
    a+=questions(a)
    time.sleep(1)
    print("\n*Machine beeps* \nThe new batch of test vaccines are ready. \nYou head to the Animal testing Lab")
    if a >= 2 :
        animal_room() #this is temporary place holder function call for good path to animal lab
    else:
        animal_room() #this is temporary place holder function call for good path to animal lab

def player_name():
    print("Who are you?\nEnter your Name")
    global name
    name=input()
    a=input(f"Are you sure your name is {name}? [Y/N] ")
    if a[0].upper()=="Y":
        return()
    else:
        player_name()
#Dale

#Nazmi
answer_yes = ["Yes", "Y", "yes", "y"]
answer_no = ["No", "N", "no", "n"]

def animal_room():
    print("""
    WELCOME TO THE ANIMAL TESTING ROOM! 

                   _                 _   _______        _   _               _____                       
       /\         (_)               | | |__   __|      | | (_)             |  __ \                      
      /  \   _ __  _ _ __ ___   __ _| |    | | ___  ___| |_ _ _ __   __ _  | |__) |___   ___  _ __ ___  
     / /\ \ | '_ \| | '_ ` _ \ / _` | |    | |/ _ \/ __| __| | '_ \ / _` | |  _  // _ \ / _ \| '_ ` _ \ 
    / ____ \| | | | | | | | | | (_| | |    | |  __/\__ \ |_| | | | | (_| | | | \ \ (_) | (_) | | | | | |
   /_/    \_\_| |_|_|_| |_| |_|\__,_|_|    |_|\___||___/\__|_|_| |_|\__, | |_|  \_\___/ \___/|_| |_| |_|
                                                                    __/  |                              
                                                                    |___/    
            /~~~~~~~~\                            _
        ##\__/ @)      ~~~~~~~~\                     \ \ ) )    
        |              /~~\~~~~~                ((    |  
        \    /           |                          /   |
        (~~~   /         \____________/~~~~~~~~~~~~   /
        ~~~~|~                                     /
            :                                      |
                \                                     |
                |                               /      
                \  \_         :         \     /~~~\    |
                /   :~~~~~|   :~~~~~~~~~~|   :     :   :
                /    :    /    :         /    :    /    :
            (~~~     )(~~~     )     (~~~     )(~~~     )
            ~~~~~~~~  ~~~~~~~~       ~~~~~~~~  ~~~~~~~~
            


    You entered a room full of animals, they all start jeering at your arrival.

    Some of them see you as a friend,
    Some of them see you as food, 
    Some of them see you as a potential mate. Those are your favourites...

    You must test the vaccine on these poor, defenseless animals.

    We know poking animals with a needle isn't exactly a hobby...

    Do you want to continue? [Y/N]
    """)

    ans1 = input(">>")

    if ans1 in answer_yes:        
        print("Congratulations! By poking one of the animals you calmed it down! You made progress!")
        question_2(ans1)
    elif ans1 in answer_no:
        print("\nIf you don't do it, all of humanity will be die! It's either us or them. \nWould you like to start a new Game? [Y/N]")
        animal_room()
        #ans1 = input(">>")
    else:
        print("I didn't recognise that")
        animal_room()
    
    #ans1 = input(">>")

def question_2(ans1):
    ans1
    if ans1 in answer_yes:
        print("""
        All of a sudden the ghost of a dog called Dogzilla that dies during yesterday\'s tests appears and tries to mount you! 
        
        You have to decide whether to:  
        A) Mount him back
        B) Offer him a treat to try and hopes he forgets about humping you
        C) Offer him the vaccine """)
        
       
        ans1 = input(">>")
        
    if ans1.upper() == "A":
        print("""The animals became rowdy and extremely horny. This pleases you.

        They escape their cages, wanting a piece of the action.

        You need to be brave and mount him back! How bad it can be huh?? 
        
        *\'Everybody hurts\' starts playing on the lab speakers*""")
        
        print("""You carefully approach a tiger and find a bald spot caused by the virus.

        Just before you push your needle into the tiger, he says \'I love you.\' 
        
        You think this is weird but so is your entire life.
        
        The tiger slowly goes to sleep and his normal colour starts returning, 
        
        *Borat voice* 
        Great success! """)
        first_riddle(ans1)
       
        ans1 = input(">>")
    elif ans1.upper() == "B":
        print("Come on don't be stingy! Give him the last cookie that you've hidden in your pocket, you know you want to.")
        print("test0")
        first_riddle(ans1) 
    elif ans1.upper() == "C":
        print("You vaccinated the animals. They are virus-free, baby.")
        first_riddle(ans1)
    else:
        print("Invalid input! Would you like to try again? [Y/N]")
        ans1 = input(">>")
        if ans1 == "no": 
            animal_room()
        else:
            question_2(ans1)

        
        ans1 = input(">>")

def first_riddle(ans1):
    print("test1")
    if ans1 in answer_yes:
        print("\nOK, let me ask you a riddle!")
        print("test2")
        question_2(ans1)
    print("""You proceed to give the rest of the animals the test vaccine.

         Suddenly you slip on a banana skin left by a gorilla. 
         
         Gorilla Koko is angry and want to attack

         Gorilla Koko makes you a one time deal.
         
         If you solve her riddle, she will let you live. 
         Otherwise start praying!
         
         Press enter to see the riddle

        """)
    ans1 = input("""After a train crash, every single person died. Who survived?
    A: No one
    B: The couples
    C: Married people
    """)
    if ans1.upper() == "A":
        print("\nIncorrect, try again")
        first_riddle(ans1)
    elif ans1.upper() == "B" or ans1.upper() == "C":
        print("\nWell done.")
        second_riddle(ans1)
    else:
        print("Try again")
        first_riddle(ans1)

def second_riddle(ans1):
    print("\nOK, let me ask you another riddle!")
    ans1 = input("""If a brother, his sister, and their dog weren’t under an umbrella, why didn’t they get wet?
    A: They had a raincoat
    B: They were at home
    C: It wasn't raining
    """)
    if ans1 == "A":
        print("\nIncorrect, try again")
        second_riddle()
    elif ans1.upper() == "B":
        print("Good try, but it's not the correct answer!")
        
    elif ans1.upper() == "C":
        print("""That's correct! You survived Gorilla Koko. 

        You start to test the rest of the animals, looking over your shpoulder for a frisky ghost-dog..
        
        Just get on with it test the vaccine and save the world!""")
        caged_animals()
    else:
        print("Try again")
        second_riddle(ans1)

def caged_animals():
    
    print("\nTest the vaccine on all animals and see the outcome...")
    ans1 = input("""You tried everything, after an hour you return the animal testing room
    
    Did they live?

    Did they die?

    Take a guess...

    A: Dogzilla has some more ghost friends wanting to hump you
    B: All the animals are high and behaving weirdly
    C: Just like Johnny Five, all of them are alive
    """)
    if ans1.upper == "A":
        print("\nIncorrect, try again")
        caged_animals()
    elif ans1.upper() == "B":
        #print("They are dead and go to the bar to be sad")
        print ("\nUh-oh, it looks like you and Ivan messed up big time, your vaccine failed and all the animals died. This will haunt you forever. Well done genius.")
        input ("\nPress enter to continue...") 
        print ("\nTo drown that guilt that should definietly be weighing on you heavily at this point you murderer, you go to a local bar to drown your sorrows \nNothing fancy though, you dont deserve it. \n A shady but beautiful woman comes and sits next to you")
        beautiful_organ_dealer()
    elif ans1.upper() == "C":
        print("They are all alive. You deserved to have some fun in the bar!")
        bar_big_pharma()
    else:
        print("Try again")
        caged_animals()

        
        




 #------------------------------------------------------------------------------------------------------------------------
   
    #ans1 = input(">>")


#Nazmi

#Hasan
#Conditional branch based on previous outcome of animals dying so 
def vaccine_question():

    print("\nSo I have the vaccine for you, but it will kill half of the people who take it. \nBut what I can guarantee is that you and your family will be safe")

    time.sleep(3)

    print("\nIt looks like you have an ethical dilemma here young animal murderer. Will you refuse the vaccine and risk your family dying \nOr will you roll the dice with the fate of the world?")

    time.sleep(1)

    response = input("\nA: Take the vaccine off this gorgeous Russian organ dealaer and hope for the best or \nB: Get on your moral high horse after killing a bunch of animals and let everyone die too [A/B] ")

    if response.upper() == "A":
        time.sleep (2)
        print("\nWow, I really didn't think you had the balls. Rolling the dice like that? You're a stronger man than me")
        time.sleep(2)
        print("\nYou better get that Russian whatever-it-is to the vaccine plant before sunrise mate")
    elif response.upper() == "B":
        time.sleep(3)
        print("\nReally?.......So everyone dies? Including you?")
        time.sleep(2)
        print("""\nBye-bye

                  88                               88           
                  88                         ,d    88           
                  88                         88    88           
          ,adPPYb,88  ,adPPYba, ,adPPYYba, MM88MMM 88,dPPYba,   
         a8"    `Y88 a8P_____88 ""     `Y8   88    88P'    "8a  
         8b       88 8PP"\"\"\"\"\"\" ,adPPPPP88   88    88       88  
         "8a,   ,d88 "8b,   ,aa 88,    ,88   88,   88       88  
          `"8bbdP"Y8  `"Ybbd8"' `"8bbdP"Y8   "Y888 88       88  

        """)
        vaccine_question()
    else:
        print("\nWere you born stupid or did you choose this life?")
        time.sleep(3)
        vaccine_question()

def beautiful_organ_dealer():
    print("\n*thick russian accent* \"Why the long face handsome?\"")

    time.sleep(3)

    print("\n\"Oh Mcdonald doesn't have a farm anymore...\" you reply")

    input("\nPress enter to continue...")

    print("\nShe looks at you, confused. You notice how beautiful this woman is and start paying attention, \nShe has a question for you")

    input ("\nPress enter to continue...")

    print("\nI know who you are and I know what you've been working on. I have to say it is noble of you. In Russia we don't place such value on human life. \nUnless you pay cash...")
    time.sleep(5)

    print("\n\"What do you mean?\" you reply")
    time.sleep(1)

    print("\n*Russian accent gets thicker* Well put it this way, if one of your tests went wrong and you ruined your kidneys, \nI could fix this problem. \nI can also fix the problem you have now")
    time.sleep(5)

    print("\n*She pulls a vial out of the left pocket of her full length leather coat* \nI have your vaccine right here")

    input("\nPress enter to continue... ")

    print("\nThis vaccine here has a 50/50 chance or curing the world\n& I know what you are thinking..")

    time.sleep(3)

    print("\nBut 50 is hgher than 0 my friend...")

    vaccine_question()
#commented out as it used else where to enable story
#animals = "dead"
# if animals == "dead":
#     print ("Uh-oh, it looks like you and Ivan messed up big time, your vaccine failed and all the animals died. This will haunt you forever. Well done genius.")
#     input ("Press enter to continue...") 
#     print ("To drown that guilt that should definietly be weighing on you heavily at this point you murderer, you go to a local bar to drown your sorrows, nothing fancy though, you dont deserve it. \n A shady but beautiful woman comes and sits next to you")
#     beautiful_organ_dealer()
# elif animals == "alive":
#     print ("Well, well well. you're not just a pretty face after all. It seems liek the vaccine you put together with Ivan in the lab did the trick. If worked on a giraffe it'll probably work on humans too. Right?")
#     input ("Press enter to continue...")
#     print ("To celebrate this win (sort of) you go to a bar to celebrate, the nicest one you can afford. So you go to the cheapest bar you can find and order a drink or nine. A man in a suit comes and sits down next to you")

#Hasan
def factory_organ():
    d=int(0)
    factory()
    print("\nAs you make your way to the vaccine factory you notice there isn't much secuirty tonight. They must be saying goodbye to their loved ones.")
    time.sleep(2)
    print("\nYou forgot your ID, you'll have to sneak in")
    a=sneak()
    if a==1:
        print("\nNot just a pretty face.\nYou're in.")
    elif a== 0 :
        print("\nYou walk up to the entrance and start talking to the guard, the guard recognizes you but can't let you in without your ID, he calls up for clearance")
        time.sleep(1)
        game_q(d)
    else:
        print("\nYou walk up to the entrance and start talking to the guard, the guard recognizes you but can't let you in without your ID, he calls up for clearance")
        game_q(d)
    print("\nAs you enter the main production room you spot the super-old control PC and fancy some nostalgia")
    time.sleep(2)
    computer()
    print("\nYou upload the Russian  vaccine to the computer and start production")
    time.sleep(1)
    print("\nIt has been a few days you uploaded the vaccine. \nYou turn on the news and see there is an experimental vaccine being rolled out")
    time.sleep(1)
    print("It has now been a week since the vaccine has been give to people and the realization that 50% of people are dieing while the others are cured")
    print("Your family walks in saying they had the vaccine and have been given the all clear from it side effects")
    end_game()

#Caleb
def restart():
    a=input("Would you like to restart and make a diffrent choices Yes/Y or  No/N")
    if a[0].upper() == "Y":
        start_game()
    else:
        quit()

def start_game():
 
 time.sleep(3)
 print("""It's the year 2050 and COVID 50 has broken out and the whole world is now a ticking time bomb.

 At the stroke of midnight the virus will be activated for some reason.

 It's 5pm. You forgot to work on the vaccine today becuase you were daydreaming.

 You have one night to save the world.

 Good luck.
""")
 player_name()

 time.sleep(2)
 let_start()

def let_start():
 response = input("Are you up to the task [Y/N] ")
 time.sleep(2)

 if response.upper() == "Y" or response.upper() == "YES":
   print("\nGreat, let's go.")

 elif response.upper() == "N" or response.upper() == "NO":
    print("\nThe fate of the world was in your hands and you have failed. Well done mate...")
    restart()
 else:
    print("\nTime is ticking... please try again.")
    let_start()
start_game()

time.sleep(1)

print("""    ________________________________________________
            //                                               \\ 
           |    _________________________________________     |
           |   |                                         |    |
           |   |  C:\                                    |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |        ******COVID 50 OUTBREAK******    |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |_________________________________________|    |
           |                                                  |
            \_________________________________________________/
                   \___________________________________/
                ___________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_
:-------------------------------------------------------------------------:
`---._.-------------------------------------------------------------._.---'
                              
""")


print("\nIts a cold, lonely night, and you're in your office when the boss barges in...")

time.sleep(1)

print ("""The boss has come in to grill you about having just one night to save the world

What do you do
?""")
time.sleep(1)

def office_function():
    global boss_reply #needs defining in main code.
    first_choice = input("""

    A: Examine the picture of his kids and exclaim how ugly they are.
    B: Call his wife and tell her he's having an affair.
    C: Walk out calmly and get back to work.
    >>""")

    if first_choice[0].upper() == "A":
        print("\nThe boss in his anger slaps you then agrees with you. You go back to work holding your face")
        #Call A path function
        boss_reply="A"
        Lab()
    elif first_choice[0].upper() == "B":
        print("\nYou hear the bosses wife divorce him over the phone and you exit the room with a smirk on your face. Hehe")
        #Call B path function
        boss_reply="B"
        Lab()
    elif first_choice[0].upper() == "C":
        print("\nWork resumes ... time is ticking")
        #Call C path function
        boss_reply="C"
        Lab()
    else:
        #You didn't choose A, B or C, try again
        #Repeat this function
        office_function()

office_function()
#Caleb
