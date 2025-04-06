#syntex error compile time error
#logical error -> no error by code only in ogic 
#runtime error -> provide invalid input cause

# try:
# 	a=int(input())
# 	b=int(input())
# 	print(a+b)
# except Exception as e:
# 	print("something",e)


# try:
# 	a=input()
# 	b=input()
# 	print(a/b)
# except Exception as e:
# 	print("something",e)

try:
	a=int(input())
	b=int(input())
	# c=input()
	print(a+b)
	# print(d)
except ValueError as e:
	print("Value Eror",e)
except TypeError as e:
	print("Type Error:",e)
except Exception as e:
	print("Something wrong:",e)
finally:
	print("Done")


