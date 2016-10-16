from sys import exit

def start():
	print "Welcome to the most terrified Mansion"
	print "This mansion was builgin for gost in 1560th"
	print "The legend tells that whoever enters it must face many dangeros"
	print "Are you ready to come in?"
	
	ready = raw_input("> ")
	
	if ready == "yes":
		your_brave()
		
	elif ready == "no":
		print "The ghosts and witch are angry with you", dead()
	
	else:
		print scared(), "Are you ready now?"
		
def your_brave():
	print "WELL WELL WELL. Are you very BRAVE  for daring to enter"
	print """First I must warn that once you are inside...
	you never get out...
	if you don't find the withc and you don't solve his riddle.
	But the riddle is not ver difficult, your problem will be...
	\t\n FIND THE WITCH IN THIS DARNGEROS HOUSE UHAHAHAHAHAHAHHA"""
	print "Choise the key and enters to he house"
	
	key = raw_input("> ")
	
	if key == "1":
		print "Well well well... good choise, you have choisen key attic"
		print "Attic hides a lot of secrets and dangers, in there live a lot of lost ghost"
		print "You dare to open the door?"
		
		door = raw_input("> ")
		
		if door == "yes":
			first_attic()
			
		elif door == "no":
			your_brave()
			
	elif key == "2":
		print "Well well well... dangerous choise, you have choisen key Kitchen.."
		print "In the kithcen the objects fly alone... walk whit mind"
		print "Are you already in the kitchen?"
		
		kitchen = raw_input("> ")
		
		if kitchen == "yes":
			print "Good, find clues leading to the witch"
			print "you have it?"
			
			have = raw_input(">")
			
			if have == "yes":
				print "OMG! REALLY? you can go to find a witch, she is waiting for you"
				witch()
			elif have == "no":
				print "Sorry! You never get out hear"
				dead()
		else:
			dead()
				
def	first_attic():
		print "There you need choise the door on the left or on the right"
		
		door = raw_input("> ")
		
		if door == "left":
			print "Good choise, inside there is a map whit tracks to finde a witch... careful, the ghosts can play whith you tell you a lies"
			print "Have you been able to decipher the map?"
			
			map = raw_input("> ")
			
			if map == "yes":
				print "OMG! REALLY? you can go to find a witch, she is waiting for you"
				witch()
			
			elif map == "no":
				print "Sorry!", dead()
			
def	dead():
		print "You have killed, you are now a ghost trapped in the house"
		exit(0)
			
def scared ():
	print "No problem it's normal, but it's your choise, entire or dead"
		
	choise = raw_input("> ")
		
	if choise == "entire":
		your_brave()
		
	elif choise == "dead":
		dead()
		
def witch():
	print "Well! you're the one who found me!!"
	print "Are you ready for save or dead?"
	print "Come on! How old I am"
		
	old = 150
	
	if old == 150: 
		print "NOOOOO YOU'RE RIGHT YOU ARE DE WIN, YOU CAN GO OUT OF MY HOUSE OR YOU CAN STAY HERE FOR EVER, YOU CHOISE!"
		print "CONGRATULATIONS!!!!"
	elif old > 150:
		dead()
			
start()