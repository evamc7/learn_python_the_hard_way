class Music(object):

	def __init__(self, two):
		self.two = two
		
	def second_part(self):
		for line in self.two:
			print line
			
imagine_one = Music(["Imagine there's no Heaven",
				"It's easy if you try",
				"And no Hell below us",
				"Above us only sky"])
				
people_two = Music(["Imagine all the people",
				"Living for today",
				"Imagine there's no country",
				"It isn't hard to do"])
				
imagine_one.second_part()

people_two.second_part()


#remember (object); __init__ ; self 