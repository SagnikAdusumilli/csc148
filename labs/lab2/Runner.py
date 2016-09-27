class Runner:
    """
    Runners in the Race

    ===Private Attribues===
    @type _name: str
        The name of runner
    @type _email: str
        The email address of the runner
    @type _time: int
        The time he/she will take to complete the race

    """
    def __init__(self, name, email, time ):

        self._name = name
        self._email = email
        self._time = time

    def set_name(self, name):
        """set the current name to a new name
        @type name: str
        """
        self._name = name

    def get_name(self):
        """Return the name of the runner
        @rtype: str
        """
        return self._name

    def set_email(self, email):
        """set the current email to a new email
        @type email: str
        """
        self._name = email

    def get_email(self):
        """Return the email of the runner
        @rtype: str
        """
        return self._email

    def set_time(self, time):
        """set the current time to a new time
        @type time: int
        """
        self._time = time

    def get_time(self):
        """Return the time of the runner
        @rtype: int
        """
        return self._time
