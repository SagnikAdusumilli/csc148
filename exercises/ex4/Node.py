class Node:

    def __init__(self, Data):
        self._data = Data
        self.next = None

    def add(self, Oject):
        if self._data is None:
            self._data = Oject
            return None
        if self.next is None:
            self.next = Node(Oject)
            return None
        node = self.next
        while node.next is not None:
            node = node.next

        node.next = Node(Oject)

    def is_none(self):
        return self._data is None

    def __str__(self):
        return str(self._data)



class LinkedList:

    def __init__(self):
     self._head = Node(None)

    def add(self, object):
        self._head.add(object)

    def __str__(self):

        pointer = self._head
        list = []
        while pointer is not None:
            list.append(pointer.__str__())
            pointer = pointer.next

        return list.__str__()

    def deqeue(self):
        Node = self._head
        self._head = self._head.next
        return Node


if __name__ == '__main__':

    list = LinkedList()

    list.add(6)
    list.add(7)
    list.add(8)
    list.add(11)

    print(list)

    print(list.deqeue())
    print(list.deqeue())

    print(list)
