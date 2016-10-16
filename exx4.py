# creamos equivalencias numericas a plabras
# ponemos 4.0 pq es un floating point 
cars = 100
space_in_a_car = 4.0
drivers = 30
passangers = 90
cars_not_driven = cars - drivers
cars_driven = drivers 
carpool_capacity = cars_driven * space_in_a_car
average_passangers_per_car = passangers /cars_driven


# la equivalencia que queremos mostrar la ponemos fuera de los parentesis para que se ejecute 
print "There are", cars, "cars avaiable."
print "There are only", drivers, "drivers avaiable."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passangers, "to carpool today."
print "We need to put about", average_passangers_per_car, "in each car."
