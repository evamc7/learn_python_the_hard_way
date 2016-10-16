# its a argument variable
from sys import argv
# donem nom a les variables
script, filename = argv

#print a few of string 
## %r es per completar amb la informacio que ha donar l'usuari 
print "We're going to erase %r." %filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want thaht, hit RETURN."

# print ? and the user answers
raw_input("?")

# print a string 
print "Opening the file..."
# creem una variable que es diu patata i diuem que obri un archiu on es pugui escriure ("w") - write
patata = open(filename, 'w')

print "Truncating the file. Goodbye!"
# diem que es borri tot el que hi ha dins de la variable patata 
patata.truncate()

print "Now I'm going to ask you for three lines."
# informem de que tres lines omplira la informacio l'usuari i ordenem que simprimeixin i omplin, es a dir les creem cadenes
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

#fem que les cadenes que s'han creat anteriorment s'escriguin a l'arxiu // amb \n fem backslash and new line
patata.write(line1)
patata.write("\n")
patata.write(line2)
patata.write("\n")
patata.write(line3)
patata.write("\n")

print "and finally, we close it."
patata.close()
# close the file
