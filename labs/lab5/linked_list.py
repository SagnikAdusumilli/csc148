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

    def __eq__(self, other):
        """""
        @type other: Object
        @rtype: bool
        """
        if other == self._data:
            return True
        else:
            return False



class LinkedList:

    def __init__(self):
     self._head = Node(None)
     self._len = 0

    def add(self, object):
        self._head.add(object)
        self._len += 1

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
        self._len -= 1
        return Node

    def delete_index(self, index):

        if index == 0:
            self.deqeue()
            return None

        count =0
        curr = self._head

        while curr.next is not None and count< index-1:
            count += 1
            curr = curr.next

        saved_Node = curr.next.next

        curr.next = saved_Node

    def delete_item(self, item):

        curr = self._head

        if curr._data is item:
            self._head = curr.next
            return None

        while curr is not None and curr.next != item:
            curr = curr.next

        if curr is not None:
            saved_node = curr.next.next
            curr.next = saved_node


if __name__ == '__main__':

    list = LinkedList()

    list.add(6)
    list.add(7)
    list.add(8)
    list.add(11)

    print(list)

    list.delete_item(8)

    print(list)
