
### Garbage Collection :

'''

-> In old languages like C++, programmer is responsible for both creation 
	and destruction of objects. Usually programmer taking very much care 
	while creating object, but neglecting destruction of useless objects. 
	Because of his neglectance, total memory can be filled with useless objects 
	which creates memory problems and total application will be down with 
	out of memory error.

-> But in Python, We have some assistant which is always running in the background 
	to destroy useless objects. Because of this assistant the chance of failing 
	Python program with memory problems is very less. This assistant is nothing 
	but Garbage Collector.

-> Hence the main objective of Garbage Collector is to destroy useless objects.

-> If an object does not have any reference variable then that object eligible 
	for Garbage Collection.,


## how to enable and disable Garbage Collector in our program :

-> By default Gargbage collector is enabled, but we can disable based on our 
	requirement. In this context we can use the following functions of gc module.

	-> gc.isenabled()
		returns True if gc enabled

	-> gc.disable()
		to disable gc explicitly

	-> gc.enable()
 		to enable gc explicitly

'''


import gc

print(gc.isenabled())        # True

gc.disable()
print(gc.isenabled())        # False

gc.enable()
print(gc.isenabled())        # True