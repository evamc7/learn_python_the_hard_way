from sys import argv
from os.path import exists


script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
# creem una variable amb el nom "in_file" y li diem que obri larxiu from_file
in_file = open(from_file)
#creem una variable "indata" y lo diem que llegeixi la variable "in_file"
indata = in_file.read()

# len() escribe la longitud de una cadena 
print "The input file is %d bytes long" % len(indata)

# li estem demenan si existix "to_file"
print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

# creem una variable "out_file" y li diem que obri el archiu "to_file" en mode write
out_file = open(to_file, 'w')
# li diem que escriqui a la variable "out_file" es a dir a l'arxiu "to_file" el que posa a la variable "indata" es a dir a l'arxiu in_file.read 
out_file.write(indata)

print "Alright, all done."

#tanquem els dos arxius
out_file.close()
in_file.close()