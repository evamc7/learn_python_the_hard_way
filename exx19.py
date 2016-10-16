# aqui creamos la funcion  y lo que vamos a imprimir con ella
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	
# 4 posibles maneras de ejecutar la funcion

# 1. escribimos la funcion y entre parentesis el valor de cada variable de la funcion 
print "We can just give the fuction numbers directly:"
cheese_and_crackers(20, 30)

# le decimos que la funcion esta compuesta por amount_of_cheese y amount_of_crackers y les damos a estas un valor 
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# recreamos el valor de las variables a traves de sumas 
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# utilizamos variables creadas anteriormente con una suma.
print "and we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Esto muestra las diferentes maneras en que somos capaces de dar a nuestros cheese_and_crackers funcion de los valores que necesita para imprimirlos. Podemos darle numeros consecutivos. Podemos darle variables. Podemos darle matematicas. Incluso podemos combinar las matematicas y las variables