def histogram(word):
    """ Return a dictionary with a letter as its keys and its values as the number
        of occurrences of that letter appearing in <word>.


    :type word: str
    :rtype: {str: int}

    >>> histogram('parrot') ==  {'a': 1, 'o': 1, 'p': 1, 'r': 2, 't': 1}
    True

    """
    d = {}
    for letters in word:
        d[letters] = d.get(letters, 0) + 1
    return d

if __name__ == '__main__':
    import doctest
    doctest.testmod()
