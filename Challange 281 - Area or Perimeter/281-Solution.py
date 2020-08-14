def AreaOrPeremeter(w, l):
    if w == l:
        a = w*l
        print("The area of your square is: " + str(a))
    else:
        p = 2 * (w+l)
        print("The peremeter of your rectangle is: " + str(p))


AreaOrPeremeter(3, 7)
AreaOrPeremeter(5, 5)
