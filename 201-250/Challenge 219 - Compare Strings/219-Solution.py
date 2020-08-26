def compareStrings(inputString, characterCheck):

    lowerString = inputString.lower()
    occurence = 0

    if len(characterCheck) == 0:
        print("There must be a character to check against.")
        return

    else:
        for elements in lowerString:
            if elements == characterCheck:
                occurence += 1

        print(occurence)


compareStrings("How many T's do I have", "t")
compareStrings('oh goodness gracious', 'o')
compareStrings('howdy, pardner', 'd')
compareStrings('Incumbent President', 'e')
compareStrings('', 'z')
compareStrings('Test', '')
