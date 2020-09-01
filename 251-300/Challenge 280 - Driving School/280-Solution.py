# Original Solution
def DrivingSchool(time):

    totalCost = 0

    # Only times above 5 minutes are charged
    if time > 5:

        # Inital cost is always $30 for the first our, so add that cost and subtract that time
        totalCost += 30

        if time < 60:
            print(totalCost)
            return
        else:
            time -= 60

        # Checks for every subsequent half an hour and charges $10 per
        if time/30 > 1:
            totalCost = totalCost + (10 * ((time//30)))
            time -= 30 * ((time//30))

        # If whatever time reamains is more thatn 5 minutes, charge a final $10
        if time > 5:
            totalCost = totalCost + 10

    print(totalCost)


DrivingSchool(84)
DrivingSchool(102)
DrivingSchool(273)
