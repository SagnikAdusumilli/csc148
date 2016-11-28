"""CSC148 Exercise 7: Recursion Wrap-Up

=== CSC148 Fall 2016 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module description ===
This file contains starter code for Exercise 7.
"""


##############################################################################
# Task 1: A variation on sorting
##############################################################################

def kth_smallest(lst, k):
    """Return the <k>-th smallest element in <lst>.

    Raise IndexError if k < 0 or k >= len(lst).
    Note: for convenience, k starts at 0, so kth_smallest(lst, 0) == min(lst).

    Precondition: <lst> does not contain duplicates.

    @type lst: list[int]
    @type k: int
    @rtype: int

    >>> lst = [1, -2, 0, -2351984498541921861760, -1]
    >>> kth_smallest(lst, 2)
    -1
    """
    # Hint: partition the list based on a chosen pivot.
    # smaller, bigger = partition(...)
    # Check the length of <smaller>, and use that to figure out which list
    # to recurse on. You only need to recurse on one!

    if k < 0 or k >= len(lst):
        raise IndexError

    elif len(lst) == 1:
        return lst[0]

    elif len(lst) == 2:
        if k == 0:
            return min(lst[0], lst[1])
        else:
            return max(lst[0], lst[1])

    else:

        pivot = lst[0]

        tup = partition(lst[1:], pivot)

        smaller = tup[0]
        bigger = tup[1]

        if k == 0:
            if len(bigger) == len(lst) - 1:
                return pivot
            else:
                return kth_smallest(smaller, 0)

        else:

            if len(smaller) == k:
                return pivot
            elif len(smaller) > k:
                return kth_smallest(smaller, k)
            else:
                return kth_smallest(bigger, k-len(smaller)-1)


def partition(lst, pivot):
    """Return a partition of <lst> according to pivot.

    Return two lists, where the first is the items in <lst>
    that are <= pivot, and the second is the items in <lst>
    that are > pivot.

    @type lst: list
    @type pivot: object
    @rtype: (list, list)
    """
    # Use a loop to go through <lst> to build up the two
    # lists. Note that <smaller> and <bigger> do *not* need to be sorted here.
    smaller = []
    bigger = []

    for item in lst:
        if item > pivot:
            bigger.append(item)
        else:
            smaller.append(item)

    return smaller, bigger


##############################################################################
# Task 2: Something a little different
##############################################################################
# The file of English words to use. The one we've provided doesn't contain
# plural forms. Assume this list is in alphabetical order.
FILE = 'dict.txt'
LETTERS = 'abcdefghijklmnopqrstuvwxyz'


def anagrams(phrase):
    """Return a list of all anagrams of <phrase>.

    The anagrams are returned in alphabetical order.

    @type phrase: str
    @rtype: list[str]
    """
    # variables. This is particularly useful to see how the letter frequencies
    # are being represented.
    words = _generate_word_list()
    letter_count = _generate_letter_count(phrase.lower())
    return _anagrams_helper(words, letter_count)


def _generate_word_list():
    """Read in English words from <FILE> and return them.

    The returned list is in alphabetical order.

    @rtype: list[str]
    """
    words = []
    with open(FILE) as f:
        for line in f.readlines():
            words.append(line.strip().lower())
    return words


def _generate_letter_count(phrase):
    """Return a dictionary counting the letter occurrences in <string>.

    All letters in <phrase> are converted to lower-case.
    The keys in the returned dictionary are the 26 lower-case letters,
    'a', 'b', 'c', etc.

    Precondition: <phrase> contains only letters.

    @type phrase: str
    @rtype: dict[str, int]
    """
    lower = phrase.lower()
    letter_count = {}
    for char in LETTERS:
        letter_count[char] = lower.count(char)
    return letter_count


def _anagrams_helper(words, letter_count):
    """Return all the anagrams using the given letters and allowed words.

    Each anagram must use all the letters, with correct occurrences, given by
    <letter_count>, and must use only the words appearing in <words>.

    Note: we're using a helper function here so that you don't need to
    recompute <words> for each recursive call.

    The anagrams are returned in alphabetical order.

    Preconditions:
    - letter_count has 26 keys (one per lowercase letter),
      and each value is a non-negative integer.

    @type words: list[str]
    @type letter_count: dict[str, int]
    @rtype: list[str]
    """
    anagrams_list = []

    # 1. Base case - no more letters in <letter_count>.
    # In this case, there is only one valid anagram: the empty string.
    if _check_empty(letter_count):
        return ['']

    for word in words:
        # 2. For each word, check whether it can be used with the given
        # letter count. (If not, go onto the next word.)
        if not _within_letter_count(word, letter_count):
            continue

        # 3. If the word can be used, recurse and create anagrams.
        #  (i) Create a new dictionary that has the same values as letter_count,
        #      except with counts decreased based on the letters in <word>.
        #      Look at how we implemented _generate_letter_count for guidance.
        #  (ii) Call _anagrams_helper recursively with the new, reduced
        #       letter count.
        #  (iii) Combine <word> with the result of the recursive call to update
        #        <anagrams_list> with the anagrams that start with <word>.
        #        Don't forget to separate the words with a space.

        new_lettter_count = dict()

        for key in letter_count:
            new_lettter_count[key] = letter_count[key] - word.count(key)

        result = _anagrams_helper(words, new_lettter_count)

        if result != []:
            for item in result:
                word += " " + item

        if _check_anagram(word, letter_count):
            word = word.strip()
            anagrams_list.append(word)

    # 4. Return the anagrams that can be made by the letters in letter_count.
    return anagrams_list


def _check_anagram(word, letter_count):
    """Return wether the word is an anagram based on the letter count
    @type letter_count: dict[str, int]
    @type word: str
    @rtype bool
    """
    sum_ = 0
    for key in letter_count:
        sum_ += letter_count[key]

    return sum_ == len(word.replace(" ", ""))


def _within_letter_count(word, letter_count):
    """Return whether <word> can be made using letters in <letter_count>."""
    for char in LETTERS:
        if word.count(char) > letter_count[char]:
            return False
    return True


def _check_empty(letter_count):
    """check if letter count does not have anymore words
      @type letter_count: dict[str, int]
      """
    for key in letter_count:
        if letter_count[key] != 0:
            return False

    return True


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config='pylintrc.txt')
