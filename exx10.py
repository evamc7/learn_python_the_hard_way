# \t se utiliza para crear un espacio un tap (--> la flechita de espacio)
tabby_cat = "\tI'm tabbed in."
# \n backslash new line, creamos una nueva linea
persian_cat = "I'm split\non a line."
# se escriben 2 \\ para que salga reflejada una, es un caracter especial dentro de una cadena 
backslash_cat = "I'm \\ a \\ cat."

# recordamos que las """ es para poner comentarios en mas de una linea, y el \t es para hacer un tap y  el asterisco queda refelejado
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
# en la linea 13 vemos un \n backslash new line para que la contiuacion sea en una nueva linea y el \t para hacer un tap (espacio)
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

while True:
	for i in ["/","-","|","\\","|"]:
		print "%s\r" %i,
		