# \t es com fer un tap (--> la flechita de espacio)
tabby_cat = "\tI'm tabbed in."
# \n backslash new line ( el que hi ha despres de la \n es posa a l linea de sota)
persian_cat = "I'm split\non a line."
# es posen dos \\ perque surti 1 \ per posar casracters especials dins duna cadena 
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat




while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" %i,
		