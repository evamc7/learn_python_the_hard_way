print "How old are you?"
age = raw_input (22)
print "How tall are you?"
height = raw_input (70)
print "How much do you weigh?"
weight = raw_input (53)
# en este caso he rellenado yo los parentes de raw_input, que seria lo que tendria que rellenar el usuario con los datos que deben aparecer 
print "So, you're %r old, %r tall and %r heavy." % (
	age,height, weight)
	
	
#raw_input sirve a la hora de crear una sentencia que solicite datos, La función input está destinada a la entrada de cualquier caracter, siempre y cuando este mismo sea notificado como es. Es decir, si ingresamos números, simplemente sera así lo que nos dirá Python
#normalmente se usa para que el usuario rellene el campo con los datos que deben salir 