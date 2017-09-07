##
#
# @author Florian CAVASIN
"""
#a variable
a=1 # default type : int

# an empty list
mylist = []

# a filled list
mylist2 = [1,2,3]

#append to a list
mylist.append(10)

# a buggy list
mybuggylist = [1,'a',"Hi"]

#operators
b=a+2
mylist_sum=mylist+mylist2
"""

som=0
n=0

input_list=[1,2,3,4,-7]

for item in input_list:
	if item>0:
		som += item
		n += 1
	elif item==0:
		print('This value is not positive: '+str(item))
	else:
		print('This value is negative '+str(item))
average = som/n
print('Positive elements average is '+str(average))

