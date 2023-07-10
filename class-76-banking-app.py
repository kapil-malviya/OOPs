## mini banking application :

class Account :
	def __init__(self, name, balance, min_balance) :
		self.name = name
		self.balance = balance
		self.min_balance = min_balance

	def deposit(self, amount) :
		self.balance+=amount

	def withdraw(self, amount) :
		if self.balance-amount >= self.min_balance :
			self.balance-=amount
		else :
			print('sorry.. insufficient funds')

	def printstatement(self) :
		print('account balance : ', self.balance)


class Current(Account) :
	def __init__(self, name, balance) :
		super().__init__(name, balance, min_balance = -1000)

	def __str__(self) :
		return "{}'s current account with balance : {}".format(self.name, self.balance)


class Saving(Account) :
	def __init__(self, name, balance) :
		super().__init__(name, balance, min_balance = 0)

	def __str__(self) :
		return "{}'s saving account with balance : {}".format(self.name, self.balance)



c = Saving('kapil', 8000)
print(c)                     #  kapil's saving account with balance : 8000
c.deposit(8000)
c.printstatement()           #  account balance :  16000
c.withdraw(4000)
print(c)                     #  kapil's saving account with balance : 12000
c.withdraw(3000)
print(c)                     #  kapil's saving account with balance : 9000
print()


x = Current('kapil-8', 1000)
x.deposit(200)
print(x)                     #  kapil-8's current account with balance : 1200
x.withdraw(1300)
print(x)                     #  kapil-8's current account with balance : -100