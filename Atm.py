class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def check_balance(self):
        print("Your current balance is 6000")

    def withdrawl(self,amount):
        new_amount = 6000 - amount
        print("you have withdrawn amount "+str(amount) +". Your remaining balance is "+ str(new_amount))

def main():
    Card_number = input("insert your card number: ")
    pin_number  = input("enter your pin number: ")

    new_user =  Atm(Card_number ,pin_number)

    print("Choose a number")
    print("1.Balance Enquriy   2.withdrawl")
    activity = int(input("enter a number : "))

    if (activity == 1):
        new_user.check_balance()
    elif (activity == 2):
        amount = int(input("enter the amount: "))
        new_user.withdrawl(amount)
    else:
        print("please enter valid  number")


if __name__ == "__main__":
    main()
