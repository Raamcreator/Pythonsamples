# a=int(input("a:"))
# b=int(input("b:"))
#for i in range(a+1,b):
#    if(i%2==0):
#	    print("Even",i)
#    else:
#	    print("Odd",i)

a=[]
for i in range(5):
	b=int(input("enter number "+str(i+1) + " :"))
	a.append(b)
print(a)
s=0
for j in a:
	s+=j
print(s)



# a=(1,2,3,4,5)
# for i in a:
#     print("list:",i)

# cnt=0
# s=0
# for i in range(a+1,b):
# 	if(i%2==0):
# 		cnt+=1
# 		s+=i
# 		print("even:",i,cnt,s)

# print("count of even:",cnt)
# print("sum of even:",s)



# a=[]
# a.append(10)
# a.append(30)
# print(a)
# b=int(input())
# a.append(b)
# print(a)