"""
find common 

"""

def f_commonalpha(inp1:str,inp2:str)->list:
	input_set1=set(inp1)
	input_set2=set(inp2)
	print("Common letters:",input_set1&input_set2)
	print("All letters:",input_set1|input_set2)
	print("A-B:",input_set1-input_set2)
	print("B-A:",input_set2-input_set1)
	return 0



inp1="Ramkumar"
inp2="raghulan"
f_commonalpha(inp1,inp2)