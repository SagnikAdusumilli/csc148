"""Assignment 1 - Domain classes (Task 2)

This module contains all of the classes required to represent the entities
in the experiment, including at least a class Parcel and a class Truck.
"""

class Truck:
    pass
class Parcel:
    pass

if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='.pylintrc')
    import doctest
    doctest.testmod()
