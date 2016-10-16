# la coma serveix per seperar lines, es a dir que les frases apareixin el diferents lines 
print "How old are you?",
#raw_input, serveix per a que lusuari ompli la informacio que falta 
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)
	