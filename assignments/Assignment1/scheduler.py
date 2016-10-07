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

    def _get_eligibleTrucks(self, parcel, trucks):
        """Retrun a list of trucks which can carry the parcel
        @type self: Scheduler
        @type parcel: Parcel
        @type trucks: [Truck]
        @rtype [Truck]
        """
        raise NotImplementedError


class RandomScheduler(Scheduler):

    def schedule(self, parcels, trucks, verbose=False):

        shuffle(parcels)
        not_used_parcels = []

        for parcel in parcels:
            eligible_trucks = self._get_eligibleTrucks(parcel, trucks)

            if len(eligible_trucks) == 0:
                not_used_parcels.append(parcel)
            else:
                chosen_index = choice(eligible_trucks)
                eligible_trucks[chosen_index].load(parcel)

        return not_used_parcels




    def _get_eligibleTrucks(self, parcel, trucks):
        list = []
        for truck in trucks:
            if truck.get_volume()<=parcel.get_volume() :
                list.append(parcel)

        return list

class GreedyScheduler(Scheduler):

    def schedule(self, parcels, trucks, verbose=False):
        pass

    def _get_eligibleTrucks(self, parcel, trucks):
        pass






if __name__ == '__main__':
    import doctest
    doctest.testmod()
    import python_ta
    python_ta.check_all(config='.pylintrc')
