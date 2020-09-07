def additonNoCarry(firstNum, secondNum):

    # My Solution involves converting the numbers to strings, filling them to the same length
    # and then performing addition, and adding the output to the final string.
    firstNumString = str(firstNum)
    secondNumString = str(secondNum)
    finalNumString = ""

    # If the numbers are not the same length, add zeros to the front until they are
    if len(firstNumString) != len(secondNumString):
        if len(firstNumString) > len(secondNumString):
            secondNumString = secondNumString.zfill(len(firstNumString))
        else:
            firstNumString = firstNumString.zfill(len(secondNumString))

    # Iterate through the string indexes, add and push to final string
    for i in range(len(firstNumString)):
        finalNumString = finalNumString + \
            str((int(firstNumString[i]) + int(secondNumString[i])))

    print(finalNumString)


additonNoCarry(1222, 30277)
additonNoCarry(1236, 30889)
additonNoCarry(49999, 49999)
