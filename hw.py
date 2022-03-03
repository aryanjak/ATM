class ATM:
    def __init__(self, name, balance, pin):
        self.name = name
        self.balance = balance
        self.pin = pin

    def getname(self):
        print("The name of the Car is:" + self.name)

    def getbalance(self):
      print("Your balance is:"+ str(self.balance))


    def gM(self):
        print("pin of the car:" + self.pin)

    def Wd(self):
        amt = int(input("Enter Amount to Widthdraw:"))
        if amt <= self.balance:
            self.balance = self.balance - amt
            print("Required Amount is WIDTHDRAWED The amount you widthdrawed is:" +
                  str(amt) + "The remaining balance is:" + str(self.balance))

        else:
            print("Sorry!! This amount you enterd cant be widthdrawed for further assistance contact XXXX-XXX-XXXX")

    def deposit(self):
        amtt = int(input("Enter the amount you want to deposit:"))
        self.balance = self.balance + amtt
        print("DEPOSI SUCCESSFUL!! The amount you deposited is:" + str(amtt) + "Balance is:" + str(self.balance
                                                                                                   ))


costumer = ATM("Damru ji" , 6598 , 1236548)
costumer.getbalance()
costumer.Wd()
costumer.deposit()