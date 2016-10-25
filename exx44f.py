#create a other class
class other(object):

	
	def override(self):
		print "OTHER override()"
		
	def implicit(self):
		print "OTHER implicit()"
		
	def altered(self):
		print "OTHER altered()"
		
#create a child class
class child(object):
	
	
	#definimos una funcion y llamamos a other y le damos el nombre de self.other para llamarlo
	def __init__(self):
		self.other = other()
		
		
	#definimos una funcion y llamamos a la funcion implicit de other
	def implicit(self):
		self.other.implicit()
	
	def override(self):
		print "child override()"
		
	def altered(self):
		print "CHILD, BEDORE OTHER altered()"
		#llamamos a la funcion altered de other 
		self.other.altered()
		print "Child, after other altered()"
		
son = child() #instancia 1
girl = child() # instancia 2





son.implicit()
son.override()
son.altered()