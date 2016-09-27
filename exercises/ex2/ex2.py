"""CSC148 Exercise 2: Inheritance and Introduction to Stacks

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module description ===
This file contains starter code for Exercise 2.
It is divided into two parts:
- Task 1, which contains a set of classes that build on your work from
  last week
- Task 2, which contains the skeleton of a simple function involving a new
  data structure, the *Stack*.

Notes:
  1. When you override a method, you generally do not need to include a
     method docstring, unless there are subclass-specific details to describe.
     While PyCharm will complain about a missing docstring, you may ignore this
     warning *for this specific case*.
  2. A lot of starter code has been provided! Read through it carefully
     before starting. You may also find it interesting to compare our work
     against what you did for Exercise 1.
"""
# You will find these imports useful. Please do not import any others.
from math import sqrt  # sqrt used to calculate diagonal distances
import random          # used to generate random numbers


##############################################################################
# Task 1: Cars and other vehicles
##############################################################################
class SuperDuperManager:
    """A class responsible for keeping track of all cars in the system.

    === Private Attributes ===
    @type _vehicles: dict[str, Vehicle]
        A map of unique string identifiers to the corresponding vehicles.
        For example, _vehicles['a01'] would be a vehicle corresponding to
        the id_ 'a01'.
    """
    def __init__(self):
        """Initialize a new SuperDuperManager.

        Initially there are no vehicles in the system.

        @type self: SuperDuperManager
        @rtype: None
        """
        self._vehicles = {}

    def add_vehicle(self, vehicle_type, id_, fuel):
        """Add a new vehicle to the system of the given type.

        The new vehicle is identified by the string <id_>,
        and has initial amount of fuel <fuel>.

        Do nothing if there is already a vehicle with the given id.

        Precondition: <vehicle_type> is one of 'Car', 'Helicopter', or
                      'UnreliableMagicCarpet'.

        @type self: SuperDuperManager
        @type vehicle_type: str
        @type id_: str
        @type fuel: int
        @rtype: None
        """
        # Check to make sure the identifier isn't already used.
        if id_ not in self._vehicles:
            if vehicle_type == 'Car':
                self._vehicles[id_] = Car(fuel)
            elif vehicle_type == 'Helicopter':
                self._vehicles[id_] = Helicopter(fuel)
            elif vehicle_type == 'UnreliableMagicCarpet':
                self._vehicles[id_] = UnreliableMagicCarpet(fuel)

    def move_vehicle(self, id_, new_x, new_y):
        """Move a vehicle with the given id.

        The vehicle called <id_> should be moved to position (<new_x>, <new_y>).
        Do nothing if there is no vehicle with the given id,
        or if the corresponding vehicle does not have enough fuel to move.

        @type self: SuperDuperManager
        @type id_: str
        @type new_x: int
        @type new_y: int
        @rtype: None
        """
        if id_ in self._vehicles:
            self._vehicles[id_].move(new_x, new_y)

    def get_vehicle_position(self, id_):
        """Return the position of the vehicle with the given id.

        Return a tuple of the (x, y) position of the vehicle.
        Return None if there is no vehicle with the given id.

        @type self: SuperDuperManager
        @type id_: str
        @rtype: (int, int) | None
        """
        if id_ in self._vehicles:
            return self._vehicles[id_].position

    def get_vehicle_fuel(self, id_):
        """Return the amount of fuel of the vehicle with the given id.

        Return None if there is no vehicle with the given id.

        @type self: SuperDuperManager
        @type id_: str
        @rtype: int | None
        """
        if id_ in self._vehicles:
            return self._vehicles[id_].fuel


class Vehicle:
    """An interface for a vehicle in the Super Duper system.

    Note that this interface specifies *two* public attributes,
    and *two* public methods (the constructor is not considered public).

    Of the public methods, a default implementation is given for move,
    but not fuel_needed.

    It also defines a constructor that should be called by each of its
    subclasses.

    === Attributes ===
    @type position: (int, int)
        The position of this vehicle.
    @type fuel: int
        The amount of fuel remaining for this vehicle.

    === Representation invariants ===
    - fuel >= 0
    """
    def __init__(self, new_fuel, new_position):
        """Initialize a new Vehicle with the given fuel and position.

        Precondition: new_fuel >= 0

        @type self: Vehicle
        @type new_fuel: int
        @type new_position: (int, int)
        @rtype: None
        """
        self.fuel = new_fuel
        self.position = new_position

    def fuel_needed(self, new_x, new_y):
        """Return how much fuel would be used to move to the given position.

        Note: the amount returned may be larger than self.fuel,
        indicating that this vehicle may not move to the given position.

        @type self: Vehicle
        @type new_x: int
        @type new_y: int
        @rtype: float
        """
        raise NotImplementedError

    def move(self, new_x, new_y):
        """Move this vehicle to a new position.

        Do nothing if this vehicle does not have enough fuel to move.

        @type self: Vehicle
        @type new_x: int
        @type new_y: int
        @rtype: None
        """
        needed = self.fuel_needed(new_x, new_y)
        if needed <= self.fuel:
            self.position = (new_x, new_y)
            self.fuel -= needed


# TODO: Implement this class (you can use your work from Exercise 1)
class Car(Vehicle):
    """A car in the Super Duper system.

    A car can only move vertically and horizontally, and uses
    one unit of fuel per unit distance travelled.
    """
    pass


# TODO: Implement this class. Note: We've imported the sqrt function for you.
class Helicopter(Vehicle):
    """A helicopter. Can travel diagonally between points."""
    pass


# TODO: Implement this class. Note: We've imported the random module for you.
class UnreliableMagicCarpet(Vehicle):
    """An unreliable magic carpet.

    Does not need to use fuel to travel, but ends up in a random position
    within two horizontal and vertical units from the target destination.
    """
    pass


##############################################################################
# Task 2: Introduction to Stacks
##############################################################################
def reverse_top_two(stack):
    """Reverse the top two elements on <stack>.

    Precondition: <stack> has at least two items.

    @type stack: Stack
    @rtype: None

    >>> from obfuscated_stack import Stack
    >>> stack = Stack()
    >>> stack.push(1)
    >>> stack.push(2)
    >>> reverse_top_two(stack)
    >>> stack.pop()
    1
    >>> stack.pop()
    2
    """
    # TODO: implement this function after you've read about Stacks.
    pass

if __name__ == '__main__':
    # Run python_ta to ensure this module passes all checks for
    # code inconsistencies and forbidden Python features.
    # Useful for debugging!
    import python_ta
    python_ta.check_errors(config='.pylintrc')

    # Uncomment and run before final submission. This checks for style errors
    # in addition to code inconsistencies and forbidden Python features.
    # python_ta.check_all(config='.pylintrc')
