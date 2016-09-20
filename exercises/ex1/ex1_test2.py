import unittest

from ex1 import SuperDuperManager


class TestCar(unittest.TestCase):
    """Sample unit tests for Exercise 1."""

    def setUp(self):
        self.manager = SuperDuperManager()
        self.manager.add_car('car1', 10)

    def test_move(self):
        self.manager.move_car('car1', 2, 3)
        postion = self.manager.get_car_position('car1')
        self.assertAlmostEqual(postion, (2, 3))

    def test_dispatch(self):
        self.manager.add_car('car2', 100)
        self.manager.add_car('car3', 100)
        self.manager.add_car('car4', 100)
        self.manager.add_car('car5', 100)

        self.manager.move_car('car2', 4, 5)
        self.manager.move_car('car3', 1, 9)
        self.manager.move_car('car4', 10, 0)
        self.manager.move_car('car5', 11, 9)

        self.manager.dispatch(12, 9)

        for car in self.manager._cars:
            print(str(self.manager.get_car_position(car))+ car)




if __name__ == '__main__':
    unittest.main()
