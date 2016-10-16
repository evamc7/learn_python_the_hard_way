#we are doing our own math fuctions 
def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b
# en return decimos volver a + b, nustra funcion tiene dos argumentos
def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
	
def divide (a, b):
	print "Dividing %d / %d" % (a, b)
	return a / b
	
#aqui hacemos una cadena y damos valor a las funciones antes creadas que se van a imprimir aquí
print "Let's do some math with just fuctions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

#aqui lo que hace es imprimir en age ls funciones con el valor que les ha dado 
print "Age: %d, Height: %d, weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print "Thats become: ", what, "Can you do it by hand?"