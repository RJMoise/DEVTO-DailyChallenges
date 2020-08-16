def createDiamond(size):

    if ((size < 0)or (size % 2 == 0)):
        return
    else:
        stableSize = size
        increment = 1

        while(increment <= stableSize):
            print(("*"*increment).center(stableSize))
            increment += 2
        while(size > 1):
            size -= 2
            print(("*"*size).center(stableSize))


createDiamond(11)
