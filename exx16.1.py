from sys import argv

script, filename = argv

print "Please, complete and read %r." % filename
print "Later, save the file in your computer"
sunny = open(filename, 'w')

print "Please, answer the questions:"

print "What is your name?"
name = raw_input()

print "How old are you?"
old = raw_input()

print "Tell me something about you"
something = raw_input()

print "Perfect, you can Play!"

sunny.write(name)
sunny.write("\n")
sunny.write(old)
sunny.write("\n")
sunny.write(something)

print "Game out"
sunny.close()
