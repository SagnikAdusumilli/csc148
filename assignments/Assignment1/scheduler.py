"""Assignment 1 - Scheduling algorithms (Task 4)

This module contains the abstract Scheduler interface, as well as the two
classes RandomScheduler and GreedyScheduler, which implement the two
scheduling algorithms described in the handout.

Your task is to implement RandomScheduler and GreedyScheduler.
You may *not* change the public interface of these classes, except that
you must write appropriate constructors for them.  The two constructors do not
need to have the same signatures.

Any attributes you use must be private, so that the public interface is exactly
what is specified by the Scheduler abstract class.
"""
from random import shuffle, choice
from container import PriorityQueue


class Scheduler:
    """A scheduler, capable of deciding what parcels go onto which trucks, and
    what route each truck will take.

    This is an abstract class.  Only child classes should be instantiated.

    You may add *private* methods to this class so make them available to both
    subclasses.
    """

    def schedule(self, parcels, trucks, verbose=False):
        """Schedule the given parcels onto the given trucks.

        Mutate the trucks so that they store information about which
        parcels they will deliver and what route they will take.
        Do *not* mutate the parcels.

        Return the parcels that do not get scheduled onto any truck, due to
        lack of capacity.

        If <verbose> is True, print step-by-step details regarding
        the scheduling algorithm as it runs.  This is *only* for debugging
        purposes for your benefit, so the content and format of this
        information is your choice; we will not test your code with <verbose>
        set to True.

        @type self: Scheduler
        @type parcels: list[Parcel]
            The parcels to be scheduled for delivery.
        @type trucks: list[Truck]
            The trucks that can carry parcels for delivery.
        @type verbose: bool
            Whether or not to run in verbose mode.
        @rtype: list[Parcel]
            The parcels that did not get scheduled onto any truck, due to
            lack of capacity.
        """
        raise NotImplementedError

    def _get_eligible_trucks(self, parcel, trucks):
        """Retrun a list of trucks which can carry the parcel
        @type self: Scheduler
        @type parcel: Parcel
        @type trucks: [Truck]
        @rtype [Truck]
        """
        list = []
        for truck in trucks:
            if truck.get_volume() >= parcel.get_volume():
                list.append(truck)

        return list


class RandomScheduler(Scheduler):
    """Process the parcel in random order and assign to random truck"""

    def schedule(self, parcels, trucks, verbose=False):

        shuffle(parcels)
        not_used_parcels = []

        for parcel in parcels:
            eligible_trucks = Scheduler._get_eligible_trucks(self,
                                                             parcel, trucks)

            if len(eligible_trucks) == 0:
                not_used_parcels.append(parcel)
            else:
                chosen_truck = choice(eligible_trucks)
                chosen_truck.load(parcel)

        return not_used_parcels


class GreedyScheduler(Scheduler):
    """Process each parcel accoring to priority
    of the truck and parcel queues

    === Private attribues ===
    @type _t_queue: PriorityQueue
    priority queue for sorting the trucks

    @type _p_queue: PriorityQueue
    priority queue for sorting the parcles
    """

    # specify the types of priority qeue
    # for truck and parcel
    def __init__(self, func_truck, func_parcel):
        """
        @type self: GreedyScheduler
        @type func_truck: Callabe([Truck, Truck])
        @type func_parcel: Callabe([Truck, Truck])
        """
        self._t_queue = PriorityQueue(func_truck)
        self._p_queue = PriorityQueue(func_parcel)

    def schedule(self, parcels, trucks, verbose=False):

        not_used_parcels = []

        # sort the parcels according to priority
        for parcel in parcels:
            self._p_queue.add(parcel)

        # get eligible trucks for each parcle
        for parcel in parcels:
            eligible_trucks = self._get_eligible_trucks(parcel, trucks)

            if eligible_trucks == []:
                not_used_parcels.append(parcel)
            else:
                for truck in eligible_trucks:
                    self._t_queue.add(truck)

                chosen_truck = self._t_queue.remove()
                chosen_truck.load(parcel)

        return not_used_parcels

    def _get_eligible_trucks(self, parcel, trucks):

        # filter all the trucks with enough volume
        volume_eligible = Scheduler._get_eligible_trucks(self, parcel, trucks)

        city_eligible = []
        for truck in volume_eligible:
            if parcel.get_destination() in truck.get_route():
                city_eligible.append(truck)

        if city_eligible == []:
            return volume_eligible
        else:
            return city_eligible

if __name__ == '__main__':
    import doctest

    doctest.testmod()
    import python_ta

    python_ta.check_all(config='.pylintrc')
