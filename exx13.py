from sys import argv
# las referencias a que son script first second and third se indican en el powershell todo seguido y si aqui tenemos indicadas tres variables y en el power solo indicamos 2 nos dara error
script, first, second, third = argv

# en las values (script, first, second, third) saldran los valores que nosotros indiquemos en power shell
print "The scrip is called:", script
print "Your first varibale is:", first
print "Your second variable is:", second
print "your third variable is:", third


#IMPORANT! a la hora de imprimirlo en power shell se tiene que especificar las values/variables ej: python exx13.py first 2nd 3rd
color = raw_input ("What is your color? ")
film = raw_input ("What is your prefer film? ")

print "So you're prefer color is %r ans you're prefer film is %r." % (color, film)