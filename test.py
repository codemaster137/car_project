import unittest
from super_car import CarManager

class TestCar(unittest.TestCase):

	def setUp(self):
		self.manager = CarManager()
		self.manager.add_car('car1', 2)
		self.manager.add_car('car2', 10)
		self.manager.add_car('car3', 20)

		# New added cars
		self.manager.add_car('car4', 15)
		self.manager.add_car('car5', 10)
		self.manager.add_car('car6', 8)
		self.manager.add_car('car7', 7)
		self.manager.add_car('car8', 12)
		self.manager.add_car('car9', 8)
		self.manager.add_car('car10', 10)
		self.manager.add_car('car11', 10)
		self.manager.add_car('car12', 9)



	def test_initial_fuel(self):
		self.assertEqual(self.manager.get_car_fuel('car1'), 2)
		self.assertEqual(self.manager.get_car_fuel('car2'), 10)
		self.assertEqual(self.manager.get_car_fuel('car3'), 20)

		# Fuel test for new added cars
		self.assertEqual(self.manager.get_car_fuel('car4'), 15)
		self.assertEqual(self.manager.get_car_fuel('car5'), 10)
		self.assertEqual(self.manager.get_car_fuel('car6'), 8)


	def test_initial_pos(self):
		pos = self.manager.get_car_position('car1')
		self.assertEqual(pos, (0, 0))

		# Testing initial position for new added cars
		pos1 = self.manager.get_car_position('car4')
		self.assertEqual(pos1, (0, 0))
		pos2 = self.manager.get_car_position('car5')
		self.assertEqual(pos2, (0, 0))
		pos3 = self.manager.get_car_position('car6')
		self.assertEqual(pos3, (0, 0))


	def test_move_simple(self):
		self.manager.move_car('car2', 2, 3)
		pos = self.manager.get_car_position('car2')
		self.assertEqual(pos, (2, 3))
		self.assertEqual(self.manager.get_car_fuel('car2'), 5)

		# Test 1
		self.manager.move_car('car4', 6, 4)
		pos1 = self.manager.get_car_position('car4')
		self.assertEqual(pos1, (6, 4))
		self.assertEqual(self.manager.get_car_fuel('car4'), 5)

		self.manager.move_car('car4', 2, 3)
		pos2 = self.manager.get_car_position('car4')
		self.assertEqual(pos2, (8, 7))
		self.assertEqual(self.manager.get_car_fuel('car4'), 0)

		# Test 2
		self.manager.move_car('car5', 2, 5)
		self.assertEqual(self.manager.get_car_fuel('car5'), 3)
		self.assertEqual(self.manager.get_car_position('car5'), (2, 5))
		
		self.manager.move_car('car5', -2, 1)
		self.assertEqual(self.manager.get_car_fuel('car5'), 0)
		self.assertEqual(self.manager.get_car_position('car5'), (0, 6))

		# Test 3
		self.manager.move_car('car12', 2, 3)
		self.assertEqual(self.manager.get_car_fuel('car12'), 4)
		self.assertEqual(self.manager.get_car_position('car12'), (2, 3))
		
		self.manager.move_car('car12', -2, 1)
		self.assertEqual(self.manager.get_car_fuel('car12'), 1)
		self.assertEqual(self.manager.get_car_position('car12'), (0, 4))

		self.manager.display_cars()



	def test_move_just_enough(self):
		self.manager.move_car('car1', 0, 2)
		pos = self.manager.get_car_position('car1')
		self.assertEqual(pos, (0, 2))
		self.assertEqual(self.manager.get_car_fuel('car1'), 0)

		# Test 1
		self.manager.move_car('car6', 2, 2)
		posTemp = self.manager.get_car_position('car6')
		self.assertEqual(posTemp, (2, 2))
		self.assertEqual(self.manager.get_car_fuel('car6'), 4)

		self.manager.move_car('car6', 1, 1)
		self.assertEqual(self.manager.get_car_position('car6'), (3, 3))
		self.assertEqual(self.manager.get_car_fuel('car6'), 2)

		self.manager.move_car('car6', 0, -2)
		self.assertEqual(self.manager.get_car_position('car6'), (3, 1))


		# Test 2
		self.manager.move_car('car7', 2, 0)
		posTemp = self.manager.get_car_position('car7')
		self.assertEqual(posTemp, (2, 0))
		self.assertEqual(self.manager.get_car_fuel('car7'), 5)

		self.manager.move_car('car7', 4, 1)
		posTemp = self.manager.get_car_position('car7')
		self.assertEqual(posTemp, (6, 1))
		self.assertEqual(self.manager.get_car_fuel('car7'), 0)



		# Test 3
		self.manager.move_car('car8', 2, 0)
		posTemp = self.manager.get_car_position('car8')
		self.assertEqual(posTemp, (2, 0))
		self.assertEqual(self.manager.get_car_fuel('car8'), 10)

		self.manager.move_car('car8', -3, -1)
		posTemp = self.manager.get_car_position('car8')
		self.assertEqual(posTemp, (-1, -1))
		self.assertEqual(self.manager.get_car_fuel('car8'), 6)

		self.manager.move_car('car8', 3, 3)
		posTemp = self.manager.get_car_position('car8')
		self.assertEqual(posTemp, (2, 2))
		self.assertEqual(self.manager.get_car_fuel('car8'), 0)

		self.manager.display_cars()

	def test_move_not_enough(self):
		self.manager.move_car('car1', 3, 5)
		pos = self.manager.get_car_position('car1')
		self.assertEqual(pos, (0, 0))
		self.assertEqual(self.manager.get_car_fuel('car1'), 2)

		# Test 1
		self.manager.move_car('car9', 1, 1)
		self.manager.move_car('car9', 2, 2)
		self.manager.move_car('car9', 3, 3)
		self.assertEqual(self.manager.get_car_position('car9'), (3, 3))
		self.assertEqual(self.manager.get_car_fuel('car9'), 2)

		# Test 2
		self.manager.move_car('car10', 3, 3)
		self.manager.move_car('car10', -1, -1)
		self.manager.move_car('car10', -2, -2)
		self.assertEqual(self.manager.get_car_position('car10'), (2, 2))
		self.assertEqual(self.manager.get_car_fuel('car10'), 2)

		# Test 3
		self.manager.move_car('car11', 6, -9)
		self.assertEqual(self.manager.get_car_position('car11'), (0, 0))
		self.assertEqual(self.manager.get_car_fuel('car11'), 10)

		self.manager.display_cars()	


		
if __name__ == '__main__':
	unittest.main()
