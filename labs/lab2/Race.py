from Runner import Runner


class Race:
    """ manages the info for runners
    === private attribues ===
    @type: _runners: [Runner]
        List of Runners in the Race
    @type: _categories: {int, [Runner]}
        Dictionary of List of Runners devided based on their speed
    """

    def __init__(self):
        """initialize the attribues

        @type self = Race
        """
        self._runners = list()
        self._categories = dict()

    def get_groups(self):
        """ get the dictionary of runners devided by speed
        @type self: Race
        """
        return self._categories

    def get_runners(self):
        """ get the list of all the runners
        @type self: Race
        """
        return self._runners

    def add_runner(self, runner):
        """ Add <Runner> to the list of runners
        add <Runner> in the appropriate category of the dictoinary

        @type runner: Runner
        """
        category = int(runner.get_time() / 10)
        if runner not in self._runners:
            self._runners.append(runner)

            if runner.get_time() < 40:
                if category not in self._categories:
                    self._categories[category] = []
                    self._categories[category].append(runner)
                else:
                    self._categories[int(runner.get_time() / 10)].append(runner)
            else:
                if 4 not in self._categories:
                    self._categories[4] = []
                    self._categories[4].append(runner)

    def get_runner(self, email):
        """Locate a runner by their email from the list of runners
        @type email: str
        @rtype Runner
        """
        for i in range(0, len(self._runners)):
            if self._runners[i].get_email == email:
                return self._runners[i]

    def get_category(self, time):
        """ get a list of runners in the <time> category
        @type time: int
        @rtype [Runner]
        """
        if time < 40:
            return self._categories[int(time / 10)]
        else:
            return self._categories[4]

    def display_categories(self):
        """ Return a dictionary of devided runners that can be printed
         @type self: Race
         @rtype: {int,[str]}
        """
        display = dict()
        for i in self._categories:
            c = self._categories[i]
            display[i] = []
            for r in c:
                display[i].append(r.get_email())

        return display

    def remove_runner(self, email):
        """remove the runner with email address of <email> from both the race
        @type email: str
        """
        runner = self.get_runner(email)

        if runner is not None:
            self._runners.pop(runner)
            self.get_category(runner.time).pop(runner)

    def edit_email(self, email, new_email):
        """change the email address of the runner from <email> to <new_email>
        @type email:str
        @type new_email: str
        """
        runner = self.get_runner(email)
        runner.set_email(new_email)

    def edit_time(self, email, new_time):
        """set the time of the runner with email address, <email> to <new_time>
        @type email:str
        @type new_time: int
        """
        runner = self.get_runner(email)
        self.get_category(runner.time).pop(runner)
        self.get_category(new_time).add(runner)
        runner.set_time(new_time)
