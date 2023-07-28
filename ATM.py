import time


class ATM :
    def __init__(self):
        
        self.balance=int(input("Enter your amount that can halp you to check the code properly  :"))
        self.pin=int(input("Creat your own 4 digit pin to acsses the code  :"))
        self.Transection_History=[]
        self.manu()
        
    def manu (self):
            print("""Choose Option:
    1.Chack Balance
    2.Deposit
    3.Whitdrow
    4.Transaction History
    5.Exit""")
            option=int(input("Enter your option :  "))
            if option==1:
                self.chack_Balance()
            elif option==2:
                self.Deposit_Balance()
            elif option==3:
                self.Withdrow_Balance()
            elif option==4:
                self.Transaction()
            else:
                self.Exit_option()

    def chack_Balance(self):
            print("Enter insert your Card :")
            time.sleep(0)
            input_pin=int(input("Enter Your pin "))
            if self.pin==input_pin :
                    print("*"*50)
                    print("Your Account Balance is ",self.balance)
                    print("*"*50)
            else:
                        print("Wrong pin  :")
            self.manu()
    def Deposit_Balance(self):
            print("Insert your Card :")
            time.sleep(0)
            input_pin=int(input("Enter Your pin "))
            if self.pin==input_pin:
                    input_Amount=(int(input("Enter your Deposit amount : ")))
                    self.balance=self.balance+input_Amount
                    print("*"*50)
                    print("Your Updated Balance is ",self.balance)
                    print("*"*50)
                    self.Transection_History.append(f"Deposit :+{input_Amount}")
            else:
                print("Wrong pin :")
            self.manu()
    def Withdrow_Balance(self):
        print("Insert your Card :")
        time.sleep(0)
        input_pin=int(input("Enter Your pin "))
        if self.pin==input_pin:
                Withdrow=int(input("Enter Withdrow Amount :"))
                if self.balance<Withdrow:
                    print("unsufficient Balance :")
                else:
                    self.balance=self.balance-Withdrow
                    print("*"*50)
                    print("Your updated Amount is ",self.balance)
                    print("*"*50)
                    self.Transection_History.append(f"Withdrow :-{Withdrow}")
        else:
                print("Wrong pin")
        self.manu()
    def Transaction(self):
        print("Transaction History :")
        print("  Deposite Transection")
        Deposit_transection=0
        for transaction in reversed(self.Transection_History):
                if "Deposit" in transaction:
                    print(transaction)
                    Deposit_transection+=1
                    if Deposit_transection>=10:
                        break
                
        print(" Withdrow Transection :")
        Withdrow_transection=0
        for transaction in reversed(self.Transection_History):
            if "Withdrow" in transaction:
                print(transaction)
                Withdrow_transection+=1
                if Withdrow_transection>=10:
                    break
        self.manu()
    def Exit_option(self):
        print("Thank You ")
        SystemExit()
Card=ATM()


