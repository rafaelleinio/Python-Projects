class Account:
	def __init__(self, filepath):
		self.filepath = filepath
		with open(filepath,'r') as file:
			self.balance = int(file.read())
	
	def withdraw(self,amount):
			self.balance = self.balance - amount
			self.commit()
	
	def deposite(self,amount):
		self.balance = self.balance + amount
		self.commit()

	def commit(self):
		with open(self.filepath,'w') as file:
			file.write(str(self.balance))

class Checking(Account):
	"""Doc String"""
	classVariable = 10
	
	def __init__(self,filepath,fee):
		Account.__init__(self,filepath)
		self.fee = fee

	def transfer(self, amount):
		self.balance = self.balance - amount - self.fee
		self.commit()

checking = Checking('balance.txt',5)
checking.transfer(10)
print(checking.balance)
#print(checking.__doc__)