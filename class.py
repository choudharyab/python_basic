#Simple program for class and object
class Test:
    def __init__(self,id,name):
        self.id=id
        self.name=name

t=Test(1,'anup')
print t.id
print t.name

#program for calculating area
class Area:
    def __init__(self):
        self.width=100
        self.length=200
    def area(self):
        return self.width*self.length
t=Area()
t.area()
print t.area()

#program for bank account
class Bank:
    def __init__(self,acc_no,name,amount):
        self.acc_no=acc_no
        self.name=name
        self.amount=amount

    def deposit(self,amount):
        self.amount=self.amount+amount
        print self.amount

    def withdraw(self,amount):
        if(self.amount<amount):
            print "insufficient balance"
        else:
            self.amount=self.amount-amount
            print "Remaininb balance is ",self.amount
    def check(self,amount):
        print "Balance is ",self.amount

    def display(self):
        print(self.acc_no+" "+self.name+" "+self.amount)
b=Bank(121,'anup',1200)
b.deposit(200)
print b.deposit
b.withdraw(2000)
print b.withdraw
print b.check
print b.display

