def stringPeeler(string):
    if len(string) < 2:
        print("This string is not long enough")
        return
    else:
        string = string[1:-1]
        print(string)


stringPeeler("testme")
