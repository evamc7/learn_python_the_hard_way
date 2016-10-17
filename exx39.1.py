communities = {
	'Catalonia': 'CAT',
	'Andalucia': 'AND',
	'Madrid': 'MAD',
	'PaisVasco': 'VAS',
	'Galicia': 'GAL'
	}
	
cities = {
	'CAT': 'Barcelona',
	'AND': 'Almeria',
	'MAS': 'Madrid',
	'PaisVaso': 'Bilbao'
	}
	
cities['GAL'] = 'Lugo'

print '-' * 15
print "CAT communty has: ", cities['CAT']

print '-' * 5
print "Andalucioa has: ", cities[communities['Andalucia']]

print '-' * 5
for communities, abbrev in communities.items():
	print "%s is abbreviated %s" % (communities, abbrev)


print '-' * 15