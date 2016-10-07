"""CSC148 Exercise 3: Stacks and a Chain of People

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains sample tests for Exercise 3.

Warning: This is an extremely incomplete set of tests!
Add your own to practice writing tests and to be confident your code is correct.

For more information on hypothesis (one of the testing libraries we're using),
please see
<http://www.teach.cs.toronto.edu/~csc148h/fall/software/hypothesis.html>.

Note: this file is for support purposes only, and is not part of your
submission.
"""
import unittest
from stack import Stack
from ex3 import reverse, PeopleChain, ShortChainError
from hypothesis import given
from hypothesis.strategies import lists, text, integers


class TestStack(unittest.TestCase):

    def test_reverse_many(self):
        stack = Stack()
        for i in range(100):
            stack.push(i)
        reverse(stack)
        for i in range(100):
            self.assertEqual(stack.pop(), i)
        self.assertTrue(stack.is_empty())

    def test_reverse_empty(self):
        stack = Stack()
        reverse(stack)
        self.assertTrue(stack.is_empty())


class TestPeopleChain(unittest.TestCase):

    def setUp(self):
        self.chain = PeopleChain(['Iron Man', 'Janna', 'Kevan'])
        self.empty_chain = PeopleChain([])
        self.one_chain = PeopleChain(['David'])
        self.two_chain = PeopleChain(['Karen', 'Paul'])

    def test_get_leader_simple(self):
        self.assertEqual(self.chain.get_leader(), 'Iron Man')

    def test_get_second_simple(self):
        self.assertEqual(self.chain.get_second(), 'Janna')

    def test_get_third_simple(self):
        self.assertEqual(self.chain.get_third(), 'Kevan')

    @given(lists(text()), integers(min_value=1))
    def test_get_nth_on_out_of_bounds_index(self, names, offset):
        chain = PeopleChain(names)

        # Use assertRaises to check whether calling PeopleChain.get_nth
        # raises a ShortChainError on the given arguments.
        self.assertRaises(ShortChainError,
                          PeopleChain.get_nth,
                          chain,
                          len(names) + offset)


if __name__ == '__main__':
    unittest.main(exit=False)
