"""CSC148 Exercise 1: Basic Object-Oriented Programming

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains sample tests for Exercise 1.

Warning: This is an extremely incomplete set of tests!
Add your own to practice writing tests and to be confident your code is correct.

For more information on hypothesis (one of the testing libraries we're using),
please see
<http://www.teach.cs.toronto.edu/~csc148h/fall/software/hypothesis.html>.

Note: this file is for support purposes only, and is not part of your
submission.
"""
import unittest
from hypothesis import given
from hypothesis.strategies import integers, text

from ex1 import SuperDuperManager


class TestCar(unittest.TestCase):
    """Sample unit tests for Exercise 1."""

    def setUp(self):
        """This is a special method that's called at the beginning of each test.

        It is used to create a SuperDuperManager object with three cars;
        these will be the cars used in subsequent tests.
        """
        self.manager = SuperDuperManager()
        self.manager.add_car('car1', 2)
        self.manager.add_car('car2', 10)
        self.manager.add_car('car3', 20)

    def test_move_simple(self):
        self.manager.move_car('car2', 2, 3)
        pos = self.manager.get_car_position('car2')
        self.assertEqual(pos, (2, 3))
        self.assertEqual(self.manager.get_car_fuel('car2'), 5)

    def test_move_not_enough(self):
        self.manager.move_car('car1', 3, 5)
        pos = self.manager.get_car_position('car1')
        self.assertEqual(pos, (0, 0))
        self.assertEqual(self.manager.get_car_fuel('car1'), 2)

    def test_move_negative(self):
        self.manager.move_car('car3', -2, -3)
        pos = self.manager.get_car_position('car3')
        self.assertEqual(pos, (-2, -3))
        self.assertEqual(self.manager.get_car_fuel('car3'), 15)


class TestCarWithHypothesis(unittest.TestCase):
    """Sample hypothesis tests for Exercise 1."""
    @given(text(), integers(min_value=0))
    def test_add_car_returns_none(self, id_, fuel):
        """Check that add_car always returns None."""
        manager = SuperDuperManager()
        # return_value = manager.add_car(id_, fuel)
        # self.assertIsNone(return_value)

    @given(text(), integers(min_value=0))
    def test_car_has_initial_fuel_set(self, id_, fuel):
        """Check that a car's initial fuel is set properly.
        """
        manager = SuperDuperManager()
        manager.add_car(id_, fuel)                         # Create new car
        self.assertEqual(fuel, manager.get_car_fuel(id_))  # Check new car fuel

    @given(text(), integers(min_value=0))
    def test_car_has_initial_fuel_set(self, id_, fuel):
        manager = SuperDuperManager()
        manager.add_car(id_, fuel)
        self.assertEqual((0, 0), manager.get_car_position(id_))


if __name__ == '__main__':
    unittest.main()
