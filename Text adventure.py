from sys import exit
import random 
import time as t
import sys


def eff(a):
    for i in a :
        print(i,end="")
        t.sleep(0.05)
    print()


    

def respawn():
    eff(" ")
    ok = ""
    while(ok!="y" and ok != "n"):
        ok = input("would you like to retry (y/n) ")
        if ok == "y":
            eff(" ")
            a_map=Map("Floor5")
            a_game=Engine(a_map)
            a_game.play()    
        if ok == "n":
            eff(" ")
            eff("this game is too hard for you (fyi ; the n00b is implyed) ")
            eff(" ")
            sys.exit(0)

def erespawn():
    eff(" ")
    ok = ""
    while(ok!="y" and ok != "n"):
        ok = input("would you like to retry (y/n) ")
        if ok == "y":
            eff(" ")
            a_map=Map("Floor5")
            a_game=Engine(a_map)
            a_game.play()    
        if ok == "n":
            eff("")
            eff("well...")
            t.sleep(5)
            eff(" ")
            eff("IG you win then..... ")
            t.sleep(2)
            eff(" ")
            credit()


class trap():
    def enter(self):
        f = random.randint(1,5)
        if f == 5:
            Floor5.enter(self)
        if f == 4:
            Floor4.enter(self)
        if f == 3:
            Floor3.enter(self)
        if f == 2:
            Floor2.enter(self)
        if f == 1:
            Floor1.enter(self)

def death():
    a = random.randint(1,5)
    eff(" ")
    if a == 1:
        eff(" haah.... noob you just died ")
        respawn()
        
    if a == 2:
        eff(" nothing fancy you just died ")
        respawn()
    if a == 3:
        eff(" just stop trying already ")
        respawn()
    if a == 4:
        eff(" you are dead bro ")
        respawn()
    if a == 5:
        eff(" each time you die you owe me 5$ ok ? ")
        eff(" ")
        eff(" fyi , its hard work  ")
        respawn()


class Scene(object):

    def enter(self):
        eff(" this scene is not yet configured ")
        exit(1)

class Engine(object):
    
    def __init__(self, scene_map):
        self.scene_map=scene_map

    def play(self):
        current_scene=self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('Finished')

        while current_scene!=last_scene:
            next_scene_name=current_scene.enter()
            current_scene=self.scene_map.next_scene(next_scene_name)

        current_scene.enter()

class Drop(Scene):
    def enter(self):
        print(Drop.drop_lines[random.randint(0, 2)])

    drop_lines={
        " you were thrown out of your current floor":1,
        "a trapdoor opened below you and you fell into the darkness ":2,
        #add some more
    }


class Floor5(Scene):
    
    def enter(self):
        
        eff (" welcome to floor 5 : looks like a cave ")
        
        def sp5():
            
            eff(" ")
            eff(" you find yourself in a cave with 4 paths to take N,E,W,S ")
            eff(" ")
            dirn = ""
            while (dirn!="n" and dirn!= "e" and dirn != "w" and dirn != "s"):
                dirn = input(" Enter direction you want to move in ")   
                eff(" ")
                
                if dirn == "n":
                    p_a()
                
                if dirn == "e":
                    p_c()
                
                if dirn == "w":
                    eff (" You are stuck in a loop and end up at the same place you started ")
                    eff(" ")
                    sp5()
                
                if dirn == "s":
                    eff (" You are stuck in a loop and end up at the same place you started ")
                    eff(" ")
                    sp5()

                

                
                    


    

        def p_a():
            eff(" You arrive at a dead end you have two paths E,S ")
            eff(" ")
            
            eff(" ")
            dirn = ""
            while (dirn!= "e" and dirn != "s"):
                dirn = input("Enter direction you want to move in ")
                eff(" ")
                
                if dirn == "e":
                    p_b()
                
                if  dirn== "s":
                    sp5() 
                
                
                    
        def p_b():
            eff(" You meet a talking bunny ")
            eff(" ")
            eff(" Bunny-'you are in the dungeon of  if you want to escape you have to defete the boss of each floor  ' ")
            eff(" ")
            eff(" Bunny-'but i suggest you dont go up not only because the bosses are very hard to beat but also.....' ")
            eff(" ")
            eff(" Bunny-'you'll see when you go up' ")
            eff(" ")
            eff(" Bunny-'if you want to go up here is the key' ")
            eff(" ")
            eff(" Bunny gives you a key")
            eff(" ")
            
            eff(" Direction you can move in are South , West ")
            eff(" ")
            
            eff(" ")
            dirn=""
            
            while (dirn != "w" and dirn != "s"):
                eff(" ")
                dirn = input(" Enter direction you want to move in ")

                if dirn == "s":
                
                    p_c_u()
                
                if dirn == "w":
                    p_a()

               
                    
    
        
        def p_c():


            eff(" You arrive at a door ")
            eff(" ")
            eff(" It seems to be locked ")
            eff(" ")
            eff(" Search for the key ")
            eff(" ")
            eff(" As you start to move away from the door...")
            eff(" ")
            eff(" You hear a loud noise")
            eff(" ")
            death()


        def p_c_u():

            eff(" ")
            eff(" You use the key given by the bunny to unlock the door ")
            eff(" ")
            eff(" You you have 3 paths available to you chose one you cannot turn back ")


            eff(" ")
            path = ""
             
            while (path != "1" and path != "2" and path != "3" ):

                path = input(" Enter the path you want to use (1/2/3) ")
                eff(" ")
                if path == "1":


                    eff(" A strong monster appears  ")
                    eff(" ")
                    eff(" Kills you instantly ")
                    eff(" ")
                    death()
                if path == "2":


                    eff(" There is a empty dark path ")
                    eff(" ")
                    eff(" At the end of the path you find a gigantic door ")
                    eff(" ")
                    p_g()
                
                if path == "3":
                    eff(" There is a monster ")
                    eff(" ")
                    eff(" What do you chose to do ")
                    eff("1]Run ")
                    eff("2]Attack ")
                    eff(" ")
                    c= 0
                    
                    while ( c != "1" and c != "2" ):

                        c= input(" Enter your choice ")
                        eff(" ")
                        
                        if c == "1":
                            eff(" The monster kills you while you run ")
                            eff(" ")
                            death()
                        
                        if c == "2" :
                            eff(" After a long fight you manage to defeat the monster ")
                            eff(" ")
                            eff(" As you walk down the path you find a gigantic door ")
                            eff(" ")
                            p_g()
                        
                        
            

        def p_g():
            eff(" ")
            eff(" You touch the door ")
            eff(" ")
            eff(" The door opens only to reveal a huge trool  ")
            eff(" ")
            p_h()
            
            

        def p_h():
            eff(" ")
            eff(" The boss sees you ")
            eff(" ")
            eff(" He is amazed to see you ") 
            eff(" ")
            eff(" Troll - 'oh you look like a smart one' ")
            eff(" ")
            eff(" Troll - 'ill let you go if you manage to tell me ans of this question -'")
            eff(" ")
            eff(" What month of the year has 28 days ?  ")
            eff(" ")
            ans = input(" Enter your answer ")
            eff(" ")
            if ans == "All":
                eff(" ")
                eff("You have completed the floor")
                eff(" ")
                Floor4().enter()
                
                
                
            

        
        sp5( )
       
        
        
        
        

class Floor4(Scene):
    
    def enter(self):
        
        eff(" Welcome to floor 4 : lava lol ")
        
        def sp4():
            eff(" ")
            eff("you find yourself in a cave with 4 paths to take N,E,W,S")
            eff(" ")
            dirn =""
            while (dirn!="n" and dirn!="e" and dirn!="w" and dirn!="s"):
                eff(" ")
               
                dirn = input("enter direction you want to move in ")   
               
                if dirn == "e":
                    eff(" ")
                    eff("a you arraive at a door ")
                    eff(" ")
                    eff("it looks breakable")
                    eff(" ")
                    eff("what do you do?")
                    eff(" 1]break the door ")
                    eff(" 2]go back to West ")
                    eff(" ")
                    op=0
                    while(op!= "1" and op!= "2" ):
                        op = input("enter your choice- ")
                        if op == "1":
                            eff(" ")
                            eff("O0ps its LAVA!!!")
                            death()
                        
                        if op ==  "2":
                            eff(" ")
                            sp4()

                        
                
                if dirn == "n":
                    p_a()           
                
                if dirn == "w":
                    eff ("you walk towards west but somehow end up at the same location you were at before")
                    eff(" ")
                    sp4()
                
                if dirn == "s":
                    eff(" ")
                    p_l()
                
                

        def p_a():
            eff(" ")
            eff("you arrive at a dead end there are two paths to take South and East ")
            dirn =""
            
            while(dirn !="e" and dirn != "s" ):
                eff(" ")
                dirn = input("enter the direction you want to move in - ")
                
                if dirn == "s":
                    sp4()
                
                if dirn == "e":
                    p_b1()

                
        
        def p_b1():
            eff(" ")
            eff("while walking on a path to the east you encouter a chest ")
            eff(" ")
            eff("what do you do- ")
            eff(" 1] Open the chest")
            eff(" 2] continue on your path")
            o = 0
            while(o != "1" and o != "2"):
                o = input("Enter your choice- ")
                
                if o == "1" :
                    eff("hah... you fell in to my trap ")
                    eff(" ")
                    Floor5.enter(self)
                
                if o == "2" :
                    p_c1()
                
                

        def p_c1():
            eff(" ")
            eff("You arrive at a dead end ")
            eff(" ")
            eff("the paths available are  South and West ")
            dirn= ""
            while(dirn!="s" and dirn!="w"):
                eff(" ")
                dirn = input("Enter the direction you want to move in ")

                if dirn == "w":
                    eff(" ")
                    eff("while walking on a path to the east you encouter a chest ")
                    eff(" ")
                    eff("what do you do- ")
                    eff(" 1] Open the chest")
                    eff(" 2] continue on your path")
                    o  = 0
                    while(o != "1" and o != "2"):
                        o = int(input("Enter your choice- "))
                        
                        if o == "1" :
                            eff("hah... you fell in to my trap ")
                            eff(" ")
                            Floor5.enter(self)
                        
                        if o == "2" :
                            p_a()
                        
                        
                
                if dirn == "s":  # point D on map
                    eff(" ")
                    eff("while walking on the path towards the south you encounter a path towards west ")
                    eff(" ")
                    eff("What do you do ?")
                    eff(" 1] Go west") # goes toward point E
                    eff(" 2] Continue on your path ")
                    o  = 0
                    while(o != "1" and o != "2"):
                        o = input("Enter your choice- ")
                        
                        if o == "1" :
                            eff("O0ps is LAVA lol !! ")
                            eff(" ")
                            death()
                        
                        if o == "2" :
                            p_m()
                        
                        
        def p_m():
            eff(" ")
            eff("you arrive at a dead end ")
            eff(" ")
            eff("you have to paths to take North , West ")
            dirn = ""
            while (dirn!="n" and dirn !="w"):
                dirn=input("Enter the direction you want to move in ")
                
                if dirn == "n":
                    eff(" ")
                    eff("while walking on the path towards the south you encounter a path towards west ")
                    eff(" ")
                    eff("What do you do ?")
                    eff(" 1] Go west") # goes toward point E
                    eff(" 2] Continue on your path ")
                    o  = 0
                    while(o != 1 and o != 2):
                        o = int(input("Enter your choice- "))
                        if o == 1 :
                            eff("O0ps is LAVA lol !! ")
                            eff(" ")
                            death()
                        
                        if o == 2 :
                            p_c1()
                        
                        
                
                if dirn == "w":
                    p_g()

                

        def p_g():
            eff(" ")
            eff("you see a dark path ahead of you... ")
            eff(" ")
            eff("you continue to walk on this dark path... ")
            eff(" ")
            eff("you see a giant red door ")
            p_j()
        
        def p_f():
            eff(" ")
            eff("you see a dark path ahead of you... ")
            eff(" ")
            eff("you continue to walk on this dark path... ")
            eff(" ")
            eff("you see a giant red door ")
            p_j()
        
        def p_l():
            eff(" ")
            eff("you run into a dead end ")
            eff(" ")
            eff("the paths available to you are East and North ")
            dirn = ""
            while(dirn != "n" and dirn != "e"):
                dirn = input("enter direction you want to move in ")
                
                if dirn == "n":
                    sp4()
                
                if dirn == "e":
                    p_f()
                
               


        
        
        def p_j():
            eff(" ")
            eff("you touch this and it starts to open... ")
            eff(" ")
            eff("as the door opens you see mountains of corpses in front of you...")
            eff(" ")
            eff("A dragon even bigger than the mountain of corpses is seen ")
            eff(" ")
            p_k()
            
        
        def p_k():
            eff("the dragon sees you ")
            eff(" ")
            eff("dragon - 'hey human do you know who i am....'")
            eff(" ")
            eff("dragon - 'how did you enter my lair ? '")
            eff(" ")
            eff("dragon - 'any way i am l'drago the ruler of this floor  ' ")
            eff(" ")
            eff("l'drago - 'I dont like violence so ill give you a riddle '")
            eff(" ")
            eff("l'drago - 'if you ans me correctly ill let you pass if you can't ill kill you'")
            eff(" ")
            eff("l'drago - 'i am very hypocryitical you see '")
            eff(" ")
            eff("l'drago - 'now listen to the riddle carefully i shall not repeat'")
            eff(" ")
            eff("l'drago - 'What is greater than god,'")
            eff("          'more evil than the devil,'")
            eff("          'the poor have it, '")
            eff("          'the rich need it, '")
            eff("          'and if you eat it,'")
            eff("          'you'll die'")
            eff(" ")
            eff("l'drago - 'now answer me human'")
            eff(" ")
            ans = input('Enter you answer here ')
            if ans == "nothing":
                eff("l'drago - 'very good my friend you may pass'")
                eff(" ")
                eff("you have cleared the floor")
                Floor3().enter()
                return "clear"
            else:
                eff("l'drafo - 'i am sorry my friend , but we made a deal'")
                eff(" ")
                eff("l'drago kills you ")
                eff(" ")
                death()

            
        sp4()
        


class Floor3(Scene):
    
    def enter(self):
        
        
        eff("welcome to floor 3 : is it a jungle? ")
        global fish 
        fish = 0
        
        def sp3():
            
            eff(" ")
            eff("you find yourself in a cave with 4 paths to take North,East,West,South")
            eff(" ")
            dirn =""
            while (dirn!="n" and dirn!="e" and dirn!="w" and dirn!="s"):
                eff(" ")
               
                dirn = input("enter direction you want to move in ")   
               
                if dirn == "e":
                    t.sleep(2)
                    p_e()

                if dirn == "n":
                    t.sleep(0.2)
                    p_b()           
                
                if dirn == "w":
                    t.sleep(0.2)
                    p_a()
                
                if dirn == "s":
                    t.sleep(0.2)
                    p_c()

               
        
        def p_a(): 
            global fish
            fish = 0
           
            
            eff("you see a huge lake ")
            eff("you can  do the following activities- ")
            eff("   1]take a swim")
            eff("   2]catch fish")
            eff(" ")
            ch = ""
            while (ch != "1" and ch != "2"):
                ch = input("what do you do (1/2)- ")
                if ch == "1":
                    eff("you enjoy yourself in the lake ")
                    eff("you feel refreshed")
                    t.sleep(0.2)
                    eff("as there is no place to go you go back towards East")
                    sp3()
                if ch == "2":
                    eff("you catch a fish in the lake ")
                    eff("what do you do- ")
                    eff("   1]eat the fish ")
                    eff("   2]keep the fish for another time")
                    cf = ""
                    while(cf != "1" and cf!= "2" ):
                        
                        cf = input("enter your choice (1/2)- ")
                        
                        if cf == "1" :
                            eff("you eat the fish")
                            fish -= 1
                            eff("your are not hungry anymore")
                            eff("tho were you hungry in the first place ?")
                            t.sleep(0.2)
                            eff("as there is no place to go you go back towards East")
                            sp3()
                        
                        if cf == "2":
                            eff("you decide to not eat the fish ")
                            eff("and save it for another day as you ar not hungry right now ")
                            fish += 1
                            t.sleep(0.2)
                            eff("as there is no place to go you go back towards East")
                            sp3()  

                       
                        
        
        def p_b():

            eff("you arrive at a dead end ony two paths are available East,South")
            dirn = ""
            while (dirn != "e" , dirn != "s"):
                dirn = input("enter direction you want to move in ")
                if dirn == "e":
                    eff(" ")
                    eff("you see a door in front of you ")
                    eff(" what do you do? ")
                    eff("   1]open the door")
                    eff("   2]continue to the path towards South of the door")
                    
                    cd = ""
                    while(cd != "1" and cd != "2"):
                        eff(" ")
                        cd = input("enter your choice here (1/2)- ")
                        
                        if cd == "1":
                            eff("hah...its a trap trap trap trap ")
                            Floor4.enter(self)
                        
                        if cd == "2":
                            p_e()
                        
                        
                
                if dirn == "s":
                    sp3()
                
                

        def p_e():
            
            eff("there is a monster ")
            eff(" ")
            eff("what do you chose to do")
            eff("1]run")
            eff("2]attack")
            eff(" ")
            c= ""
                    
            while ( c != "1" and c != "2" ):

                c= input("enter your choice ")
                eff(" ")
                if c == "1":
                    eff("the monster kills you while you run ")
                    eff(" ")
                    death()
                    
                if c == "2" :
                    eff("after a long fight you manage to defeat the monster")
                    eff(" ")
                    p_f()

                else:
                    eff("")
                    eff("enter valid option")
                    eff("")
        
        def p_f():
            
            eff("there is a monster ")
            eff(" ")
            eff("it looks strong...")
            
            eff(" ")
            eff("what do you chose to do")
            eff("1]run")
            eff("2]attack")
            eff(" ")
            c= ""
                    
            while ( c !="1" and c != "2" ):
                eff(" ")
                c = input("enter your choice ")
                
                if c == "1":
                    eff("the monster kills you while you run ")
                    eff(" ")
                    death()
                    
                if c == "2":
                    eff("after a long fight you manage to stun the monster")
                    eff(" ")
                    eff("what do you do next?")
                    eff("   1]run")
                    eff("   2]attack again")
                    fi = ""
                    while(fi != "1" and fi != "2"):
                        fi = input("enter your choice ")
                        eff(" ")
                        if fi == "1":
                            eff("you manage to escape the monster ")
                            eff(" ")
                            p_g()

                        if fi == "2":
                            eff("the monster moves....")
                            eff(".......")
                            t.sleep(4)
                            death()
                       
               

        def  p_c():
            global k 
            k = 0
            a = random.randint(1,40)
            eff("you see a misty forest ")
            ok = ""
            while(ok != "y" and ok !="n"):
                ok = input("do you wish to continue ? (y/n)- ")

                if ok == "n":
                    eff("as you are too afraid to move forward ")
                    eff(" ")
                    eff("you return to the starting point... ")
                    eff(" ")
                    sp3()
                
                if ok == "y":
                    
                    if a%2 == 0:
                        p_j()

                    else:
                        eff("you get lost in this dense forest...")
                        eff(" ")
                        t.sleep(2)
                        eff("you wander in this forest....")
                        eff(" ")
                        t.sleep(2)
                        eff("you die of starvation ")
                        eff(" ")
                        t.sleep(2)
                        p_j()
                
              
        def p_g():
            eff(" ")
            
            eff("while walking on a path to the east you encouter a chest ")
            eff(" ")
            eff("what do you do- ")
            eff(" 1] Open the chest")
            eff(" 2] continue on your path")
            o = ""
            
            while(o != "1" and o != "2"):
                o = input("Enter your choice- ")
                
                if o == "1" :
                    eff("hah... you fell in to my trap ")
                    eff(" ")
                    Floor4.enter(self)
                
                if o == "2" :
                    p_i()

               

        def p_i():
            eff(" ")
            
            eff("you see a door in front...")
            eff(" ")
            t.sleep(2)
            eff("you touch it... ")
            eff(" ")
            t.sleep(2)
            eff("it opens...")
            eff(" ")
            t.sleep(2)
            eff("you see a bear...")
            eff(" ")
            t.sleep(2)
            eff("it sees you")
            eff(" ")
            t.sleep(5)
            p_k()
            
        
        def p_k():
            eff("bear - 'hi there do you have any fish ? '")
            eff("")

            if fish == 0:
                eff("bear - 'human you are of no use to me '")
                t.sleep(5)
                eff(" ")
                eff("bear - 'just die' ")
                eff(" ")
                eff("the bear kills you ")
                death()
            
            if fish == 1:
                eff("bear - 'aah...thank you'")
                eff(" ")
                eff("bear - 'you want to go up'")
                eff(" ")
                eff("bear - 'i suggest you dont, but if you wanna go sure why not '")
                eff(" ")
                Floor2().enter()
                return "clear"
            
            
            if fish == -1:

                eff("bear - 'human you ate MY FISH !!!'")
                eff(" ")
                t.sleep(2)
                eff("bear - 'MY FISH !!!!'")
                eff(" ")
                t.sleep(2)
                eff("the bear is angry ")
                eff(" ")
                t.sleep(5)
                eff("the bear kills you ")
                eff(" ")
                death()

            else:
                eff("bear - 'human you are of no use to me '")
                t.sleep(5)
                eff(" ")
                eff("bear - 'just die' ")
                eff(" ")
                eff("the bear kills you ")
                death()

            

        def p_j():
            eff(" ")
            eff("the jungle ends... ")
            t.sleep(2)       
            eff("you begin to see a path towards north ...")
            t.sleep(2)
            eff("you folow the path ...")
            t.sleep(2)
            p_i()




         



                         

                       


                    

        
        
        
        sp3()
       
class Floor2(Scene):
    
    def enter(self):
        
        eff("welcome to floor 2 : potholes? ")

        def sp2():
            eff(" ")
            eff("you find yourself in a cave with 4 paths to take North,East,South")
            eff(" ")
            dirn =""
            while (dirn!="n" and dirn!="e" and dirn!="w" and dirn!="s"):
                eff(" ")
               
                dirn = input("enter direction you want to move in ")   
               
                if dirn == "e":
                    eff(" ")
                    eff("there is a hole in the ground")
                    eff(" ")
                    t.sleep(2)
                    pothole()
                if dirn == "n":
                    t.sleep(0.2)
                    p_a()           
                
                if dirn == "s":
                    t.sleep(0.2)
                    p_y()

                
        
        def pothole():

            z = random.randint(1,3)
            if z == 3:
                Floor3.enter(self)
            
            if z == 2:
                Floor4.enter(self)

            if z == 1:
                Floor5.enter(self)

        def p_a():
            eff(" ")
            eff("you arrive at a dead end")
            eff("")
            eff("the direction available are South , East ")
            eff(" ")
            dirn =""
            while(dirn!="s" and dirn != "e"):
                dirn = input("enter direction you want to move in")
                if dirn == "e":
                    p_b()
                
                if dirn == "s":
                    sp2()
                
               
        
        def p_b():
            eff("")
            eff(" ")
            eff("you arrive at a dead end")
            eff("")
            eff("the direction available are West , South ")
            eff(" ")
            dirn =""
            while(dirn!="s" and dirn != "w"):
                dirn = input("enter direction you want to move in")
                if dirn == "w":
                    p_a()
                
                if dirn == "s":
                    p_h()
                
                
        
        def p_h():
            eff(" ")
            eff("you find yourself at a intersection ")
            eff(" ")
            eff("the directions available are North,East,West,South ")
            eff(" ")
            dirn =""
            while (dirn!="n" and dirn!="e" and dirn!="w" and dirn!="s"):
                eff(" ")
               
                dirn = input("enter direction you want to move in ")   
               
                if dirn == "e":
                    eff(" ")
                    eff("there is a hole in the ground")
                    eff(" ")
                    t.sleep(2)
                    pothole()

                if dirn == "n":
                    t.sleep(0.2)
                    p_b()           
                
                if dirn == "s":
                    t.sleep(0.2)
                    p_i()

                if dirn == "w":
                    eff(" ")
                    eff("there is a hole in the ground")
                    eff(" ")
                    t.sleep(2)
                    pothole()

                

        def p_i():

            eff(" ")
            eff("you find yourself at a intersection ")
            eff(" ")
            eff("the directions available are North,East,West,South ")
            eff(" ")
            dirn =""
            while (dirn!="n" and dirn!="e" and dirn!="w" and dirn!="s"):
                eff(" ")
               
                dirn = input("enter direction you want to move in ")   
               
                if dirn == "e":
                    eff(" ")
                    eff("there is a hole in the ground")
                    eff(" ")
                    t.sleep(2)
                    pothole()

                if dirn == "n":
                    t.sleep(0.2)
                    p_h()           
                
                if dirn == "s":
                    t.sleep(0.2)
                    p_z()

                if dirn == "w":
                    eff(" ")
                    eff("there is a hole in the ground")
                    eff(" ")
                    t.sleep(2)
                    pothole()

               

        def p_y():
            eff(" ")
            eff("you arrive at a dead end")
            eff("")
            eff("the direction available are North, East ")
            eff(" ")
            dirn =""
            while(dirn!="n" and dirn != "e"):
                dirn = input("enter direction you want to move in")
                if dirn == "e":
                    eff(" ")
                    eff("there is a hole in the ground")
                    eff(" ")
                    t.sleep(2)
                    pothole()
                
                if dirn == "n":
                    sp2()
                
               
        def p_z():
            eff(" ")
            eff("you arrive at a deadend ")
            eff(" ")
            eff(" the directions available are West , East ")
            eff("")
            dirn = ""
            while(dirn != "e" and dirn != "w"):

                dirn = input("enter direction you want to move in- ")

                if dirn == "e":
                    p_f()
                
                if dirn == "w":
                   p_c()
                
               
        def p_f():
            eff(" ")
            eff("you arrive at a dead end")
            eff("")
            eff("the direction available are North, West ")
            eff(" ")
            dirn =""
            while(dirn!="n" and dirn != "w"):
                dirn = input("enter direction you want to move in")
                if dirn == "w":
                    p_z()
                
                if dirn == "n":
                    eff(" ")
                    eff("there is a hole in the ground")
                    eff(" ")
                    t.sleep(2)
                    pothole()
                
                
        
        def p_c():
            eff(" ")
            eff("you see a tiny gate ")
            eff(" ");t.sleep(2)
            eff("you open it and squeeze your way threw it")
            eff(" ");t.sleep(2)
            eff("when you enter the room..")
            eff(" ");t.sleep(2)
            eff("you see a giant mouse.... ")
            eff(" ");t.sleep(5)
            eff("............")
            p_d()
            

        def p_d():
            eff("")
            eff("rat - 'hello here puny human' ")
            eff(" ");t.sleep(2)
            eff("rat - 'have you seen any cheese around here ? '")
            eff(" ");t.sleep(1)
            eff("you notice there are paths leading to North,East,West,South")
            eff(" ");t.sleep(1)
            dirnr = ""
            while(dirnr != "n" and dirnr != "e" and dirnr != "w" and dirnr != "s"):
                dirnr = input("enter the direction you tell the rat to go in ")
                if dirnr == "s":
                    eff("")
                    eff("the rat goes south and falls down  a pothole")
                    eff("");t.sleep(3)
                    eff("the rat dies ")
                    Floor1().enter()
                    return "cl"
                
                if dirnr == "n":
                    eff("")
                    eff("the rat goes North... ")
                    eff("");t.sleep(2)
                    eff("unable to find any cheese the rat comes back...")
                    eff("");t.sleep(2)
                    eff("rat  - 'you liar ' ")
                    eff("....................")
                    eff("");t.sleep(2)
                    eff("the rat is annoyed")
                    eff("");t.sleep(2)
                    eff("the rat kills you")
                    eff("");t.sleep(2)
                    death()

                if dirnr == "e":
                    eff("")
                    eff("the rat goes East... ")
                    eff("");t.sleep(2)
                    eff("unable to find any cheese the rat comes back...")
                    eff("");t.sleep(2)
                    eff("rat  - 'you liar ' ")
                    eff("....................")
                    eff("");t.sleep(2)
                    eff("the rat is annoyed")
                    eff("");t.sleep(2)
                    eff("the rat kills you")
                    eff("");t.sleep(2)
                    death()

                if dirnr == "w":
                    eff("")
                    eff("the rat goes West... ")
                    eff("");t.sleep(2)
                    eff("unable to find any cheese the rat comes back...")
                    eff("");t.sleep(2)
                    eff("rat  - 'you liar ' ")
                    eff("....................")
                    eff("");t.sleep(2)
                    eff("the rat is annoyed")
                    eff("");t.sleep(2)
                    eff("the rat kills you")
                    eff("");t.sleep(2)
                    death()
                
                



            

           


        


        sp2()
       
        
class Floor1(Scene):
    def enter(self):

        eff("welcome to floor 1 : moredoor")

        def pothole():

            z = random.randint(1,4)
            if  z == 4:
                Floor2.enter(self)
            
            if z == 3:
                Floor3.enter(self)
            
            if z == 2:
                Floor4.enter(self)

            if z == 1:
                Floor5.enter(self)

        def sp1():
            eff(" ")
            eff("you find yourself in a cave with 4 paths to take North,East,South")
            eff(" ")
            dirn =""
            while (dirn!="n" and dirn!="e" and dirn!="w" and dirn!="s"):
                eff(" ")
               
                dirn = input("enter direction you want to move in ")   
                
                if  dirn == "w":
                    eff(" ")
                    p_b()
               
                if dirn == "e":
                    eff(" ")
                    p_e()
                
                if dirn == "n":
                    eff(" ") 
                    p_a()           
                
                if dirn == "s":
                    eff(" ")
                    p_y()

        def p_a():
            eff("")
            eff("you reach a deadend...")
            eff(" ")
            eff("you find a chest")
            eff(" ")
            eff("what do you do? ")
            eff("   1]open the chest")
            eff("   2]return to starting point")
            eff("")
            o = ""
            while(o != "1" and o != "2"):
                o = input("enter your choice(1/2)- ")

                if o == "1":
                    eff("oops... your not supposed to do that")
                    eff("")
                    Floor2.enter(self)
                
                if o == "2":
                    eff("you return to the starting point ")
                    sp1()

        def p_b():

            eff("you arrive at the dead end ")
            eff(" ")
            eff("you see a door....")
            eff(" ")
            eff("what do you do?")
            eff("  1]open the door")
            eff("  2]go back to start point")
            eff("")
            d = ""
            while( d != "1" and d != "2"):
                d = input("enter your choice here(1/2)- ")

                if d == "1":
                    eff(" ")
                    p_c()

                if d == "2":
                    eff(" ")
                    sp1()

        def p_c():
            eff("you arrive at a dead end...")
            eff(" ")
            eff("the directions available are North , East")
            eff(" ")
            dirn =""
            while(dirn!="n" and dirn!="e"):
                dirn = input("enter direction you want to move in- ")

                if dirn =="n":
                    eff("you go back to the starting point threw the door you came threw....  ")
                    eff(" ")
                    eff("and close the door on your way back ")
                    eff("")
                    sp1()

                if dirn =="e":
                    eff("there is a hole in the floor ")
                    eff(" ")
                    pothole()
        
        def p_e():

            eff("you arrive at the dead end ")
            eff(" ")
            eff("you see a door....")
            eff(" ")
            eff("what do you do?")
            eff("  1]open the door")
            eff("  2]go back to start point")
            eff("")
            d = ""
            while( d != "1" and d != "2"):
                d = input("enter your choice here(1/2)- ")

                if d == "1":
                    eff(" ")
                    p_f()

                if d == "2":
                    eff(" ")
                    sp1()

        def p_f():
            eff("you arrive at a dead end...")
            eff(" ")
            eff("the directions available are North , West")
            eff(" ")
            dirn =""
            while(dirn!="n" and dirn!="w"):
                dirn = input("enter direction you want to move in- ")

                if dirn =="n":
                    eff("you go back to the starting point threw the door you came threw....  ")
                    eff(" ")
                    eff("and close the door on your way back... ")
                    eff("")
                    sp1()

                if dirn =="w":
                    eff("there is a hole in the floor ")
                    eff(" ")
                    pothole()

        def p_y():
            eff("")
            eff("after a long walk you arrive at a dead end ")
            eff("")
            eff("the directions available are East and West ")
            eff(" ")
            dirn = ""
            while(dirn != "e" and dirn != "w"):
                dirn = input("enter the directions you want to move in-  ")

                if dirn == "e":
                    
                    eff("")
                    eff("you encouter a weird elevator...")
                    eff(" ")
                    eff("you ride the elevator")
                    Finished().enter()

                if dirn == "w":
                    eff("you see a door....")
                    eff(" ")
                    eff("what do you do?")
                    eff("  1]open the door")
                    eff("  2]go back ")
                    eff("")
                    d = ""
                    while( d != "1" and d != "2"):
                        d = input("enter your choice here(1/2)- ")

                        if d == "1":
                            eff(" ")
                            eff("its a trap lol!!")
                            death()

                        if d == "2":
                            eff(" ")
                            p_y()
        
        


class Finished(Scene):

    def enter(self):
        eff("")
        eff("you reach the top floor and see the exit to the cave ")
        eff("")
        eff("you run towards it....")
        eff("")
        eff("as you run towards the exit you encounter the bunny you met before ")
        eff("")
        eff("bunny - 'hell there old friend'")
        eff("")
        eff("bunny - 'you see impatient to go some where ?'")
        eff("")
        eff("bunny - 'there is nothing outside'")
        eff("")
        eff(".......")
        eff("")
        eff("bunny - 'ooh!!-you think i am lying.....then go and see for yourself '")
        eff("")
        eff("you go out of the cave and see people with bunny like heads (basically bunny zombies!!) ")
        eff("")
        eff("bunny - ' ooh ; You won! Good job, i guess ?? '")
        eff("")
        eff("bunny - 'you see there was no 'escape' all along '")
        eff("")
        eff("bunny - 'its just that i could no do any thing to you inside that cave'")
        eff("")
        eff("bunny - 'and now that you are outside'")
        eff("")
        eff("the bunny kills you")
        eff("")
        erespawn()
        

        return 'Finished'


def credit():
    eff("this game is made by- ")
    eff("")
    eff("Deven Waykar")
    erespawn()

def htp():
    eff("HOw t0 PLay? -")
    eff("")
    eff("In the game text is used to navigate threw the map- ")
    eff("There are 4 main direction(may change acc to the point on map)- ")
    eff("")
    eff("   1]'n'-is to go North ")
    eff("   2]'e'-is to go East ")
    eff("   3]'w'-is to go West ")
    eff("   4]'s'-is to go South ")
    eff("   #the user is requested to enter the direction he wants to proceed in when asked")
    eff("")
    eff("   #when asked for choice enter the number preceding the your choice ")
    eff("")
    eff("#important notes-")
    eff("   1]Enter small case letter everywhere(the game is case sensitive lol) ")
    eff("   2]If the same question is asked again that means the entered option is not available (please enter valid option)")
    eff("   3]No spaces are to be entered any where ")
    eff("")



def wel():
    eff("")
    eff("Welcome to TExt ADv3nture ") #decide name
    eff("")

def strsc():
    eff("")
    eff("You walk into a cave hoping to find something to sell")
    eff("")
    eff("You walk down a dark path... ")
    eff("")
    eff("You are scared but continue on the path....")
    eff("")
    eff("You fall down a hole ")
    eff("")
    eff("As you fall down you you see a sinister bunny....")
    eff("")
    eff("")
    eff("..................................................")
    eff("")
    eff("...............................")
    eff("")
    eff("...................")
    eff("")
    eff("..........")
    eff("")
    eff("You wake up in a cave")
    eff("")
    eff("You cant seem to remember any thing after the fall....")
    eff("")
    eff("All you remember is entering a cave and falling down ")
    eff("")
    







wel()
htp()
strsc()

class Map(object):

    scenes={
        
        "Floor1":Floor1(),
        "Floor2":Floor2(),
        "Floor3":Floor3(),
        "Floor4":Floor4(),
        "Floor5":Floor5(),
        
       
        "Drop":Drop(),
        "Finished":Finished()
    }

    def __init__(self, start_scene):
        self.start_scene=start_scene

    def next_scene(self, scene_name):
        name = Map.scenes.get(scene_name)
        return name

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map=Map("Floor3")
a_game=Engine(a_map)
a_game.play()


