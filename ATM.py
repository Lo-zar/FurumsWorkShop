class ATM:
    LOGO = "^^^^^^^^^^^^***$$$ ATM MACHINE $$$***^^^^^^^^^^^^"

    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name
        self.withdrawals_list = []

    def withdrawal(self, request):
        print(ATM.LOGO)
        print("WELCOME TO {0}".format(self.bank_name))
        print("Your Balance Is: {0}$ And You Requested {1}$.".format(
            self.balance, request))

        if self.balance <= 0:
            print("Insufficient Balance, Please Deposit Money And ,Try Agein @_@")

        elif request > self.balance:
            print("I can,t Give You All This Money @_@ , Your Balance Is " + str(self.balance))

        elif request <= 0:
                print("Try Agine")

        else:
            self.withdrawals_list.append(request)
            self.balance -= request
            bills = [100, 50, 10, 5, 2, 1]
            for currency in bills:
                bills_number = int(request / currency)
                request -= currency * bills_number
                for i in range(bills_number):
                    print("give", currency)
            if request > 0:
                print("give", request)
        print(ATM.LOGO)
        return self.balance

    def show_withdrawals(self):
        index = 1
        for Withdrawal in self.withdrawals_list:
            print("{0} withdrawal No.{1}: {2}$".format(self.bank_name, index, Withdrawal))
            index += 1
        print("all withdrawals:", sum(self.withdrawals_list))
        print("available balance:", self.balance)
        print(ATM.LOGO)
balance1 = 500
balance2 = 1000

atm1 = ATM(balance1, "Smart Bank")
atm2 = ATM(balance2, "Baraka Bank")
atm1.withdrawal(277)
atm1.withdrawal(52)
atm1.withdrawal(1000)
atm1.withdrawal(-5)

atm2.withdrawal(654)
atm2.withdrawal(106)
atm2.withdrawal(900)

atm1.show_withdrawals()
atm2.show_withdrawals()
