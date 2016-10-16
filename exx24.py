print "Let's practice everything."
#solo queda reflejada una \ cuando hay \\
print 'You\'d need to know \'bout escapes whit \\ that do \n newlines and \t tabs.'

# \tab \n backslash new linw
poem = """
\tThe lovely world
whit logic so firmly planted
cannot discern \n the need of love
nor comprehend passion form intuition
and requieres an explanation
\n\t\twhere there is none.
"""


print "--------------"
print poem
print "--------------"

#creamos una variable 
five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

#creamos una formula 
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
	
	
start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "Whit a starting point of: %d" % start_point
print "WE'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)


start_point = start_point / 10

#arriba hemos creado la cadena secret_formula(start_point) que hacen referencia a beans, jars, carates y (1000) por start_point de la formula que hemos creado , que son los valores que imprimimos en esta string 
print "We can also do tht this way:"
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

#error cuidado con los espacios 