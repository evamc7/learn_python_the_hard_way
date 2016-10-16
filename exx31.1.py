print """Hello to the HALLOWEEN AWARDS
		 we are so exited to present the best \nterrified \ncustomes \nof \tHALLOWEEN COMPETITION"""
		
print "Do you want to participate? and WIN?"

answer = raw_input("> ")

if answer == "yes" :
	print "COOL! Do you have +18?"
	
elif answer == "no":
	print "OH! we are very sad! why?"

age = raw_input("> ")

if age == "yes":
	print "PERFECT! you can star to find a most terrified custom! uuuuuhhh"
	
elif age == "no":
	print "OH SORRY! you can't participate in this competition"
	
print "Do you want come to a wiched house?"

house = raw_input("> ")

if house == "yes" :
	print "COOL! your prefer than competition? yes or no"
			
	competition = raw_input("> ")
			
	if competition == "yes":
		print "We have a house perfect for you!"
			
	elif competition == "no":
		print "Perfect, we wait in out best HALLOWEEN COMPETITION"
			
	else:
		print "What do you prefer for HALLOWEEN NIGHT?"

if house == "no":
	print "Perfect, we wait in out best HALLOWEEN COMPETITION"