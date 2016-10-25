class Parent(object):

	def override(self):
		print "PARENT override()"
		
class Child(Parent):
	
	def override(self):
		print "CHILD override()"
		
dad = Parent()
son = Child()

dad.override()
son.override()


class JESUS(object):

	def informatic(self):
		print "Hello I am Gilabertus"
		
class EVA(JESUS):
	
	pass
	
one = JESUS()
two = EVA()

one.informatic()
two.informatic()


class LAW(object):
	
	def codi(self):
		print "you need study this"
		
class LAWER (LAW):

	def codi(self):
		print "You need knew the law rules"
		
constitution = LAW()
judge = LAWER()

constitution.codi()
judge.codi()