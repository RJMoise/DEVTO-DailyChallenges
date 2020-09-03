def stringPeeler(string):
    # Check if string is long enough to work with
    if len(string) < 2:
        print("This string is not long enough")
        return
    # Create new string based off the input without the first and last characters
    else:
        string = string[1:-1]
        print(string)


stringPeeler("testme")
