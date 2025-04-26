class laptop():
	price=0
	processor=""
	ram=""

hp=laptop()
dell=laptop()
lenova=laptop()

hp.price=50000
hp.processor="i5"
hp.ram="8GB"

dell.price=65000
dell.processor="i7"
dell.ram="16GB"

print("hp laptop config:",hp.price,hp.processor,hp.ram)
print("dell laptop config:",dell.price,dell.processor,dell.ram)