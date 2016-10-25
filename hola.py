class ISAAC(object):

	def hola(self):
		print "bajadpjsajda"
		
	def adeu(self):
		print "okey"
		

class EVA(ISAAC):
	
	pass
		
		
boy = ISAAC()
child = ISAAC()
grandpa = ISAAC()

girl = EVA()

boy.hola()
boy.adeu()
girl.hola()