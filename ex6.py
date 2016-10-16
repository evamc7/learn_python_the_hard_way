#el %d posa un digit a la cadena y tota la cadena s'asigna a x
x = "There are %d types of people." % 10
# la cadena s'associa a una variable ( binary es la variable y "binary" es la cadena
binary = "binary"
# la cadena "don't" s'associa a la variable do_not
do_not = "don't"
# el %s fica una cadena "binary" dins d'una cadena dos cops en aquest cas 
y = "Those who know %s and those %s." % (binary, do_not)

# imprimim la cadena associada a la variable x de dalt
print x
#imprimim la cadena associada a la variable y de dalt
print y

# imprimim una string a cadena i afegim la cadena associada a la variable x tal qual esta (%r ho imprimeix tal qual esta)
print "I said: %r." % x
#imprimim una string i li afegim la cadena associada a la variable y se li diu que ho imprimeixi entre cometes
print "I also said: '%s'." % y 

# hem assignat a la variable hilarious false que es un valor BOOLEAN
hilarious = False
#assignem una cadena a una variable i posem la possibilitat de posar un string interpolation ( sortira entre cometes)
joke_evaluation = "Isn't that joke so funny?! %r"

# posem el % hilarious pq substitueixi el %r de la string de dalt
print joke_evaluation % hilarious 


w = "This is the left side of..."
e = "a string with a right side."

# s'ha de sumar perque s'ajuntin, si possesim una , no s'ajuntarien i no podriem modifcar/ fer operacions 
print w + e 
z = w + e
print z 