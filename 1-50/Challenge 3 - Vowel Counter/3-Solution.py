def countVowels(string):
    userString = string
    upperCount = 0
    lowerCount = 0

    for stringChars in userString:
        # Checks for uppercase vowels and counts up when found
        if stringChars == "A" or stringChars == "E" or stringChars == "I" or stringChars == "O" or stringChars == "U":
            upperCount += 1
        # Checks for lowercase vowels and counts up when found
        elif stringChars == "a" or stringChars == "e" or stringChars == "i" or stringChars == "o" or stringChars == "u":
            lowerCount += 1

    print("There was " + str(lowerCount) + " lowercase vowels and " +
          str(upperCount) + " uppercase vowels in that string.")


countVowels("How many vowEls Are therE In this OustandIng rUn on sentence?")
