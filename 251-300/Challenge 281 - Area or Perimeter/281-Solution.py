def AreaOrPeremeter(w, l):

    # If sides are equal it is a square, calculate area
    if w == l:
        a = w*l
        print("The area of your square is: " + str(a))

    # Sides are not equal so it is a rectangle, calculate perimeter
    else:
        p = 2 * (w+l)
        print("The perimeter of your rectangle is: " + str(p))


AreaOrPeremeter(3, 7)
AreaOrPeremeter(5, 5)
