#inheritance extend one class variables and functions to another class
#one class to oneclass  is single inheritance
#once class can access more than 2 class means multile inheritance
#Multilevel inheritance means class can access another class inheritance class values son can access dad class with grandpa class
#Hierarchy inheritance base class dad is acccess multiple class son1,son2,son3 means heirarchy
#hybrid inheritance is both muktilevelk and heirarchial and single like ever combination


class land():
	def important(self):
		print("important land")

class grandpa():
	def phone(self):
		print("grandpa phone")

class dad(grandpa):
	def money(self):
		print("Dad's money")


class mom():
	def sweet(self):
		print("Mom's sweet")

class son(dad,mom):
	def laptop(self):
		print("Son's laptop")

class son1(dad,land):
	pass

class son2(dad,land):
	pass

class son3(dad):
	pass


s2=son2()
s2.money()



ram=son()
ram.laptop()
ram.phone()
ram.money()
ram.sweet()

d1=dad()
d1.money()
d1.phone()