# Original Solution
def DrivingSchool(time):

    totalCost = 0

    if time > 5:
        totalCost += 30
        if time < 60:
            print(totalCost)
            return
        else:
            time -= 60
        if time/30 > 1:
            totalCost = totalCost + (10 * ((time//30)))
            time -= 30 * ((time//30))
        if time > 5:
            totalCost = totalCost + 10

    print(totalCost)


DrivingSchool(84)
DrivingSchool(102)
DrivingSchool(273)
