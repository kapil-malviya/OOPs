
# destructor will execute only when object will be destroyed...


import time 

class Test :
	def __init__(self) :
		print('constructor execution..')

	def __del__(self) :
		print('destructor execution..')


l1 = [Test(), Test(), Test()]

time.sleep(8)

del l1

print('end')


''' output without deleting object l1 : 

constructor execution..
constructor execution..
constructor execution..
end
destructor execution..
destructor execution..
destructor execution..                


    output after deleting object l1 : 

constructor execution..
constructor execution..
constructor execution..
destructor execution..
destructor execution..
destructor execution..
end

'''