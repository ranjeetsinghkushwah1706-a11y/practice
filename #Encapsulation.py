#Encapsulation
#Wrapping data and function into a single unit(object)

class Account:
    def __init__(self, acc_no, acc_balance):
        self.__balance = acc_balance     # private variable
        self.__acc_no = acc_no

    def credit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid amount")
        return self.__balance

    def debit(self, amount):
        if amount > self.__balance:
            print("Insufficient Balance")
        elif amount <= 0:
            print("Invalid amount")
        else:
            self.__balance -= amount
        return self.__balance

    def display(self):
        print("Account No:", self.__acc_no, "Balance:", self.__balance)


# Creating objects
cust1 = Account(101, 50000)
cust2 = Account(102, 30000)

# Operations
cust1.credit(4000)
cust2.debit(1000)

# Display
cust1.display()
cust2.display()
