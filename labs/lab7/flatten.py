def flatten(lst):
    """
    @type lst: nestedList
    @rtype []
    >>> flatten(5)
    [5]
    >>> flatten([1, [2], 3])
    [1, 2, 3]
    >>> flatten([[1, 5, 7], [[4]], 0, [-4, [6], [7, [8], 8]]])
    [1, 5, 7, 4, 0, -4, 6, 7, 8, 8]
    """
    result = []
    if isinstance(lst, int):
        result.append(lst)
        return result

    for item in lst:

        result.extend(flatten(item))

    return result



