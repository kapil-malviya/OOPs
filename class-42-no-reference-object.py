'''

find the total number of reference of a object =>

-> sys module contains getrefcount() function for this purpose  

'''


import sys 

class Test :
	pass

t1 = Test()
t2 = t1
t3 = t1
t4 = t1
t5 = t2

print(sys.getrefcount(t1))         #  6 (above : 5 & one default reference variable self)



#  For every object, Python internally maintains one default reference variable self.,