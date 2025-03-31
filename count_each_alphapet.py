"""
Input = "bbbbcccaad"
output = [4,3,2,1]
"""

# def f_count_each_element(input:str)->list:
# 	counter=1
# 	l=[]
# 	for i in range(1,len(input)):
# 		if(input[i]==input[i-1]):
# 			counter+=1
# 		else:
# 			l.append(counter)
# 			counter=1
# 	l.append(counter)
# 	return l

# input="bbbbcccaad"
# print(f_count_each_element(input))


from ordered_set import OrderedSet
def f_count_each_element(input:str)->list:
	input_set=OrderedSet(input)
	l=[]
	for i in input_set:
		l.append(input.count(i))
	return l

input="bbbbcccaaddddddd"
print(f_count_each_element(input))
 