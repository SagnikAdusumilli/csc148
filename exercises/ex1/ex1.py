"""CSC148 Exercise 1: Basic Object-Oriented Programming

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains starter code for Exercise 1.
It contains two classes that work together:
- SuperDuperManager, which manages all the cars in the system
- Car, a class which represents a single car in the system

Your task is to design and implement the Car class, and then modify the
SuperDuperManager methods so that they make proper use of the Car class.

You may not modify the public interface of any of the SuperDuperManager methods.
We have marked the parts of the code you should change with TODOs, which you
should remove once you've completed them.

Notes:
  1. We'll talk more about private attributes on Friday's class.
     For now, treat them the same as any other instance attribute.
  2. You'll notice we use a trailing underscore for the parameter name
     "id_" in a few places. It is used to avoid conflicts with Python
     keywords. Here we want to have a parameter named "id", but that is
     already the name of a built-in function. So we call it "id_" instead.
"""


class SuperDuperManager:
    """A class responsible for keeping track of all cars in the system.

    === Private Attributes ===
    @type _cars: dict[str, Car]
        A map of unique string identifiers to the corresponding Car.
        For example, _cars['a01'] would be a Car object corresponding to
        the id 'a01'.
    """

    def __init__(self):
        """Initialize a new SuperDuperManager.

        There are no cars in the system when first created.

        @type self: SuperDuperManager
        @rtype: None
        """
        self._cars = {}

    def add_car(self, id_, fuel):
        """Add a new car to the system.

        The new car is identified by the string <id_>, and has initial amount
        of fuel <fuel>.

        Do nothing if there is already a car with the given id.

        @type self: SuperDuperManager
        @type id_: str
        @type fuel: int
        @rtype: None
        """
        # Check to make sure the identifier isn't already used.
        if id_ not in self._cars:
            self._cars[id_] = Car(fuel)

    def move_car(self, id_, new_x, new_y):
        """Move the car with the given id.

        The car called <id_> should be moved to position (<new_x>, <new_y>).
        Do nothing if there is no car with the given id,
        or if the corresponding car does not have enough fuel.

        @type self: SuperDuperManager
        @type id_: str
        @type new_x: int
        @type new_y: int
        @rtype: None
        """
        if id_ in self._cars:
            self._cars[id_].move(new_x, new_y)

    def get_car_position(self, id_):
        """Return the position of the car with the given id.

        Return a tuple of the (x, y) position of the car with id <id_>.
        Return None if there is no car with the given id.

        @type self: SuperDuperManager
        @type id_: str
        @rtype: (int, int) | None
        """
        if id_ in self._cars:
            return self._cars[id_].get_position()

    def get_car_fuel(self, id_):
        """Return the amount of fuel of the car with the given id.

        Return None if there is no car with the given id.

        @type self: SuperDuperManager
        @type id_: str
        @rtype: int | None
        """
        if id_ in self._cars:
            return self._cars[id_].get_fuel()

    def dispatch(self, x, y):
        """Move a car to the given location.

        Choose a car to move based on the following criteria:
        (1) Only consider cars that *can* move to the location.
            (Ignore ones that don't have enough fuel.)
        (2) After (1), choose the car that would move the *least* distance to
            get to the location.
        (3) If there is a tie in (2), pick the car whose id comes first
            alphabetically. Use < to compare the strings.
        (4) If no cars can move to the given location, do nothing.

        @type self: SuperDuperManager
        @type x: int
        @type y: int
        @rtype: None
        """
        # this will point to the selected car
        selected_id = None
        min_dist = None
        for _id in self._cars:
            position = self._cars[_id].get_position()  # @type: (int, int)
            dist = abs(x - position[0]) + abs(y - position[1])

            if dist < self._cars[_id].get_fuel():
                if selected_id is None:
                    selected_id = _id
                    min_dist = dist
                elif dist < min_dist:
                    selected_id = _id
                    min_dist = dist
                else:
                    selected_id = min(_id, selected_id)

        if selected_id is not None:
            self.move_car(selected_id, x, y)


class Car:
    """A car in the Super system.

    === Attributes ===
    @type _fuel: int
    keep track of the how many grids the car can move

    @type _position: [int,int]
    keep track of the position of the car in the grid system
    """

    def __init__(self, fuel):
        """ initialze the instance attribues
        @type self: Car
        """

        self._fuel = fuel
        self._position = [0, 0]

    def move(self, x, y):
        """ change the car position of the car on the grid either vertially or
        horizontally
         @type self: Car
         @type x: int
         @type y: int
        """
        # store the distance between the destination and the current location
        dist = abs(self._position[0] - x) + abs(
            self._position[1] - y)  # type: int

        if dist <= self._fuel:  # move only if there is enough fuel
            self._position[0] = x
            self._position[1] = y
            self._fuel -= dist

    def get_position(self):
        """Return the grid location of the car
        @type self: Car
        @rtype: (int, int)
        """
        return self._position[0], self._position[1]

    def get_fuel(self):
        """Return the number of units of fuel left in the car
        @type self: Car
        @rtype: int
        """
        return self._fuel


if __name__ == '__main__':
    # Run python_ta to ensure this module passes all checks for
    # code inconsistencies and forbidden Python features.
    # Useful for debugging!
    import python_ta

    python_ta.check_errors()

    # Uncomment and run before final submission. This checks for style errors
    # in addition to code inconsistencies and forbidden Python features.
    python_ta.check_all()
