from abc import *

class Printer(ABC) :
	@abstractmethod
	def printit(self, text) : pass

	@abstractmethod
	def disconnect(self) : pass

class EPSON(Printer) :
	def printit(self, text) :
		print('printing from EPSON printer')
		print(text)

	def disconnect(self) :
		print('printing completed on EPSON printer')

class HP(Printer) :
	def printit(self, text) :
		print('printing from HP printer')
		print(text)

	def disconnect(self) :
		print('printing completed on HP printer')


with open('config.txt', 'r') as f :
	pname = f.readline()

# it will read class name from the file whether it is HP or EPSON (written in config.txt file)

classname = globals()[pname]
print(pname)
print(classname)
x = classname()
x.printit('this data has to print...')
x.disconnect()


'''

EPSON
<class '__main__.EPSON'>
printing from EPSON printer
this data has to print...
printing completed on EPSON printer

'''