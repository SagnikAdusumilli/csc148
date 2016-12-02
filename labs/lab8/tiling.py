"""Lab 8: Trees and Recursion, Task 3

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module Description ===
This module contains a basic automatic random tiling generator that you will
complete for Task 3 of this lab.

There's quite a bit to read here - go slow, and make sure you read carefully
before writing any code yourself.

Keep in mind that this program requires the Python library pygame to be
installed (it already is for the Teaching Labs, but you'll need to install it
yourself if you're using your own machine).
"""
import random
import pygame


# Constants defining the size of a square, and two colours.
SQUARE_SIZE = 20
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


def draw_grid(n):
    """Draw a pygame grid of size 2^n by 2^n.

    Precondition: n >= 1

    @type n: int
    @rtype: None
    """
    # Initialize a pygame screen filled in black.
    pygame.init()
    screen = pygame.display.set_mode((2**n * SQUARE_SIZE, 2**n * SQUARE_SIZE))
    screen.fill(BLACK)

    # Draw white gridlines in the screen.
    for i in range(2 ** n):
        for j in range(2 ** n):
            rect = (i * SQUARE_SIZE, j * SQUARE_SIZE,
                    (i + 1) * SQUARE_SIZE, (j + 1) * SQUARE_SIZE)
            pygame.draw.rect(screen, WHITE, rect, 1)

    # Uncomment the following part after you've implemented tile_with_dominoes
    tiling = tile_with_dominoes(n)
    for domino in tiling:
        domino.draw(screen)

    # Display the screen to the user.
    pygame.display.flip()


class Domino:
    """A domino on a grid.

    === Attributes ===
    @type position: list[(int, int)]
        The location of the domino on the grid.
    @type colour: (int, int, int)
        The colour of the domino, representing in RGB colour form.

    === Representation invariants ===
    - len(position) == 2
    - position's two tuples are adjacent squares on the grid
      For a 2^n by 2^n grid, each tuple's (x, y) coordinates should both be
      between 0 and 2^n - 1, inclusive.

      The position should *not* depend on SQUARE_SIZE - this constant is only
      used when drawing the domino using pygame.

      **IMPORTANT!!!**
      In pygame, the origin (0, 0) position is located at the *top-left* corner
      of the window. Increasing the y coordinate moves *down* the grid.

    - each number in colour is between 0 and 255, inclusive

    """
    def __init__(self, square1, square2):
        """Initialize a new domino with the given two squares.

        Pick a random colour for the domino.

        Precondition: square1 and square2 are adjacent

        @type self: Domino
        @type square1: (int, int)
        @type square2: (int, int)
        @rtype: None
        """
        self.position = [square1, square2]

        self.colour = (random.randint(0, 255),
                       random.randint(0, 255),
                       random.randint(0, 255))

    def add_offset(self, x_offset, y_offset):
        """Add the given offset to each square in this domino.

        @type self: Domino
        @type x_offset: int
        @type y_offset: int
        @rtype: None
        """
        for i in range(len(self.position)):
            old_x, old_y = self.position[i]
            self.position[i] = (old_x + x_offset, old_y + y_offset)

    def draw(self, screen):
        """Draw this domino onto the given screen.
        """
        x_coords = [self.position[0][0], self.position[1][0]]
        y_coords = [self.position[0][1], self.position[1][1]]

        pygame.draw.rect(screen, self.colour,(min(x_coords) * SQUARE_SIZE, min(y_coords) * SQUARE_SIZE,(max(x_coords) + 1) * SQUARE_SIZE,(max(y_coords) + 1) * SQUARE_SIZE))


# TODO: implement this function!
def tile_with_dominoes(n):
    """Return a random tiling of a 2^n by 2^n grid by dominoes.

    Remember that you should be returning a list of dominoes here.
    Think recursively! Mentally divide up the 2^n by 2^n grid
    into four quadrants, each of size 2^(n-1).

    Precondition: n >= 1.

    **IMPORTANT!!!**
    In pygame, the origin (0, 0) position is located at the *top-left* corner
    of the window. Increasing the y coordinate moves *down* the grid.

    @type n: int
    @rtype: list[Domino]
    """
    if n == 1:
        return _tile_2_by_2()
    else:
        # TODO (1)
        # Compute four different tilings of a 2^(n-1) by 2^(n-1) grid,
        # for the four different quadrants.
        q1 = tile_with_dominoes(n-1)
        q2 = tile_with_dominoes(n-1)
        q3 = tile_with_dominoes(n-1)
        q4 = tile_with_dominoes(n-1)


        # TODO (2)
        # Each tiling will have square coordinates between 0 and 2^(n-1),
        # but these coordinates are only good for the *upper-left* quadrant.
        # Add an offset to the upper-right, lower-left, and lower-right tilings
        # so that the dominoes are placed in the correct quadrant.
        #
        # Remember that the positions here do *not* depend on SQUARE_SIZE.

        for dom in q2:
            dom.add_offset(2**(n-1), 0)

        for dom in q3:
            dom.add_offset(0, 2**(n-1))

        for dom in q4:
            dom.add_offset(2**(n-1), 2**(n-1))

        # TODO (3)
        return q1 + q2 + q3 + q4


def _tile_2_by_2():
    """Return a random tiling of a 2 by 2 grid.

    Randomly choose between tiling the grid vertically or horizontally.

    @rtype: list[Domino]
    """
    r = random.randint(0, 1)

    # 0 = veritical
    if r == 0:
        dom1 = Domino((0, 0), (0, 1))
        dom2 = Domino((1, 0), (1, 1))
    else:
        dom1 = Domino((0, 0), (1, 0))
        dom2 = Domino((0, 1), (1, 1))

    return [dom1, dom2]


if __name__ == '__main__':
    draw_grid(int(input()))
    input('Press Enter to exit\n')
