"""Assignment 1 - Domain classes (Task 2)

This module contains all of the classes required to represent the entities
in the experiment, including at least a class Parcel and a class Truck.
"""

from distance_map import DistanceMap

class Truck:
    """ Truck used in the experiments

    === private attribues ===
    @type depot: str
    @type _volume: int
    @type _id: int
    @type _route: [str]
    @type _distance_travelled: int

    === repersentation invarainat ===
    depot must be constant
    _volume >= 0
    """

    def __init__(self, id_, volume, depot):
        """Initialze all the attributes of the class
        set the id to <id> and volume to <volume>
        set distance_travelled to 0
        """
        self._id = id_
        self._volume = volume
        self._route = []
        self.depot = depot
        self._distance_travelled = 0

    def get_id(self):
        """Return the id of the truck
        @type self: Truck
        @rtype: int
        """
        return self._id

    def get_volume(self):
        """Return the remaining of the truck
        @type self: Truck
        @rtype: int
        """
        return self._volume

    def get_route(self):
        """Return the route of the truck
        @type self: Truck
        @rtype: [str]
        """
        return self._route

    def get_distance_travelled(self):
        """Return the distance travelled by the truck
        @type self: Truck
        @rtype: int
        """
        return self._distance_travelled

    def load(self, parcel):
        """load the parcel onto the truck
        decrement the volume by the volume of the parcel
        update the route to inclue the destination of the truck

        @type parcel = Parcel

        >>> t = Truck(12,12,'Ottawa')
        >>> p = Parcel(14,'Toronto','Markham',5)
        >>> t.load(p)
        >>> t.get_volume()
        7
        >>> t.get_route()
        ['Markham']
        """
        self._volume -= parcel.get_volume()

        if parcel.get_destination() not in self._route:
            self._route.append(parcel.get_destination())

    def deliver(self, map_):
        """ deliver all the parcels to their destination and calucate the distance travelled
        @type map_: DistanceMap
        @rtype: None
        """
        start_city = self.depot
        destinations = len(self.get_route())

        for i in range(0, destinations):
            min_dist = 0
            picked_city = ''

            for city in self.get_route():
                dist = map_.get_distance(start_city,city)

                if dist <min_dist or min_dist ==0:
                    min_dist = dist
                    picked_city = city

            self._route.remove(picked_city)
            start_city = picked_city
            self._distance_travelled += min_dist



class Parcel:
    """ Parcel to be delevered

    === Private attributes ===
    @type _id: int
    the id of the parcel

    @type _volume: int
    the volume of the parcel

    @type _source: str
    the city where the parcel came from

    @type _destination: str
    the destination of the parcel

    === Respresentation invariants ===
    _volume >0
    """

    def __init__(self, id_, source, destination,volume):
        """
        @type id_: int
        @type source: str
        @type destination: str
        @type volume: int
        """
        self._id = id_
        self._source = source
        self._destination = destination
        self._volume = volume

    def get_volume(self):
        return self._volume

    def get_id(self):
        return self._id

    def get_destination(self):
        return self._destination


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config='.pylintrc')
    import doctest
    doctest.testmod()
