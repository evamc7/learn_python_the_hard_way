# -*- encoding: UTF-8 -*-

from sys import exit
from random import randint


class inicio(object):

	def Primera(self):
		print "En esta aventrua te vas a encontrar con peligrosas y fantasticas criaturas", 
		print "aquellas que moran en el bosque y aquellas que nadie sabe de donde vienen."
	
	
		
class landscape(object):

	def enter(self):
		print "te encuentras en un universo extraño", 
		print "donde nada de lo que conoces tiene sentido..."
	
	def start_landscape(self):
		self.enter()

class gold(object):
	
	def __init__(self, landscape_map):
		self.landscape_map = landscape_map
		
	def play(self):
		first_scene = self.landscape_map.open_place()
		last_scene = self.landscape_map.next_place('finished')
		
	while first_scene != last_scene:
		next_place_name = first_scene.enter()
		first_scene = self.landscape_map.next_place(next_place_name)
		
	last_scene.play()
	
		
class death(landscape):

	def enter(self):
		print "you dead, GAME OVER"
		
class forest(landscape):
	
	def enter(self):
		print "bienvenido al bosque tenebroso: te toca escoger"
		print "a que lugar del bosque quieres llegar, cuidado con el camino que escojas:"
	
		way = raw_input("> ")
		
		if way == "right":
			clover()
		elif way == "left":
			dark()
		
		
class clover(landscape):
	
	def enter(self):
		print "Acabas de adentrarte en el bosque tenebroso",
		print "has escojido un camino muy tranquilo",
		print "encontraras pocas criaturas malvadas",
		print "llegaras sano y salvo a tu destino, superando unos obstaculos."
		
		
		
class dark(landscape):
	
	def enter(self):
		print "curioso camino en el que te encuentras",
		print "te encontraras con sumos peligros",
		print "el mas peligroso un cambaformas si te cruzas con el",
		print "adentrarse es la perdicion"
		rango()

class rango(landscape):

	def enter(self):
		print "PUUUUUUUUUUUUUM",
		print "un golpe te a dejado en el suelo \nahora viene de abajo \n\tno sabes que es \nno lo puedes identificar"
		print "el cambiaformas te ha encontrado, solo llevas cerillas y agua"
		print "que utilizaras para luchar?"
		
		utilizar = raw_input("> ")
		
		if utilizar == "cerillas":	
			result = find_a_way()
			result.enter()
		elif utilizar == "agua":
			death()
			
class find_a_way(landscape):

	def enter(self):
		print "GENIAL! Has conseguido superar todos los obstaculos del bosqe tenebroso"
		print "en el residen malvadas criaturas marginadas por siglos"
		print "aqui descubirars el secreto de la inmortalidad"
		print "cuidado, saberlo podría arrebatarte la vida..."
	
class map(object):

	landscapes = {
		'forest' : forest(),
		'clover' : clover(),
		'dark' : dark(),
		'rango' : rango(),
		'find_a_way' : find_a_way(),
		'death' : death(),
	}

	def __init__(self, start_landscape):
		self.start_landscape = start_landscape
		
	def next_place(self, landscape_place):
		place = map.landscapes.get(landscape_place)
		return place 
	def open_place(self):
		return self.next_place(self.start_landscape)
		
		
		
inicio()