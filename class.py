# class is collection of function and variables
# object is 

class goa:
	name=""
	drink=""
	def party(self):
		print("lets party")
	def beach(self):
		print("Enjoy Beach")

ram=goa()
Divya=goa()

ram.party()
Divya.beach()
ram.name="Ram"
ram.drink="Yes"
print(ram.name)
print("Drink?",ram.drink)
Divya.name="Divya"
Divya.drink="No"
print(Divya.name)
print("Drink?",Divya.drink)


class nametocheck:
	pass