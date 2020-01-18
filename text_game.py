import random
from sys import exit
prompt = "~> "
valid_move = "\t\tPlease enter a valid move\n~> "

# Starting Script
#eat meet be healed
# random directions until you can see
# Spot where you heal eyes with a 80% chance of death. If this heals you and not the cannibals then you may go through a special quest
# Daves Cliff
def daves_cliff():
    print("""
        You came upon Dave's Cliff and got too close 
        falling into the cold water
        The impact was so bad that you lost your vision
        """)
    dir = input(prompt)
    while True:
        if dir == "south":
                    swail_cave()
        else:
            dir = input(valid_move)

# Swail Cave Entrance
def swail_cave():

    print("""
        You make it to The Swail Cave Entrance and feel warmth coming from the east
        To the south you hear whispering
        The west provides no notable sound or feeling
        """)
    dir = input(prompt)
    while True:

        if dir == "east":
            print("""
        As you walk towards the heat it becomes significantly hotter
        So hot that without being able to see, you must turn back,
        """)

            dir = input(prompt)

            if dir == 'west': #blind == True or                 
                swail_cave()
        elif dir == "north":
            print("""
        You returned back to the water you fell into
        """)
            daves_cliff()
        elif dir == "south":
            cannibal()
        elif dir == "west":
            print("""
        You stepped into some weird liquid on the ground
        The liquid has a 40% of healing your eyes and a 60% chance of killing you
        While blind you are unable to see what's ahead and must turn back
        type yes to use liquid or else head back
        """)
            dir = input(prompt)
            if dir == "yes":
                if random.randint(1, 101) >= 60:
                    print("""
        The liquid works!
        You can now see two paths ahead to the north and west
        """)
                    deeper_cave()
                else:
                    print("""
        Oh no! The liquid starts to burn in your eyes
        You die a slow and miserable death
                            
        Play again? yes/no
        """)
                    new_life()
            elif dir == "east":
                swail_cave()
        else:
            dir = input(valid_move)


# Deeper Cave
def deeper_cave():

    dir = input(prompt)
    while True:
        if dir == "north":
            print("""
            You found a ladder leading up
            Type climb if you want to go up
            Cave continues to the east and west
            """)

            dir = input(prompt)
            
            if dir == "climb":
                print("""
            After climbing up, the door slams shut behind you
            You are in a well lit room......
            """)
                #maybe say something about not getting back down
                woods()
            # elif dir east/west/south
        elif dir == "west":
            print("""
            You got lost in the cave
            after 4 days, nature won
            and you died
            """)
            new_life()
        elif dir == "south":
            print("""
            You walked into a wall
            and cracked your head open
            and you died
            """)
            new_life()
        elif dir == "east":
            print("""
            You are at the ____ cave
            """)
            swail_cave()
        else:
            dir = input(valid_move)

# Cannibal Tribe
def cannibal():
    print("""
    You came upon a tribe of cannibals
    In order to help you they require a gift
    When you think you have what they want
    Try typing 'give' and then the items name
    They offer you a healing remedy to fix your eyes
    In return you must eat human flesh and 
    """)
    dir = input(prompt)

    while True:
        if dir == "south":
            print("""
            You squeeze through a crack in the cave
            to the north you see a sliver of light
            to the west more darkness
            """)
            new_life()
        elif dir == "north":
            print("""
            The tribe saw you leaving and killed you
            and you died Develop more
            """)
            new_life()
        elif dir == "east":
            print("""
            The tribes pet bear devoured you
            and you died Develop more
            """)
            new_life()
        elif dir == "west":
            print("""
            Disgusted with the fact you ate human meat,
            you killed yourself
            """)
            new_life()
        else:
            dir = input(valid_move)

# Woods
def woods():

        dir = input("~> ")

        if dir == "north":
            print("""
                    Develop more
            """)
        elif dir == "south":
            print("""
                    Develop More
            """)
        elif dir == "east":
            print("""
                    Develop More
            """)
        elif dir == "west":
            print("""
                    Develop More
            """)
        else: 
            dir = input(valid_move)

def new_life(lives = 2):
        lives -= 1
        if lives == 0:
            print("""
        Oh no! You lost all your lives.

        Play again? yes/no
        """)
            while True:
                dir = input(prompt)
                    
                if dir == "yes":
                    lives = 3
                    game()
                elif dir == "no":
                    print("\t\tGoodbye!")
                    exit(0)
                else:
                    dir = input(valid_move)
        else:
            game()
        

def play_again():
    play_again = input(prompt)
    while True:
        if play_again == "yes":
            game()
        elif play_again == "no":
            print("\t\tGoodbye!")
        else:
            dir = input(valid_move)

#Game
def game():
    print("""
    You awake in the center of a crossroad
    You can go north, east, south, or west
    Some parts of this game will make it impossible to go back
    Choose carefully and goodluck!
    """)

    dir = input(prompt)

    while True:
        if dir == "north":
            daves_cliff()
        elif dir == "south":
            print("""
                    Still being developed
            """)
        elif dir == "east":
            print("""
                    Still being developed
            """)
        elif dir == "west":
            print("""
                    Still being developed
            """)
        else:
            dir = input(valid_move)

game()
