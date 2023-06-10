#  OOP allows you to create objects that have properties (attributes) and behaviors (methods) 
#      associated with them. 
#  Here's the basic syntax for defining classes and properties in Python :


class ClassName:
    def __init__(self, param1, param2, ...):
        self.property1 = param1
        self.property2 = param2
        # more properties

    # methods
    def method1(self, arg1, arg2, ...):
        # code for method1

    def method2(self, arg1, arg2, ...):
        # code for method2

# creating an instance of the class
object_name = ClassName(param1_value, param2_value, ...)



"""
breaking down the syntax :

- class keyword is used to define a class. ClassName is the name of the class you want to define.

- def __init__(self, param1, param2, ...): is the special method called the constructor. It is 
    used to initialize the object's properties. self refers to the instance of the object being 
    created, and param1, param2, etc. are the parameters you pass when creating an object.

- self.property1 = param1 assigns the value of param1 to the property property1 of the object. 
    Similarly, you can define other properties.

- def method1(self, arg1, arg2, ...): is a method defined within the class. It takes self (the instance) 
    as the first parameter, followed by other parameters arg1, arg2, etc.

- Inside the methods, you can write code that defines the behavior of the object. You can access the 
    object's properties using self.property_name.

- object_name = ClassName(param1_value, param2_value, ...) creates an instance of the class. object_name 
    is the variable name you assign to the object. You pass values for the constructor parameters 
    (param1_value, param2_value, etc.) when creating the object.

Once you have created an object, you can access its properties using dot notation 
(object_name.property_name) and call its methods (object_name.method1()).

"""

