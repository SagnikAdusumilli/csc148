"""Assignment 1 - Domain classes (Task 2)

This module contains all of the classes required to represent the entities
in the experiment, including at least a class Parcel and a class Truck.
"""

from distance_map import DistanceMap


class PathNotFoundError(Exception):
    """Exception Raised when the distance between 2 cities is unknown"""


class Truck:
    """ Truck used in the experiments

    === attribues ===
    @type depot: str

    === private attribues ===
    @type _volume: int
    @type __initial_volume: int
    @type _id: int
    @type _route: [str]
    @type _distance_travelled: int

    === repersentation invarainat ===
    depot must be constant
    _volume >= 0
    __initial_volume must be constant
    """

    def __init__(self, id_, volume, depot):
        """Initialze all the attributes of the class
        set the id to <id> and volume to <volume>
        set distance_travelled to 0
        """
        self._id = id_
        self._volume = volume
        self.__initial_volume = volume
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

    def get_initial_volume(self):
        """Return the inital volume of the truck
        @rtype: int
        """
        return self.__initial_volume

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

    def deliver_optimized(self, map_):
        """ deliver all the parcels to their destination in an optimzed manner
        and calucate the distance travelled
        @type map_: DistanceMap
        @rtype: None
        """
        start_city = self.depot
        destinations = len(self.get_route())

        for i in range(0, destinations):
            min_dist = 0
            picked_city = ''

            for city in self.get_route():
                dist = map_.get_distance(start_city, city)

                if dist is None:
                    raise PathNotFoundError

                if dist < min_dist or min_dist == 0:
                    min_dist = dist
                    picked_city = city

            self._route.remove(picked_city)
            start_city = picked_city
            self._distance_travelled += min_dist

    def deliver(self, map_):
        """deliver all the parcesl to thier locations and calulate the distance
        travelled
        @type map_: DistanceMap
        @rtype: None
        """

        start_city = self.depot

        while len(self._route) != 0:

            destination = self._route.pop(0)
            dist = map_.get_distance(start_city, destination)

            if dist is None:
                raise PathNotFoundError

            self._distance_travelled += dist
            start_city = destination


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

    def __init__(self, id_, source, destination, volume):
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
        """return the volume of the parcel
        @type self: Parcel
        @rtype int
        """
        return self._volume

    def get_id(self):
        """return the id of the parcel
        @type self: Parcel
        @rtype int
        """
        return self._id

    def get_destination(self):
        """ return the destination of the parcel
        @type self: Parcel
        @rtype str
        """
        return self._destination


def create_priority_function(compare_value, order):
    """Return a method for _less_than method in PriorityQueue
    based on the given priorities (<cmpare_values>, order)
    @type compare_value: str
    what will be compared (volume or city names)

    @type order: str
    non-decreasing or non-increasing

    @rtype: Callable[[Object, Object]]
    """

    if compare_value == 'volume':
        if order == 'non-decreaing':
            def bigger_than(item1, item2):
                """ Return True if volume of <item1> is bigger than
                the volume of <item2>
                @type item1: Parcel|Truck
                @type item2: Parcel|Truck
                @rtype: bool
                """
                return item1.get_volume() > item2.get_volume()

            return bigger_than
        else:
            def smaller_than(item1, item2):
                """ Return True if volume of <item1> is bigger than
                the volume of <item2>
                @type item1: Parcel|Truck
                @type item2: Parcel|Truck
                @rtype: bool
                """
                return item1.get_volume() < item2.get_volume()

            return smaller_than
    else:
        if order == 'non-decreaing':
            def bigger_than(parcel1, parcel2):
                """ Return True if desination's name of <parcel1> is bigger than
                the desnination's of <parcel2>
                @type parcel1: Parcel
                @type parcel2: Parcel
                @rtype: bool
                """
                return len(parcel1.get_destination()) > len(
                    parcel2.get_destination())

            return bigger_than
        else:
            def smaller_than(parcel1, parcel2):
                """ Return True if desination's name of <parcel1> is bigger than
               the desnination's of <parcel2>
               @type parcel1: Parcel
               @type parcel2: Parcel
               @rtype: bool
               """
                return len(parcel1.get_destination()) > len(
                    parcel2.get_destination())

            return smaller_than


def get_unused_trucks(trucks):
    """Return the list of trucks that were not used
    @type trucks: [Truck]
    @rtype: [Truck]
    """
    unused_trucks = []

    for truck in trucks:
        if truck.get_volume() == truck.get_initial_volume():
            unused_trucks.append(truck)

    return unused_trucks


def get_unused_space(trucks):
    """Return the total unused space
    @type trucks: [Truck]
    @rtype: int
    """

    space = 0
    for truck in trucks:
        space += truck.get_volume()

    return space


def get_average_fullness(trucks):
    """Return the average of the percentage of
    volume taken up the parcels on each
    truck round to 1 decimal place
    @type trucks: [Truck]
    @rtype: float
    """
    sum_ = 0.0

    if len(trucks)==0:
        return sum_

    for truck in trucks:
        volume_taken = (truck.get_initial_volume()
                        - truck.get_volume()) / truck.get_initial_volume()

        sum_ += volume_taken * 100

    return round(sum_ / len(trucks), 1)


def get_average_distance(trucks):
    """Return the average distance
    covered by the truck rounded to 1 decimal place
    @type trucks: [Truck]
    @rtype: float
    """
    sum_ = 0.0

    if len(trucks)==0:
        return sum_

    for truck in trucks:
        sum_ += truck.get_distance_travelled()

    return round(sum_/len(trucks))


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config='.pylintrc')
    import doctest

    doctest.testmod()
