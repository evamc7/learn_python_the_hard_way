from sys import argv
#it's a argument variable
script, filename = argv
#It's a new order to opened
txt = open(filename)
#print a missage
print "Here's your file %r:" %filename
#read commands whit no parametres
print txt.read()

# the user give the name and read commands whit no parametres again
print "Tell me your name:"
name = raw_input("> ")

txt_again = open (name)

print txt_again.read()