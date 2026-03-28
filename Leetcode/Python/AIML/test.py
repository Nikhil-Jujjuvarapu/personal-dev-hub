# class BankAcc:
#     def __init__(self,balance):
#         self.__balance = balance
    
#     def deposit(self,amount):
#         self.__balance+=amount
    
#     def get_balance(self):
#         return self.__balance
    
# acc = BankAcc(500)
# acc.deposit(1000)
# print(acc._BankAcc__balance)
# print(acc.get_balance())


class Animal():
    def __init__(self):
        print("Constructor")

class Dog(Animal):
    def bark(self):
        super().eat()
        print("barking")

dog = Animal()

# dog.eat()