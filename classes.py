'''
#This program allows for updating an attributes value with a method
class Restaurant():

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0


	def describe_restaurant(self):
		print('\n' + self.restaurant_name.title() + ', ' + self.cuisine_type.title())

	def open_restaurant(self):
		print('The restaurant ' + self.restaurant_name.title() + ' is open')

	def print_number_served(self):
		print('Number of customers served at this restaurant: ' + str(self.number_served))

	def increment_number_served(self, number):
		self.number_served += number
		print('Number of customers served at this restaurant: ' + str(self.number_served))

restaurant = Restaurant('cafe chennai', 'indian')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.print_number_served()
restaurant.increment_number_served(100)

restaurant2 = Restaurant('italian pines', 'italian')
restaurant2.describe_restaurant()
restaurant2.open_restaurant()
restaurant2.print_number_served()
restaurant2.increment_number_served(200)
'''

'''
#inheritance of the Restaurant class
class Restaurant():

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0


	def describe_restaurant(self):
		print('\n' + self.restaurant_name.title() + ', ' + self.cuisine_type.title())

	def open_restaurant(self):
		print('The restaurant ' + self.restaurant_name.title() + ' is open')

	def print_number_served(self):
		print('Number of customers served at this restaurant: ' + str(self.number_served))

	def increment_number_served(self, number):
		self.number_served += number
		print('Number of customers served at this restaurant: ' + str(self.number_served))

#######Child class##################
class Cafe(Restaurant): #the child class, inheriting Restaurant
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type) #inheriting the parent super class
		self.coffee_maker_num = 2

	def number_coffee_machines(self):
		print('Number of coffe machines at cafe: ' + str(self.coffee_maker_num))

	def open_restaurant(self):  #overriding the open_restaurant method from the parent class
		print('The cafe, ' + self.restaurant_name.title() + ', is open')


my_cafe = Cafe('Cafe Roma', 'Italian American')
my_cafe.describe_restaurant()
my_cafe.number_coffee_machines()
my_cafe.open_restaurant()

'''

#Ice cream stand

class Restaurant():

	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		print('\n' + self.restaurant_name.title() + ', ' + self.cuisine_type.title())

	def open_restaurant(self):
		print('The restaurant ' + self.restaurant_name.title() + ' is open')

	def print_number_served(self):
		print('Number of customers served at this restaurant: ' + str(self.number_served))

	def increment_number_served(self, number):
		self.number_served += number
		print('Number of customers served at this restaurant: ' + str(self.number_served))

class IceCreamStand(Restaurant):
	def __init__(self, restaurant_name, cuisine_type):
		super().__init__(restaurant_name, cuisine_type) #inheriting the parent super class
		self.flavors = ['Chocolate','Vanilla','Strawberry']

	def print_flavors(self):
		print('\nIce cream flavors: \n')
		for flavor in self.flavors:
			print(flavor)

ice_cream_stand = IceCreamStand('','')
ice_cream_stand.print_flavors()
