# -*- coding: utf-8 -*-

# el %r fara que les cadenes que fiquem surtin tal qual, forma real escrita entre cometes
formatter = "%r %r %r %r"

#posem 4 elements ja que la cadena es de 4 %r, si ens faltes un sortiria %r
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)

#aquí ens sortira el valor real de formatter es a dir %r x4 
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
	"That you could type up rigth.",
# en aquet cas quan ho imprimim surten "" perque tenim el didn't i si nomes hi hages una ' podria ser confos 	
	"But it didn't sing.",
	"So I said goodnight.",
)



# error - no oblidarse les comes 