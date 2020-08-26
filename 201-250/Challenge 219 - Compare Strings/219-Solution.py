def compareStrings(inputString, characterCheck):

    occurence = 0
    for elements in inputString:
        if elements == characterCheck:
            occurence += 1

    print(occurence)


compareStrings("test", "t")
compareStrings('oh goodness gracious', 'o')
compareStrings('howdy, pardner', 'd')
compareStrings('Incumbent President', 'e')
compareStrings('', 'z')
