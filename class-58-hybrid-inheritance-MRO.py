'''
# Method Resolution Order (MRO) :

=> In Hybrid Inheritance the method resolution order is decided based on MRO algorithm.
	-> This algorithm is also known as C3 algorithm.
	-> Samuele Pedroni proposed this algorithm.

=> It follows DLR (Depth First Left to Right)
	-> Child class will get more priority than Parent class
	-> Left Parent class will get more priority than Right Parent class
		class C(P1, P2, P3) :

	-> In MRO, python will consider / visit any class only once


## We can find MRO of any class by using mro() function.
	: print(ClassName.mro())



class D : pass
class E : pass
class F : pass
class B(D, E) : pass
class C(D, F) : pass
class A(B, C) : pass

print(A.mro())
#[<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class '__main__.E'>, <class '__main__.F'>, <class 'object'>]

print(B.mro())
#[<class '__main__.B'>, <class '__main__.D'>, <class '__main__.E'>, <class 'object'>]

print(C.mro())
#[<class '__main__.C'>, <class '__main__.D'>, <class '__main__.F'>, <class 'object'>]

print(D.mro())
#[<class '__main__.D'>, <class 'object'>]

print(E.mro())
#[<class '__main__.E'>, <class 'object'>]

'''


class A:pass
class B(A):pass
class C(A):pass
class D(B,C):pass
print(A.mro())
print(B.mro())
print(C.mro())
print(D.mro()) 


'''  ->> 

[<class '__main__.A'>, <class 'object'>]
[<class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
[<class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]          '''


'''

mro(o) = object
mro(D) = D, object
mro(E) = E, object
mro(F) = F, object
mro(B) = B, D, E, object
mro(C) = C, D, F, object
mro(A) = A + Merge(mro(B), mro(C), BC)
	= A + Merge(BDEO, CDFO, BC)
	= A + B + Merge(DEO, CDFO, C)
	= A + B + C + Merge(DEO, DFO)
	= A + B + C + D + Merge(EO, FO)
	= A + B + C + D + E + Merge(O, FO)
	= A + B + C + D + E + F+ Merge(O, O)
	= A +B + C + D + E + F + O


'''