"""Assignment 1 - Domain classes (Task 2)

This module contains all of the classes required to represent the entities
in the experiment, including at least a class Parcel and a class Truck.
"""

class Truck:
    """ Truck used in the experiments

    === private attribues ===
    @type _volume: int
    @type _id: int
    @type _route: {str}
    @type _distance_travelled: int
    """

    def __init__(self, id, volume):
        """Initialze all the attributes of the class
        set the id to <id> and volume to <volume>
        set distance_travelled to 0
        """
        self._id = id
        self._volume = volume
        self._route = {}
        self._distance_travelled = 0

    def get_id(self):
        return self._id
    def get_volume(self):
        return self._volume
    def get_route(self):
        return self._route
    def get_distance_travelled(self):
        return self._distance_travelled

class Parcel:
    pass

if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='.pylintrc')
    import doctest
    doctest.testmod()
