from sys import argv

script, filename = argv
#es una nueva orden de apertura
txt = open(filename)

# aqui decimos que imprima un mensaje
print "Here's your file %r:" %filename
#aqui hacemos una funcion txt para leer  - orden de lectura sin parametros
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt.again.read()