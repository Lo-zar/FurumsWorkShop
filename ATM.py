def withdrawl(Balance, Request):
	allowed_papers = [100, 50, 20, 10, 5, 2, 1]
	if Request > Balance:
		print("You Don,t Have All This Money: You Only Have "+ str (Balance))
	elif Request <= 0:
		print("Requested Balance Must Be More Than 0")
	else:
		print("Current Balance = "+ str (Balance))
		print("Requested = ", Request)
		Balance = Balance - Request
		for i in allowed_papers:
			while Request >= i:
				Request -= i
				print("Give:", i)
		print("Remainder Balance "+ str (Balance))
		return Balance

My_Balance = 577
My_Balance = withdrawl(My_Balance,277)
My_Balance = withdrawl(My_Balance,250)
My_Balance = withdrawl(My_Balance,250)

