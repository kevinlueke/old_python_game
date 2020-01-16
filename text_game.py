prompt = "~> "
print("""
        You awake in the center of a crossroad
        You can go north, east, south, or west
        Some parts of this game will make it impossible to go back
        Only one way is right
        Choose carefully and goodluck!
        """)

dir = input(prompt)

# Cliff
def cliff():
    print("""
            You came upon a cliff and got too close 
            falling into the cold water
            luckily, you survive
            unluckily, you lose your vision
            """)

    dir = input(prompt)

    if dir == "south":
        cave()

# Cave
def cave():
        print("""
                You make it into a cave and feel warmth coming from the east
                To the south you hear whispering
                The west provides no notable sound or feeling
        """)

        dir = input(prompt)

        if dir == "east":
            print("""
                    In front of you was a pit of lava
                    Unable to see, you fell in
                    and died
            """)
def cannibal():
    # Cannibal Tribe
    if dir == "south":
        print("""
                You came upon a tribe of cannibals
                luckily, they invited you into their tribe
                they gave you a healing remedy to fix your eyes
                and they also gave you food
        """)

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
            
            dir = input(prompt)

            if dir == "north":
                print("""
                        hbkh
                        """)
            elif dir == "east":
                print("""
                        jd
                        """)
            elif dir == "south":
                print("""
                        bej
                        """)
            elif dir == "west":
                print("""
                        djb
                        """)
            else:
                print("""
                        Type a correct direction please
                        """)

                dir = input(prompt)

    elif dir == "north":
        print("""
                Without being able to see
                you ran into the wall and cracked your head open
                and you died
        """)

    elif dir == "west":
        print("""
                You stepped into some weird liquid on the ground
                You had an epiphany and put the liquid on your eyes
                You can now see two dark paths ahead to the north and west
        """)

        dir = input(prompt)

        # Woods
        if dir == "north":
            print("""
                    You found a ladder leading up
                    Naturally, you climbed it
                    You are in the middle of the woods
                    Any direction may be gone
             """)

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
                    You walked into a wall
                    and cracked your head open
                    and you died
            """)
        else:
            print("""
                    This world did not recognize the direction you went
                    and kicked you out
            """)

#Game
def game():
    if dir == "north":
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
        game()

game()
