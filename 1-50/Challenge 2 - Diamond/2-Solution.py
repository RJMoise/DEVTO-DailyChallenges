def createDiamond(size):
    # Diamond but have an odd max width
    if ((size < 0) or (size % 2 == 0)):
        return
    else:
        stableSize = size
        increment = 1
        # Increment from 1 to given size and print
        while(increment <= stableSize):
            print(("*"*increment).center(stableSize))
            increment += 2
        # Decrement back down to 1 and print
        while(size > 1):
            size -= 2
            print(("*"*size).center(stableSize))


createDiamond(11)
