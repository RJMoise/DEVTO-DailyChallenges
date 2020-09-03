def compareStrings(inputString, characterCheck):

    # Makes whole string lower so all matching characters can be easily counted
    lowerString = inputString.lower()
    occurence = 0

    # Makes sure a character has been chosen to look for.
    if len(characterCheck) == 0:
        print("There must be a character to check against.")
        return

    else:
        # Iterates through the inputString and counts up for each character that matches the given one
        for elements in lowerString:
            if elements == characterCheck:
                occurence += 1

        print("The letter " + characterCheck + " occures " +
              str(occurence) + " times in the sentence.")


compareStrings("How many T's do I have", "t")
compareStrings('oh goodness gracious', 'o')
compareStrings('howdy, pardner', 'd')
compareStrings('Incumbent President', 'e')
compareStrings('', 'z')
compareStrings('Test', '')
