# escribimos cadenas que queremos que salgan representadas, es decir asociamos una cadena a una variable 

# el %d asigna un digito a la cadena y la cadena se asigna a la vaiable x
x = "There are %d types of people." % 10
#la cadena "binary" se asocia a la variable binary
binary = "binary"
# la cadena "don't" se asocia a la variable do_not 
do_not = "don't"
# el %s asocian variables a la cadena y toda la cadena se asocia a la vaiable y 
y = "Those who know %s and those who %s." % (binary, do_not)

# escibimos las cadenas que queremos que se impriman, al ser equivlaqencias no utlizamos ""
print x
print y

#imprimimos una cadena a la que le asociamos la variable x anteriormente asociada a una cadena 
print "I said: %r." % x
#imprimimos una cadena a la que ajuntamos la variable y
print "I also said: '%s'." % y 

#cramos variables 
hiliarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#como en joke_evaluation tenemos un %r a la hora de imprimirlo tenemos que identificar con % que queremos que sea
print joke_evaluation % hiliarious

w = "This is the left side of..."
e = "a string whit a right side."

#sumamos las dos cadenas, 
print w, e
print w + e
