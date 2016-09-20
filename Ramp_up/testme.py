

def is_even(num):
    """ return True is num is even
    @type num: int
    @rtype: bool

    >>> is_even(3)
    False
    >>> is_even(4)
    True
    """
    return num % 2 == 0


def findGreater(num1, num2):
    """return the number which is greater
     @type num1: int
     @type num2: int
     @rtype: int

     >>> findGreater(1,2)
     2
     >>> findGreater(1,1)
     1
 """
    if num1 >= num2:
        return num1
    else:
        return num2


if __name__ == '__main__':
    import doctest

    doctest.testmod()
