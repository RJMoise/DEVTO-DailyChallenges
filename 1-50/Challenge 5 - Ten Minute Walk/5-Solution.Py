import random


def blockWalk(lengthOfWalk):

    compass = ["n", "s", "e", "w"]
    pathToWalk = []

    if lengthOfWalk % 2 != 0:
        print("Please only enter an even number or you'll never make it back home!")
        return

    else:
        oneWay = lengthOfWalk/2
        for i in range(int(oneWay)):
            direction = random.randint(0, 3)
            if direction == 0 or direction == 2:
                pathToWalk.insert(0, compass[direction])
                pathToWalk.insert(1, compass[direction+1])

            elif direction == 1 or direction == 3:
                pathToWalk.insert(0, compass[direction])
                pathToWalk.insert(1, compass[direction-1])

        print(pathToWalk)


blockWalk(6)
