def withdrawl(Balance, Request):
    while Request > 0:
        if Request >= 100:
            Request -= 100
            print ("Give 100")

        if Request >= 50:
            Request -= 50
            print ("Give 50")

        if Request >= 10:
            Request -= 10
            print ("Give 10")

        if Request >= 5:
            Request -= 5
            print ("Give 5")

        if Request >= 1:
            Request -= 1
            print ("Give 1")

    return Request


Balance = 700
Balance = withdrawl(Balance, 555)
