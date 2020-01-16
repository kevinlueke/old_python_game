import random
prompt = "~> "
lives = 3
#walls of caves haev colors, white cave black cave.....
# Starting Script
#eat meet be healed

# Cliff
def cliff():
    dir = input(prompt)

    if dir == "south":
        print("""
            You make it into a cave and feel warmth coming from the east
            To the south you hear whispering
            The west provides no notable sound or feeling
            """)
        cave()

# Cave Entrance
def cave():
        
        dir = input(prompt)

#  west
        if dir == "east":
            print("""
                As you walk towards the heat it becomes significantly hotter
                So hot that without being able to see if there's anywhere else to go,
                You turn around
            """)
        elif dir == "north":
            print("""
                You returned back to the water you fell into
            """)
            cliff()
        elif dir == "south":
            #idea instead of being spared make it random as to what they choose
            print("""
                You came upon a tribe of cannibals
                luckily, they spared you 
                they gave you a healing remedy to fix your eyes
                and they also gave you food for your journey
            """)
            cannibal()
        elif dir == "west":
            print("""
                    You stepped into some weird liquid on the ground
                    The liquid has a 70% of healing your eyes and a 30% chance of killing you
                    Type yes to use it or no to head back Cave Entrance
            """)
            heal = input(prompt)
            if heal == "yes":
                if random.randint(1, 100) >= 30:
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
                    play_again()

# Deeper Cave
def deeper_cave():

    dir = input(prompt)

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
    elif dir == "south":
        print("""
                You walked into a wall
                and cracked your head open
                and you died
        """)
    elif dir == "east":
        print("""
            You are at the ____ cave
            """)
        cave()
    else:
        print("""
            Please enter a valid move
            """)
        deeper_cave()

# Cannibal Tribe
def cannibal():
    dir = input(prompt)

    if dir == "south":
        print("""
                You squeeze through a crack in the cave
                to the north you see a sliver of light
                to the west more darkness
        """)
    elif dir == "north":
        print("""
                The tribe saw you leaving and killed you
                and you died Develop more
        """)
    elif dir == "east":
        print("""
                The tribes pet bear devoured you
                and you died Develop more
        """)
    elif dir == "west":
        print("""
                Disgusted with the fact you ate human meat,
                you killed yourself
        """)
    else:
        print("""
                This world did not recognize the direction you went
                and kicked you out
                """)

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
            print("""
                    This world did not recognize the direction you went
                    and kicked you out
            """)
def play_again():
    play_again = input(prompt)
    if play_again == "yes":
        game()
    elif play_again == "no":
        print("Goodbye!")
    else:
        print("Please enter a valid move")
        play_again()

#Game
def game(new_life = True):
    if new_life == True:
        print("""
                You awake in the center of a crossroad
                You can go north, east, south, or west
                Some parts of this game will make it impossible to go back
                Only one way is right
                You have 3 lives
                Choose carefully and goodluck!
                """)

    dir = input(prompt)

    if dir == "north":
        print("""
                You came upon a cliff and got too close 
                falling into the cold water
                luckily, you survive
                unluckily, you lose your vision
                """)
        x = "blind"
        cliff()
    elif dir == "south":
        print("""
                You swam right into a school of minnows
                and died
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
        print("""
                Please enter a valid move
        """)
        game(new_life = False)

game()
