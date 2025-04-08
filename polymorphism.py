#same function name being used for different types 
#base class=parent class child class = derived class
#if child class overides parant class method means method override which is also polymorphism because samfunction name but used diff is pa

# def add(a,b,c=0):
# 	print(a+b+c)

# add(2,5,10)
# add(1,2)


class animal():
	def sound(self):
		print("Animal makes sound")

class Dog(animal):
	def sound(self):
		print("Dog Parks")

class bird(animal):
	def sound(self):
		print("Birds Sings")

a1=animal()
a1.sound()
d=Dog()
d.sound()
b=bird()
b.sound()