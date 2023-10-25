#!/usr/bin/python3
"""Writing something here because it is necessary"""


class Node:
    """Creation of a singly_linked list"""

    def __init__(self, data, next_node=None):
        """Instance of a node. Instantiated.

        Attributes:
            data: value of current node.
            next_node: the next linked node.
        """

        if type(data) != int:
            raise TypeError("data must be an integer")
        if next_node is not None and type(next_node) != Node:
            raise TypeError("next_node must be a Node object")

        self._Node__data = data
        self._Node__next_node = next_node

    @property
    def data(self):
        """Returns the value of a node"""

        return (self._Node__data)

    @data.setter
    def data(self, value):
        """Sets or modifies the value of a node.

        Attributes:
            value: the new value the node is to be set to
        """

        if type(value) != int:
            raise TypeError("data must be an integer")

        self._Node__data = value
        return (value)

    @property
    def next_node(self):
        """Returns the next node the current node points to"""

        return (self._Node__next_node)

    @next_node.setter
    def next_node(self, value):
        """Modifies where the current node points to.

        Attributes:
            value: the node being pointed to, or None.
        """

        if value is not None and type(value) != Node:
            raise TypeError("next_node must be a Node object")

        self._Node__next_node = value
        return (value)


class SinglyLinkedList:
    """Creates a singly linked list"""

    def __init__(self):
        """Instance of a singly linked list"""

        self._SingleLinkedList__head = None

    def sorted_insert(self, value):
        """Inserts a new Node, in the right order (increasing).

        Attributes:
            value: value of the new node to be added.
        """

        node = Node(value, None)
        head = self._SingleLinkedList__head
        prev = None

        if (head is None):
            self._SingleLinkedList__head = node
            return (node)

        if (node.data < head.data):
            node.next_node = head
            self._SingleLinkedList__head = node
            return (node)

        while (head is not None):
            if (node.data < head.data):
                node.next_node = head
                prev.next_node = node
                return (node)

            prev = head
            head = head.next_node
            if (head is None):
                prev.next_node = node

        return (node)

    def __repr__(self):
        """Prints out a singly linked list"""

        head = self._SingleLinkedList__head
        print_arr = []
        while (head is not None):
            print_arr.append("{:d}".format(head.data))
            head = head.next_node

        return ("\n".join(print_arr))
