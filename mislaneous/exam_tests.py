"""
codes that appear in the exam
"""


def mystery(s):
    """
    Q1 in august 2015
    @param s:
    @type s:
    @return:
    @rtype:
    """

    if len(s) < 2:
        return s[0]
    else:
        m = len(s) // 2
        print('>', s[:m], s[m:])

        s1 = mystery(s[:m])
        s2 = mystery(s[m:])

        if s1[0] == s2[0]:
            print("A: ", s1, s2)
            r = s1 + s2
        elif s1[0] < s2[0]:
            print("B: ", s1, s2)
            r = s1[0]
        else:
            print("C: ", s1, s2)
            r = s2[0]

        print('<', r)
        return r


class SmallTreeError(Exception):
    """
    raise error is the BTNode is too small
    """


class BTNode:
    """ a node in binary tree"""

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def balance(self):
        """
        return number of right child - number of left child
        @return:
        @rtype:
        >>> t1 = BTNode(6)
        >>> t2 = BTNode(7, t1)
        >>> t3 = BTNode(5, t2)
        >>> t4 = BTNode(2, t3, BTNode(8, BTNode(9)))
        >>> t4.balance()
        -3
        """
        if self.right is None and self.left is None:
            return 0
        elif self.left is None:
            return self.right.balance() + 1
        elif self.right is None:
            return self.left.balance() - 1
        else:
            return self.right.balance() + self.left.balance()

    def second_deepest(self):
        """
        Return the depth of the second deepest node in the tree at this node
        @rtype: int
        >>> t1 = BTNode(6)
        >>> t2 = BTNode(7, t1)
        >>> t3 = BTNode(5, t2)
        >>> t4 = BTNode(2, t3, BTNode(8, BTNode(9)))
        >>> t5 = BTNode(99, t4)
        >>> t2.second_deepest()
        0
        """

        # case if the tress is too small:
        if self.right is None and self.left is None:
            raise SmallTreeError
        # case: if the tree has only one more level:
        elif self.right is None:
            if self.left.left is None:
                return 0
            else:
                return self.left.second_deepest() + 1
        elif self.left is None:
            if self.left.left is None:
                return 0
            else:
                return self.right.second_deepest() + 1
        else:
            if self.right.right is None and self.left.left is None:
                return 0
            else:
                return max(self.right.second_deepest(), self.left.second_deepest()) + 1


def sum_to(n):
    """

    @param n:
    @type n:
    @return:
    @rtype:
    >>> sum_to(100)
    5050saw
    """

    if n == 0:
        return n
    else:
        return n + sum_to(n-1)


def mystery2(n):
    """
    >>> mystery2(3)
    True
    >>> mystery2(4)
    False

    """
    return _mystery2(n, 2)


def _mystery2(n, t):
    if t == n:
        return True

    return (n % t != 0) and _mystery2(n, t+1)


def insert_sort(lst):
    """
    @param lst:
    @type lst:
    @return:
    @rtype:
    >>> lst = [4, 2, 6, 7, 0]
    >>> insert_sort(lst)
    >>> lst
    [0, 2, 4, 6, 7]
    >>> lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> insert_sort(lst)
    >>> lst
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    for i in range(1, len(lst)):
        j = i
        temp = lst[i]

        while j-1 >= 0 and lst[j-1] > temp:
            lst[j] = lst[j-1]
            j -= 1

        lst[j] = temp
