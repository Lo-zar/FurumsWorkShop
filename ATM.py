def withdrawl(Balance, Request):
    result = Balance
    allowed_papers = [100, 50, 20, 10, 5, 2, 1]
    sizer = "_-___----____ ATM MACHINE ____----___-_"
    print(sizer)
    if Request <= Balance:
        for i in allowed_papers:
            while Request >= i:
                print("Give:", i)
                Request -= i
                Balance -= i
        print("Remainder Balance " + str(Balance))
        return Balance
    elif Request >= Balance:
        print("You Don,t Have All This Money, Your Balance Is " + str(Balance))
    print(sizer)
My_Balance = 577
My_Balance = withdrawl(My_Balance, 277)
My_Balance = withdrawl(My_Balance, 250)
My_Balance = withdrawl(My_Balance, 250)
