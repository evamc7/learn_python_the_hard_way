print "You enter a dark room with two doors. Do you go through door #1 door or door #2?"

#we created a variable and the user answer
door = raw_input("> ")

# depending de answer print une thing or other
if door == "1":
	print "There's a gaint bear here eating a cheese cake. what do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	
	#we created a variable inside the bucle whit other answer in relation with before question
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off. Good job."
	elif bear == "2":
		print "The bear eats your legs  off. Good job."
	else: 
		print "Well, doing %s probably better. Bear runs away." % bear
		
#this is the other posibilty answer
elif door == "2":
	print "You stare into the endless abyss at Cthulhu'retina."
	print "1. Blueberries."
	print "2. Yellow jacket chlothespins."
	print "3. Understanding revolvers yelling melodies."
	
	#we created this varibale where the user answer your choise 
	hola = raw_input ("> ")
	
	if hola == "1" or hola == "2": 
		print "Your body survives powered by a mind of jello. Good job."
	else:
		print "The insanity rots you eyes into a pool of muck. Good job."


#and if the user don't chose any before posibilities print this sting.
else:
	print "You stumble around and fall on a knife and die. Good job."
	