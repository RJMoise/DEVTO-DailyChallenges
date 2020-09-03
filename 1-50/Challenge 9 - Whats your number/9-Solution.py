def phoneNumber(phone):
    # checks if there are enough numbers to create a phone number, and no other chars
    if len(str(phone)) != 10 or not phone.isnumeric():
        print("Please enter a valid amound of numbers. (10)")
    # converts input to string so it can be manipulated into the proper formate
    else:
        strPhone = str(phone)
        area = strPhone[0:3]
        firstPart = strPhone[3:6]
        lastPart = strPhone[6:11]
        print("(" + area + ") " + firstPart + "-" + lastPart)


phoneNumber("0123456789")
