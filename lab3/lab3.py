"""CSC148 Lab 3: Inheritance

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto
"""
import random


class NumberGame:
    """A number game for two players.  A count starts at 0.  On a player's
    turn, he or she adds to the count an amount that must be between a set
    minimum and a set maximum.  The player who brings the count to a set
    goal amount is the winner.

    === Attributes ===
    @type goal: int
        The amount to reach in order to win the game.
    @type min_step: int
        The minimum legal move.
    @type max_step: int
        The maximum legal move.
    @type current: int
        The current amount.
    @type players: (Player, Player)
        The two Players.
    @type turn: int
        The turn we are on, beginning with turn 0.
        If turn is 0 or any even number, it is players[0]'s turn.
        If turn is any odd number, it is player[1]'s turn.

    === Representation invariants ==
    - turn >= 0
    - len(players) = 2
    - 0 <= current <= goal
    - 0 <= min_step <= max_step <= goal
    """

    def __init__(self, goal, min_step, max_step, player1, player2):
        """Initialize this NumberGame.

        @type self: NumberGame
        @type goal: int
        @type min_step: int
        @type max_step: int
        @type player1: Player
        @type player2: Player
        """
        self.goal = goal
        self.min_step = min_step
        self.max_step = max_step
        self.players = (player1, player2)
        self.turn = 0
        self.current = 0

    def play(self):
        """Play one round of this NumberGame.

        @type self: NumberGame
        @rtype: None
        """
        while self.current < self.goal:
            self.play_one_turn()
        # The player whose turn would be next (if the game weren't over) is
        # the loser.  The one whe went one turn before that is the winner.
        loser = self.whose_turn(self.turn)
        winner = self.whose_turn(self.turn - 1)
        print('And {} is the winner!!!'.format(winner.name))
        winner.record_win()
        loser.record_loss()

    def whose_turn(self, count):
        """Return the Player whose turn it is.

        @type self: NumberGame
        @type count: int
            The turn number.
        @rtype: Player
        """
        if count % 2 == 0:
            next_player = self.players[0]
        else:
            next_player = self.players[1]
        return next_player

    def play_one_turn(self):
        """Play a single turn in this NumberGame.

        Determine whose move it is, get their move, and update the current
        total as well as the number of the turn we are on.  Print the move
        and the new total.

        @type self: NumberGame
        @rtype: None
        """
        next_player = self.whose_turn(self.turn)
        amount = next_player.move(
            self.current,
            self.min_step,
            self.max_step,
            self.goal
        )
        print('{} moves {}'.format(next_player.name, amount))
        self.current = self.current + amount
        print('Total is now {}'.format(self.current))
        self.turn += 1


class Player:
    """Player in the game
    @type name: str
    @type wins: int
    @type losses: int
    """
    def __init__(self, new_name):
        self.name = new_name
        self.wins = 0
        self.losses = 0

    def move (self,status, min_step, max_step, goal):
        """make a move based on the information of the game
        @type status: int
        @type min_step: int
        @type max_step: int
        @type goal: int
        @rtype: int
        """
        raise NotImplementedError

class RandomPlayer(Player):
    def move(self, status, min_step, max_step, goal):
        return random.randint(min_step,max_step)

class StrategicPlayer(Player):

    def move(self, status, min_step, max_step, goal):
        


def make_player(generic_name):
    """Through user input, construct and return a new Player.

    Allow the user to choose a player name and player type.

    @type generic_name: int
        What to call this player when prompting the user for information
        about it/him/her.
    @rtype: Player
    """
    name = input("What is {}'s name? ".format(generic_name))
    type = input("What is {}'s type?\n press 1 for strategic\n press 2 for random\n press 3 for user controlled".format(generic_name))
    if type ==1:

    # TODO: Construct and return some sort of Player.


def main():
    """Prompt the user to configure and play the game.

    @rtype: None
    """
    goal = int(input('Goal amount? '))
    minimum = int(input('Minimum move? '))
    maximum = int(input('Maximum move? '))
    p1 = make_player('p1')
    p2 = make_player('p2')
    play_again = True
    while play_again:
        g = NumberGame(goal, minimum, maximum, p1, p2)
        g.play()
        print('{:} has {:} wins in {:} games ({:.2%})'.format(
              p1.name, p1.num_wins, p1.num_games, p1.num_wins / p1.num_games))
        print('{:} has {:} wins in {:} games ({:.2%})'.format(
              p2.name, p2.num_wins, p2.num_games, p2.num_wins / p2.num_games))
        play_again = input('Again? (y/n) ') == 'y'

if __name__ == '__main__':
    # import python_ta
    # python_ta.check_all(config='.pylintrc')
    # import doctest
    # doctest.testmod()
    main()
