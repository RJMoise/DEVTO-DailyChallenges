import random


def blockWalk(lengthOfWalk):

    compass = ["n", "s", "e", "w"]
    pathToWalk = []
    tempDirection = ""
    i = 0

    if lengthOfWalk % 2 != 0:
        print("Please only enter an even number or you'll never make it back home!")
        return

    else:
        oneWay = lengthOfWalk/2
        while i < int(oneWay):
            direction = random.randint(0, 3)

            if direction == tempDirection:
                continue

            if direction == 0 or direction == 2:
                if len(pathToWalk) == 0:
                    pathToWalk.insert(0, compass[direction])
                    pathToWalk.insert(1, compass[direction+1])
                else:
                    insertIndex = int(len(pathToWalk)/2)
                    pathToWalk.insert(insertIndex, compass[direction])
                    pathToWalk.insert(insertIndex+1, compass[direction+1])

            elif direction == 1 or direction == 3:
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
