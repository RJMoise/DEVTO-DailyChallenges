import random


def blockWalk(lengthOfWalk):
    # Array of possible directions to walk in
    compass = ["n", "s", "e", "w"]
    pathToWalk = []
    tempDirection = ""
    i = 0
    # If number is odd there wont be a proper path home
    if lengthOfWalk % 2 != 0:
        print("Please only enter an even number or you'll never make it back home!")
        return

    else:
        # Walking one direction will be half the total walk time
        oneWay = lengthOfWalk/2

        while i < int(oneWay):
            # randomizes direction to walk in
            direction = random.randint(0, 3)
            # this if makes sure the same direction isnt used twice in a row
            if direction == tempDirection:
                continue
            # If N or E, add them and their opposite, S and W
            if direction == 0 or direction == 2:

                # Inserts directions into the middle of the array so it creates a path instead of just back and forth from start to direction and back
                if len(pathToWalk) == 0:
                    pathToWalk.insert(0, compass[direction])
                    pathToWalk.insert(1, compass[direction+1])
                else:
                    insertIndex = int(len(pathToWalk)/2)
                    pathToWalk.insert(insertIndex, compass[direction])
                    pathToWalk.insert(insertIndex+1, compass[direction+1])

            # If S or W, add them and their opposite, N and E
            elif direction == 1 or direction == 3:

                # Inserts directions into the middle of the array so it creates a path instead of just back and forth from start to direction and back
                if len(pathToWalk) == 0:
                    pathToWalk.insert(0, compass[direction])
                    pathToWalk.insert(1, compass[direction-1])
                else:
                    insertIndex = int(len(pathToWalk)/2)
                    pathToWalk.insert(insertIndex, compass[direction])
                    pathToWalk.insert(insertIndex+1, compass[direction-1])

            i += 1

            tempDirection = direction
        print(pathToWalk)


blockWalk(6)
