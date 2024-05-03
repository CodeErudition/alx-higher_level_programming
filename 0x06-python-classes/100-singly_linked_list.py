#!/usr/bin/python3
"""This module defines classes for a singly linked list."""


class Node:
    """
    This class represents a node of a singly linked list.

    Attributes:
        __data (int): The data stored in the node (private).
        __next_node (Node): The reference to the next node in the
            list (private).
    """
    def __init__(self, data, next_node=None):
        """
        Initializes a Node object with data and optional next_node.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional): The reference to the next node.
                Defaults to None.

        Raises:
            TypeError: If data is not an integer or next_node is not a
                Node object.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """int: The data stored in the node (getter)."""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the data stored in the node.

        Args:
            value (int): The new data to be stored in the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Node: The reference to the next node (getter)."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the reference to the next node.

        Args:
            value (Node): The new reference to the next node.

        Raises:
            TypeError: If value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class represents a singly linked list.

    Attributes:
        head: The head node of the list.
    """
    def __init__(self):
        """Initializes an empty singly linked list."""
        self.head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the correct sorted position in the
            list (increasing order).

        Args:
            value (int): The data value to be inserted into the list.
        """
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while (current.next_node is not None and
                    current.next_node.data < value):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Returns a string representation of the linked list."""
        result = ""
        current = self.head
        while current is not None:
            result += str(current.data) + "\n"
            current = current.next_node
        return result
