import matplotlib.pyplot as plt
from adjustText import adjust_text

class CarManager:
	"""A class responsible for keeping track of all cars in the system.
	"""

	# === Private Attributes ===
	# @type _cars: dict[str, Car]
	# A map of unique string identifiers to the corresponding cars.

	def __init__(self):
		""" Create a new CarManager.

		Initially there are no cars in the system.

		@type self: CarManager
		@rtype: None
		
		"""

		self._cars = {}

	def add_car(self, id, fuel):
		"""Add a new car to the system.

		The new car is identified by the string <id>, and has the initial amount
		of fuel <fuel>.

		Do nothing if there is already a car with the given id.

		@type self: CarManager
		@type id: str
		@type fuel: int
		@rtype: None
		"""

		#Check to make sure the identifier isn't already used.
		if id not in self._cars:
			self._cars[id] = Car(fuel)

	def move_car(self, id, new_x, new_y):
		"""Move a car in the system.

		The car called <id> should be moved to position (<new_x>, <new_y>).

		@type self: CarManager
		@type id: str
		@type new_x: int
		@type new_y: int
		@rtype: None
		"""

		if id in self._cars:
			if (abs(new_x) + abs(new_y)) <= self._cars[id].fuel:
				self._cars[id].position = (self._cars[id].position[0] + new_x, self._cars[id].position[1] + new_y)
				self._cars[id].fuel -= (abs(new_x) + abs(new_y))

	def get_car_position(self, id):
		"""Return the position of the car <id> in the system.

		Return a tuple of the (x, y) position of the car.

		@type self: CarManager
		@type id: str
		@rtype: (int, int)
		"""

		if id in self._cars:
			return self._cars[id].position

	def get_car_fuel(self, id):
		"""Return the amounf of fuel of the car <id> in the system

		@type self: CarManager
		@type id: str
		@rtype: int
		"""

		if id in self._cars:
			return self._cars[id].fuel

	def display_cars(self):
		"""
		Display the position of all the cars in the system.

		Return a matplotlib scatter plot with location of all cars
		"""

		positions = []
		car_names = []
		for car in self._cars:
			car_names.append(car)

		for id in self._cars:
			positions.append(self._cars[id].position)

		x, y = zip(*positions)

		print(x)
		print(y)
		plt.grid(linestyle = '--', linewidth = 0.5)
		plt.scatter(x, y, s = 100,)
		plt.xlabel('Horizontal Position')
		plt.ylabel('Vertical Position')
		plt.title('Car Locations')

		for i, label in enumerate(car_names):
			plt.annotate(label, (x[i], y[i] + 0.2), fontsize = 10)
		plt.xticks([i for i in range(min(x), max(x) + 1)])
		plt.yticks([i for i in range(min(y), max(y) + 2)])
		#adjust_text(car_names, only_move={'points':'y', 'texts':'y'}, arrowprops=dict(arrowstyle="->", color='r', lw=0.5))
		plt.show()




class Car:
	"""A car in the Super system.

	Fill in the public or private attributes for this class!
	"""

	def __init__(self, fuel):
		"""Create a new car.

		@type self: Car
		@type position: (int, int)
		@type fuel: int
		@rtype: None
		"""

		self.fuel = fuel
		self.position = (0, 0)



	