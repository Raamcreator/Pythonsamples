# r read
# w write
# a append

f=open("/Users/raam/Documents/Pythoncodes/files/fruits.txt","w")
# content=f.read()
# print(f)
# f.close()

f.write("banana\n")
f.write("mango\n")
f.close()

# f=open("/Users/raam/Documents/Pythoncodes/files/fruits.txt","r+")
# print(f.read())
# f.close()

f=open("/Users/raam/Documents/Pythoncodes/files/fruits.txt","a")
f.write("Apple\n")
f.write("Orange")
f.close()

f=open("/Users/raam/Documents/Pythoncodes/files/fruits.txt","r+")
print(f.readline())
f.close()