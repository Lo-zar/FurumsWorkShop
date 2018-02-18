class ATM:
    print("_-___----____ ATM MACHINE ____----___-_")

    def __init__(self, Balance, Bank_Name):
        self.Balance = Balance
        self.Bank_Name = Bank_Name
        self.Withdrawals_List = []

    def Withdraw(self, Request):
        print("WELCOME TO", self.Bank_Name)
        print("Available Balance =", self.Balance)
        self.seperator()

        if Request > self.Balance:
            print("I can,t Give You All This Money @_@ , Your Balance Is " + str(self.Balance))
        elif Request <= 0:
            print("Same Thing Was False? ,Try Agein @_@")
        else:
            self.Withdrawals_List.append(Request)
            self.Balance -= Request
            Bills = [100, 50, 10, 5, 2, 1]
            for Currency in Bills:
                Bills_number = int(Request / Currency)
                Request -= Currency * Bills_number
                for i in range(Bills_number):
                    print("give", Currency)
            if Request > 0:
                print("give", Request)

        self.seperator()
        return self.Balance

    def show_Withdrawals(self):
        print("_-___----____ ATM MACHINE ____----___-_")
        previous_Balance = self.Balance + sum(self.Withdrawals_List)
        print("Previous Balance:", previous_Balance)

        for Withdrawal in self.Withdrawals_List:
            print("withdrawal:", Withdrawal)

        print("All withdrawals:", sum(self.Withdrawals_List))
        print("Available Balance:", previous_Balance - sum(self.Withdrawals_List))
        self.seperator()

    def seperator(self):
    	print("_-___----____ ATM MACHINE ____----___-_")


Balance1 = 500
Balance2 = 1000

atm1 = ATM(Balance1, "BNP BANK")
atm2 = ATM(Balance2, "WATAN BANK")

atm1.Withdraw(300)
atm1.Withdraw(250)

atm2.Withdraw(200)
atm2.Withdraw(100)
