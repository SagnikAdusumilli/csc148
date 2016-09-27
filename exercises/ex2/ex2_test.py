"""CSC148 Exercise 2: Inheritance and Introduction to Stacks

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains sample tests for Exercise 2.

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

from ex2 import SuperDuperManager, reverse_top_two
from obfuscated_stack import Stack


class SuperDuperManagerTest(unittest.TestCase):

    @given(text(min_size=1), integers(min_value=1))
    def test_new_car_attributes(self, id_, fuel):
        manager = SuperDuperManager()
        manager.add_vehicle('Car', id_, fuel)
        self.assertEqual(manager.get_vehicle_fuel(id_), fuel)
        self.assertEqual(manager.get_vehicle_position(id_), (0, 0))

    @given(text(min_size=1), integers(min_value=1))
    def test_new_helicopter_attributes(self, id_, fuel):
        manager = SuperDuperManager()
        manager.add_vehicle('Helicopter', id_, fuel)
        self.assertEqual(manager.get_vehicle_fuel(id_), fuel)
        self.assertEqual(manager.get_vehicle_position(id_), (3, 5))

    @given(text(min_size=1), integers(min_value=1))
    def test_new_carpet_attributes(self, id_, fuel):
        manager = SuperDuperManager()
        manager.add_vehicle('UnreliableMagicCarpet', id_, fuel)
        self.assertEqual(manager.get_vehicle_fuel(id_), fuel)
        self.assertLessEqual(abs(manager.get_vehicle_position(id_)[0]), 10)
        self.assertLessEqual(abs(manager.get_vehicle_position(id_)[1]), 10)


class ReverseTopTwoTest(unittest.TestCase):
    def test_simple_reverse_top_two(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        reverse_top_two(stack)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(stack.pop(), 2)
        self.assertTrue(stack.is_empty())


if __name__ == '__main__':
    unittest.main()
