import unittest

from ex1 import SuperDuperManager


class TestCar(unittest.TestCase):
    """Sample unit tests for Exercise 1."""

    def setUp(self):
       self.manager = SuperDuperManager()
       self.manager.add_car('car1', 10)

    def test_move(self):
        self.manager.move_car('car1',2,3)
        postion = self.manager.get_car_position('car1')
        self.assertAlmostEqual(postion, (2,3))


if __name__ == '__main__':
    unittest.main()
