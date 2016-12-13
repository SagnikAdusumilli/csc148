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
