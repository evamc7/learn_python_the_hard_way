# -*- coding: utf-8 -*- 

# aqui creamos las equivalencias IMPORTANTE no olvidar (_) ni ('') porque dara error 
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'blue'
my_teeth = 'white'
my_hair = 'Brown'

# debemos indicar con %s o %d que vamos a poner una equivalencia y marcamos cual a traves de % despues de la string
print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
# si ponemos mas de una dentro de la misma string, lo marcaremos despues entre parentesis y separado por coma
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s dependin on the coffee." % my_teeth

# this line is tricky, try to get exactlu rigth
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)
