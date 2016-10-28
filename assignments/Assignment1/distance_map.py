"""Assignment 1 - Distance map (Task 1)

This module contains the class DistanceMap, which is used to store and lookup
distances between cities.  This class does not read distances from the map file.
All reading from files is done in module experiment.

Your task is to design and implement this class.

Do not import any modules here.
"""


class DistanceMap:
    """store the distances between cities present in the map data file

    === private attribues ===
    @type _map: {(str,str),int}
    Map the start city and end city to the distance from start city to end city

    === repersation invariants ===
    the data must contain atleast two cities
    """

    def __init__(self, data):
        """initialze the map
        @type self: DistanceMap
        @type data: {(str,str),int}
        @rtype: None
        >>> m = DistanceMap({('a', 'b'): 2})
        >>> m._map
        {('a', 'b'): 2}
        """
        self._map = data

    def get_distance(self, start_city, end_city):
        """ return the distance between <start_city> and <end_city>
        if no distance if found, return null
        @type start_city: str
        @type end_city: str
        @rtype: int|None

        >>> map2 = DistanceMap({('a', 'b'): 2})
        >>> map2.get_distance('a','b')
        2
        >>> map2.get_distance('b','c')
        """
        return self._map.get((start_city, end_city))


if __name__ == '__main__':
    import doctest

    doctest.testmod()
    import python_ta

    python_ta.check_all(config='.pylintrc')
