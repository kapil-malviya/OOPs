'''

Linearization(Class) = Class + merge(L(P1), L(P2),,,,,,,ParentList)

L(C) = C + Merge(L(P1), L(P2), P1P2)

	   	   merge(P1P2P3, P1P3P4,  P1P2)

P1P2P3 : 
	- P1 is nothing but the head element
	- and all remaining is the tail element
-> if head is not present in tail part of any other list 
	consider that class in the result

[refer notes alsooo]




---------------------------------

class A : pass
class B : pass
class C : pass
class X(A, B) : pass
class Y(B, C) : pass
class P(X, Y, C) : pass
print(A.mro())  # AO
print(X.mro())  # XABO
print(Y.mro())  # YBCO
print(P.mro())  # PXAYBCO 


--------------------------


mro(A)=A,object
mro(B)=B,object
mro(C)=C,object
mro(X)=X,A,B,object
mro(Y)=Y,B,C,object
mro(P)=P,X,A,Y,B,C,object                      

    ----------

# Finding mro(P) by using C3 algorithm :

Formula : L(X) = X + Merge(L(P1), L(P2),..., ParentList)

L(P) = P + Merge(L(X), L(Y), L(C), XYC)

	= P + Merge(XABO, YBCO, CO, XYC)
    = P + X + Merge(ABO, YBCO, CO, YC)
    = P + X + A + Merge(BO, YBCO, CO, YC)
	= P + X + A + Y + Merge(BO, BCO, CO, C)
	= P + X + A + Y + B + Merge(O, CO, CO, C)
	= P + X + A + Y + B + C + Merge(O, O, O)
	= P + X + A + Y + B + C + O

L(P) = PXAYBCO


'''


class A :
	def m1(self) :
		print('A class Method')

class B :
	def m1(self) :
		print('B class Method')

class C :
	def m1(self) :
		print('C class Method')

class X(A, B) :
	def m1(self) :
		print('X class Method')

class Y(B, C) :
	def m1(self) :
		print('Y class Method')

class P(X, Y, C) :
	def m1(self) :
		print('P class Method')

p=P()
p.m1()    # =>>  P class Method


'''
-> in this example P class m1() method will be considered. If P class 
	does not contain m1() method then as per MRO, X class method will 
	be considered. If X class does not contain then A class method will 
	be considered and this process will be continued.

-> The method resolution in the following order =>>> PXAYBCO

'''