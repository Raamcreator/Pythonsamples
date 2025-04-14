#self is used in fuction means instance method
#decorators class method 

class laptop():
	charger="C-Type"
	def __init__(self):
		self.brand=""
		self.price=34

	def setPrice(self,price):
		self.price=price  

	def getPrice(self):
		print(self.price)

	@classmethod
	def setCharger(cls):
		cls.charger="Thunderbolt"
		print("Charger type change to Thunderbolt")

	@staticmethod
	def info():
		print("this is laptop class")


hp=laptop()
hp.setPrice(20000)
hp.getPrice()
# laptop.setCharger(laptop)		
laptop.setCharger()
hp.info()