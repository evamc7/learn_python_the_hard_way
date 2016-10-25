## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass
	
## dog is-a class
class Dog(Animal):

	def __init__(self, name):
		##name has-a object
		self.name = name
		
##cat is-a class
class Cat(Animal):

	def __init__(self,name):
		##name has-a object
		self.name = name
		
## Person is-a object
class Person(object):

	def __init__(self, name):
		## name has-a object
		self.name = name
	
		##person has-a pet of some kind
		#That makes sure that the self.pet attribute of that class is set to a default of None.
		self.pet = None
	
##Employee is-a Class
class Employee(Person):

	def __init__(self, name, salary):
		##empleye has-a object
		super(Employee, self).__init__(name)
		#salary has-a object
		self.salary = salary
	
#fish is-a class
class Fish(object):
	pass
	
## Salmon is-a class
class Salmon(Fish):
	pass
	
##halibut has-a object
class Halibut(Fish):
	pass
	
	
##rover is-a DOF
rover = Dog ("Rover")

## Satan is-a CAT
satan = Cat("Satan")

##Mery is-a Person
mary = Person("Mery")

##satan has-a mery pet
mary.pet = satan

## frank is-a employee
frank = Employee("Frank", 120000)

#frank has-a pet rover
frank.per = rover

##fipper is-a fish
flipper = Fish()

## crouse has-a salmon
coruse = Salmon()

## harry has-a Halibut
harry = Halibut()

print "Executed"