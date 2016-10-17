"""Assignment 1 - Running experiments (Tasks 5 & 6)

This module contains class SchedulingExperiment.  It can create an experiment
with input data and an algorithm configuration specified in a dictionary, then
run the experiment, generate statistics as the result of the experiment, and
(optionally) report the statistics.

This module is responsible for all the reading of data from the data files.

To test your code, we will construct instances of SchedulingExperiment, call
its methods, and examine the dictionary of statistics that method run
returns.

If you defined any domain classes other than Parcel and Truck, you may import
them here.  You may not import external libraries.
"""
from scheduler import RandomScheduler, GreedyScheduler
from domain import Parcel, Truck, create_priority_function
from distance_map import DistanceMap


class SchedulingExperiment:
    """An experiment in scheduling parcels for delivery.

    To complete an experiment involves four stages:

    1. Read in all data from necessary files, and create corresponding objects.
    2. Run a scheduling algorithm to assign parcels to trucks.
    3. Compute statistics showing how good the assignment of parcels to trucks
       is.
    4. Report the statistics from the experiment.

    === Private Attribues===
    @type _map: DistanceMap
    @type _trucks: [Trucks]
    @type _parcles: [parcels]
    """

    def __init__(self, config):
        """Initialize a new experiment from a configuration dictionary.

        Precondition: <config> contains keys and values as specified
        in Assignment 1.

        @type config: dict[str, str]
            The configuration for this experiment, including
            the data files and algorithm configuration to use.

        @rtype: None
        """

        # initialize map
        self._map = DistanceMap(read_distance_map(config['map_file']))

        # initialize trucks
        self._trucks = read_trucks(config['truck_file'],
                                   config['depot_location'])

        # initialize parcels
        self._parcels = read_parcels(config['parcel_file'])

        #initilize config dictionary
        self._config = config

    def run(self, report=False):
        """Run the experiment and return statistics on the outcome.

        If <report> is True, print a report on the statistics from this
        experiment.  Either way, return the statistics in a dictionary.

        If <self.verbose> is True, print step-by-step details
        regarding the scheduling algorithm as it runs.

        @type self: SchedulingExperiment
        @type report: bool
            Whether or not to print a report on the statistics.
        @rtype: dict[str, int | float]
            Statistics from this experiment. Keys and values are as specified
            in Step 6 of Assignment 1.
        """
        #TODO implement this method

        """
        fleet: the number of trucks in the fleet
    unused_trucks: the number of unused trucks (trucks that have no parcels)
    avg_distance: among the used trucks, the average distance they will have to travel to follow their scheduled route
    avg_fullness: among the used trucks, their average fullness. The fullness of a truck is the percentage of its volume that is taken by parcels
    unused_space: among the used trucks, their total unused space. The unused space of a truck is the amount (not percentage) of its volume         that is not taken by parcels
    unscheduled: the number of unschedule parcels (parcels that did not fit onto any truck)
        """
        stats = {}

        scheduler = None
        if self._config['algorithm'] == 'greedy':
            scheduler = GreedyScheduler(
                create_priority_function('volume', self._config['truck_order']),
                create_priority_function(self._config['parcel_priority'],
                                         self._config['parcel_order']))

        stats['unscheduled'] = len(scheduler.schedule(self._parcels, self._trucks))

        print(stats)


    def _compute_stats(self):
        """Compute the statistics for this experiment.

        Precondition: _run has already been called.

        @type self: SchedulingExperiment
        @rtype: Dict[str, int | float]
            Statistics from this experiment. Keys and values are as specified
            in Step 6 of Assignment 1.
        """

        scheduler = None
        parcels_not_used = []
        if self._config['algorithm'] == 'greedy':
            scheduler = GreedyScheduler(
                create_priority_function('volume', self._config['truck_order']),
                create_priority_function(self._config['parcel_priority'],
                                         self._config['parcel_order']))

        parcels_not_used = scheduler.schedule(self._parcels, self._trucks)



    def _print_report(self):
        """Report on the statistics for this experiment.

        This method is *only* for debugging purposes for your benefit, so
        the content and format of the report is your choice; we
        will not call your run method with <report> set to True.

        Precondition: _compute_stats has already been called.

        @type self: SchedulingExperiment
        @rtype: None
        """

        # TODO: Implement this method!
        pass


# ----- Helper functions -----

def read_parcels(parcel_file):
    """Read parcel data from <parcel_file> and return XXXX

    @type parcel_file: str
        The name of a file containing parcel data in the form specified in
        Assignment 1.
    @rtype: [Parcel]
    """
    parcels = []

    with open(parcel_file, 'r') as file:
        for line in file:
            tokens = line.strip().split(',')
            pid = int(tokens[0].strip())
            source = tokens[1].strip()
            destination = tokens[2].strip()
            volume = int(tokens[3].strip())
            parcels.append(Parcel(pid, source, destination, volume))

    return parcels


def read_distance_map(distance_map_file):
    """Read distance data from <distance_map_file> and return a dictionary
    where the key is the start and end city pair and value is the distance between them

    @type distance_map_file: str
        The name of a file containing distance data in the form specified in
        Assignment 1.
    @rtype: {(str,str), int}

    TODO: Complete this docstring.
    """
    data = {}

    with open(distance_map_file, 'r') as file:
        for line in file:
            tokens = line.strip().split(',')
            c1 = tokens[0].strip()
            c2 = tokens[1].strip()
            dist = int(tokens[2].strip())
            data[(c1, c2)] = dist

    return data


def read_trucks(truck_file, depot_location):
    """Read truck data from <truck_file> and return XXXX

    @type truck_file: str
        The name of a file containing truck data in the form specified in
        Assignment 1.
    @type depot_location: str
        The city where all the trucks (and packages) are at the start of the
        experiment.
    @rtype: [Truck]
    """
    truck_list = []

    with open(truck_file, 'r') as file:
        for line in file:
            tokens = line.strip().split(',')
            tid = int(tokens[0])
            capacity = int(tokens[1])

            truck_list.append(Truck(tid, capacity, depot_location))

    return truck_list


def sanity_check(config_file):
    """Configure and run a single experiment on the scheduling problem
    defined in <config_file>

    Precondition: <config_file> is a json file with keys and values
    as in the dictionary format defined in Assignment 1.

    @type config_file: str
    @rtype: None
    """
    # Read an experiment configuration from a file and build a dictionary
    # from it.
    import json
    with open(config_file, 'r') as file:
        configuration = json.load(file)
    # Create and run an experiment with that configuration.
    experiment = SchedulingExperiment(configuration)
    experiment.run(report=True)


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config='.pylintrc')
