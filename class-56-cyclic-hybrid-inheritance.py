'''

## Cyclic Inheritance :

-> The concept of inheriting properties from one class to another class in cyclic way, 
	is called Cyclic inheritance. 

->Python does not support Cyclic Inheritance,


class A(B) :
	pass

class B(A) :
	pass

----------------------------------------------------------------------------------------


##  Hybrid Inheritance :

-> Combination of Single, Multi level, Multiple and Hierarchical inheritance is known
	as Hybrid Inheritance...

-->> Method Resolution Order (MRO) :

		-> In Hybrid Inheritance the method resolution order is decided based on MRO 
			algorithm.
		-> This algorithm is also known as C3 algorithm.
		-> Samuele Pedroni proposed this algorithm.
		-> It follows DLR (Depth First Left to Right)
			i.e Child will get more priority than Parent.
			Left Parent will get more priority than Right Parent               


'''