# __init__ is constructor is a unique  and no need to call whenever object is created thsi will be automatically called
#denoting current object is self key word


class laptop():
	def __init__(self):
		self.price=0
		self.ram=""
		self.proce=""		 
	def display(self):
		print("Price:",self.price)
		print("ram:",self.ram)
		print("Processer:",self.proce)

hp=laptop()
hp.price=50000
hp.ram="8GB"
hp.proce="i5"
hp.display()
# print("hp laptop config:",hp.price,hp.proce,hp.ram)
# hp.display()

dell=laptop()
dell.price=65000
dell.ram="16GB"
dell.proce="i7"
dell.display()