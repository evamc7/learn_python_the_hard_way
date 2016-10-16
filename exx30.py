people = 15
cars = 40
trucks = 40

#here says if cars is bigger than people print this sting
if cars > people:
	print "We should take the cars"
#elif: si no se cumple la anterior pero si esta se imprime esta string
elif cars < people:
	print "We should not take the cars"
#si no es ninguna de las anteriores impirmir esta 
else:
	print "We can't decide."
	
if trucks > cars:
	print "That's too many trucks."
elif trucks < cars:
	print "maybe we could take the trucks."
else:
	print "We still can't decide"
	
if people > trucks:
	print "Alrigth, let's just take a trucks."
else:
	print "Fine, let's stay home then."
	
	
#con elif se hacen bucles y se empieza por if y aacaba por else
# if more one elif is true python only will run the first one 