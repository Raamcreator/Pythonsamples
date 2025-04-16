class student:
	def __init__(self):
		self.name="Ram"
		self.regno="783186"
	def display(self):
		print("name:",self.name)
		print("regno:",self.regno)

s1=student()
s1.display()
s2=student()
s2.name="Divya"
s2.regno="57878"


class fruit:
	def __init__(self,col):
		self.color=col

apple=fruit("red")
print(apple.color)


class teacher:
	def __init__(self,n,r):
		self.name=n
		self.regno=r
	def disply(self):
		print("name:",self.name)
		print("regno:",self.regno)


t1=teacher("teacher1","123")
t2=teacher("teacher2","1234")
t1.disply()
t2.disply()


class calculator:
	def __init__(self,a,b):
		self.num1=a
		self.num2=b
	def add(self):
		print("add:",self.num1+self.num2)

obj1=calculator(10,2)
obj1.add()