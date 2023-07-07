###  Interfaces in python :
'''

-> in general if an abstract class contains only abstract methods such type of abstract class 
	is considered as interface.,


'''



from abc import *

class DBInterface(ABC) :                # interface
	@abstractmethod
	def connect(self) : pass

	@abstractmethod
	def disconnect(self) : pass


class Oracle(DBInterface) :
	def connect(self) :
		print('connecting to the oracle database')

	def disconnect(self) :
		print('disconnecting to the oracle database')


class Sybase(DBInterface) :
	def connect(self) :
		print('connecting to the sybase database')

	def disconnect(self) :
		print('disconnecting to the sybase database')


dbname = input('enter database name : ')

classname = globals()[dbname]      

# globals() : this inbuilt function converts string into class name and returns dictionary of all parameters,

x =  classname()
x.connect()
x.disconnect()


'''

enter database name : Sybase

connecting to the sybase database
disconnecting to the sybase database

'''