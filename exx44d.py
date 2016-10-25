#create parent class
class parent(object):

	#definimos una funcion
	def override(self):
		print "PARENT override()"
	
	#definimos una funcion
	def implicit(self):
		print "PARENT implicit()"
	
	#definimos una funcion
	def altered(self):
		print "PARENT altered()"

#create child class	y decimos que heredata de parent	
class child(parent):

	#definimos una funcion que anulara la funcion override de parent
	def override(self):
		print "CHILD override()"
		
	# implicit la heredaremos de parent 
	
	#definimos una funcion que primero anulara la heredada y despues con super la volvera a llamar
	def altered(self):
		print "CHILD, BEFORE PARENT aletered()"
		super(child, self).altered()
		print "CHILD, AFTER PARENT altered()"

#variables		
dad = parent()
son = child()


dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
