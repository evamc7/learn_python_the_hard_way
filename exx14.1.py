from sys import argv

script, user_name, mision = argv
prompt = '>'

print "Hi %s, I'm the %s script" % (user_name, script)
print "Your mision es %s" % mision
print "Are you agree %s?" % user_name
agree = raw_input(prompt)

print "Any questions %s?" % user_name
questions = raw_input(prompt)

print "Perfect, let's go!"