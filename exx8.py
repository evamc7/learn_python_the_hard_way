# el %r hara que salga tan cual la forma real puesta entre comillas 
formatter = "%r %r %r %r"
#hay que poner 4 elementos porque en la variable hemos puesto 4 en la cadena, sino nos saldria %r
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
	)
	
	
	# errores: olvidar la coma final en la linea 10 -- da error 