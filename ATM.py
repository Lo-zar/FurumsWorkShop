class ATM:
    print("_-___----____ ATM MACHINE ____----___-_")

    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdrawals_list = []

    def Withdraw(self, request):
        print("WELCOME TO {0}".format(self.bank_name))
        print("Your Balance Is: {0}$ And You Requested {1}$.".format(
            self.balance, request))

        if self.balance <= 0:
            print("Insufficient Balance, Please Deposit Money And ,Try Agein @_@")

        elif request > self.balance:
            print("I can,t Give You All This Money @_@ , Your Balance Is " + str(self.balance))

    def withdrawals_list:
        self.withdrawals_list.append(request)
        self.balance -= request
        bills = [100, 50, 10, 5]
        for currency in bills:
            bills_number = int(request / currency)
            request -= currency * bills_number
            for i in range(Bills_number):
                print("give", currency)
            if request > 0:
                print("give", request)

        self.seperator()
        return self.balance

    def show_withdrawals(self):
        print("_-___----____ ATM MACHINE ____----___-_")
        previous_balance = self.balance + sum(self.withdrawals_list)
        print("previous balance:", previous_balance)
        index =1
        for Withdrawal in self.Withdrawals_List:
            print("{0} withdrawal No.{1}: {2}$".format(self.bank_name, index, withdrawal))
            index += 1

        print("all withdrawals:", sum(self.withdrawals_list))
        print("available balance:", previous_balance - sum(self.withdrawals_list))
        self.seperator()

    def seperator(self):
    	print("_-___----____ ATM MACHINE ____----___-_")


balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "BNP BANK")
atm2 = ATM(balance2, "WATAN BANK")

atm1.withdraw(500)
atm1.withdraw(250)

atm2.withdraw(200)
atm2.withdraw(100)
