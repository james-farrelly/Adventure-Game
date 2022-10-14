def introduction():
    global weapon       #Reset variables and make them global for later use 
    weapon = False
    global key 
    key = False
    global treasure 
    treasure = False
    global boss 
    boss = False
    global dead 
    dead = False
    print("With a great pain in your head and a significant chunk of your memory missing, you wake up in a place you don't recognise")      #Introduction
    print("You're in a small room lit only by candles and with crumbling walls, suggesting its very old")
    name = input("You struggle to remember your name, but eventually it comes back to you:")        #Store user name for later use
    first_Room()     #Start the first sequence

def first_Room():        #Set up function for first room
    directions = ["LEFT", "FORWARD", "RIGHT"]       #Possible exits
    print("You decide its time to venture out of the room and see three possible exits as you look around you")
    user_Input = ("")
    while(user_Input not in directions):      #User will be stuck in this room until choosing one of the possible exits
        user_Input = input("Options: left/right/forward").upper()        #User chooses direction (using .upper() so that its not case sensitive)
        if(user_Input == ("LEFT")):
            print("You turn to your left and head through a small mossy door")
            damp_Room()         #Other functions are called to move the user from room to room
        elif(user_Input == ("FORWARD")):
            print("You continue forward to the next room through a hole where the door used to be")
            pit_Room()
        elif(user_Input == ("RIGHT")):
            print("Your turn to your right and head through a large heavy door leading to a seemingly very dark room")
            creepy_Room()
        else:
            print("Please enter a valid direction")
    
def damp_Room():
    directions = ["BACK"]
    global key      #Make the variable global so it can be called in the outro
    print("You step through the door to find water dripping from the ceiling and puddles all over the floor")
    print("There are no other exits to the room but there is a table at the other end with something shiny on it")
    user_Input = ("")
    while(user_Input not in directions):
        user_Input = input("Options: forward/back").upper()        
        if(user_Input == ("FORWARD")):
            print("You walk over to the table and find the shiny thing to be a key that you pocket thinking it might be useful later")
            key = True      #Set the variable to "True" for decision making later 
        elif(user_Input == ("BACK")):
            print("Staying here any longer is not worth your time so you head back")
            first_Room()
        else:
            print("Please enter a valid direction")

def pit_Room():
    directions = ["FORWARD", "BACK"]       
    print("""The "room" in front of you isn't much of a room at all, more of a large hole in the ground""")
    print("There is a door on the other side but you'll have to jump over the pit in order to reach it")
    user_Input = ("")
    while(user_Input not in directions):      
        user_Input = input("Options: forward/back").upper()        
        if(user_Input == ("FORWARD")):
            print("You decide to take your chances and leap across the gap, narrowly making it and quickly moving through the door")
            large_Room()
        elif(user_Input == ("BACK")):
            print("You decide its not worth the risk and head back the way you came")
            first_Room()
        else:
            print("Please enter a valid direction")

def creepy_Room():
    directions = ["FORWARD", "BACK"]       
    print("As expected it is almost impossible to see in this room aside from the small amount of light coming in from the first room")
    print("There is an eerie atmosphere in the room, almost as if it's warning you not to step further in to it")
    print("However, you think you are able to make out another large door at the other end of it")
    user_Input = ("")
    while(user_Input not in directions):      
        user_Input = input("Options: forward/back").upper()        
        if(user_Input == ("FORWARD")):
            print("You stumble clumsily to the other end of the room and confirm your suspicions of another door")
            print("Despite your gut feeling and all the warning signs, you stride through it with confidence...")
            creepy_Death()
        elif(user_Input == ("BACK")):
            print("Wisely, you trust your gut and return to the first room, closing the door behind you")
            first_Room()
        else:
            print("Please enter a valid direction")

def creepy_Death():
    global dead
    print("Something grabs your arm the moment you step in to the room, dragging you in and making quick work of you")
    print("Your astute gut was overpowered by your poor survival instincts and you died to a monster in the shadows")
    dead = True
    outro()

def large_Room():
    directions = ["FORWARD", "RIGHT"]
    global weapon      
    print("The doorway opens up in to a very large and beautiful room and you hear the remaining floor in the room behind you collapse")
    print("In front of you is a arena style gate, suggesting there is something waiting to fight you on the other side of it")
    print("However, to your left you see a wall covered in impressive weapons, almost inviting you to take the challenge")
    print("There is also another regular door to your right, offering a much safer looking exit to the room")
    user_Input = ("")
    while(user_Input not in directions):      
        user_Input = input("Options: left/right/forward").upper()        
        if(user_Input == ("LEFT")):
            print("You head over to the wall of weapons and equip yourself with the sharpest sword you can find")
            weapon = True
        elif(user_Input == ("FORWARD")):
            if(weapon):
                print("Now armed, your charge forward through the gate, ready for whatever challenge lies ahead")
                boss_Fight()
            else:
                print("Foolishly you let your confidence overpower your intelligence and charge through the gate without a weapon")
                boss_Fight()
        elif(user_Input == ("RIGHT")):
            print("Your decide the normal looking door is your best choice for now and continue on")
            treasure_Room()
        elif(user_Input == ("BACK")):
            print("With the floor gone, the route back is closed off and you must venture forward")
        else:
            print("Please enter a valid direction")

def boss_Fight():
    directions = ["FIGHT", "FLEE"]
    global boss
    global dead
    print("As expected, the gate leads to an opening resembling an arena")
    print("Immediately you notice a fierce looking creature standing between you and what looks like an exit on the other side")
    print("It hasn't noticed you yet, so it's not too late to flee, but this might be the only exit to this place")
    user_Input = ("")
    while(user_Input not in directions):      
        user_Input = input("Options: fight/flee").upper()        
        if(user_Input == ("FIGHT")):
            if(weapon):
                print("You grab the sword you picked up earlier and launch an attack on the creature")
                print("You hack and slash at eachother until the creature eventually falls")
                print("You step over it and through the door behind it which has a promising light shining behind it")
                boss = True
                outro()
            else:
                print("The creature makes quick work of you and you fall, never knowing what could have been if you picked up the sword...")
                dead = True
                outro()
        elif(user_Input == ("FLEE")):
            print("A quick assessment tells you its not worth the risk so you head back through the gate")
            large_Room()
        else:
            print("Please enter a valid direction")

def treasure_Room():
    directions = ["LEFT", "BACK"]
    global treasure     
    print("You find yourself in a much smaller room with nothing but a chest and a door to the left")
    print("Upon closer inspection you find that the chest is locked")
    if(key):
        print("You try the key in the lock and the chest opens!")
        print("Inside you find a valuable looking gem that you decide to take with you")
        treasure = True
    else:
        print("If only you had a key...")
    user_Input = ("")
    while(user_Input not in directions):      
        user_Input = input("Options: left/back").upper()        
        if(user_Input == ("LEFT")):
            print("Moving past the chest, you venture through the door which has a promising light shining behind it")
            outro()
        elif(user_Input == ("BACK")):
            print("Having decided you've seen all this room has to offer, you return to the much larger one")
            large_Room()
        else:
            print("Please enter a valid direction")

def outro():
    if(dead):       #Different outro depending on if the user died or escaped
        print("You succumbed to the horrors in the dungeon, never to be seen again")
        if(treasure):
            print("At least you found some shiny treasure before you perished.")
        else:
            print("You didn't even have anything to show for it...")

    else:       #Different outro depending on if the user found treasure, a weapon and killed the arena creature
        print("You successfully escaped the dungeon and its horrors. Congratulations! You live to see another day")
        if(treasure):
            print("You also managed to gain something from it, bringing some valuable treasure out with you")
        else:
            print("I wonder if there was anything valuable hidden away down there...")
        if(boss):
            print("You even found a impressive weapon and defeated a fierce foe with it, very impressive")
        else:
            if(weapon):
                print("You even found a impressive weapon!")
            print("You didn't slay any monsters but maybe thats for the best...")

    again = input("Would you like to try again and see what else the dungeon has to offer? yes/no").upper()
    if(again == "YES"):     #Restart the code by taking the user back to the first function
        introduction()      #This also resets all the variables so the first try doesn't affect the second try outro
    else:
        print("Thank you for playing")      #Thank the user for playing and end the code

introduction()