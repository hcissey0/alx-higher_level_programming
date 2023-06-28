#!/usr/bin/python3
"""Defines a singly linked list node"""


class Node:
    """
    A Node of a singly linked list

    Attributes:
        head (Node): The head node of the linked list.
    """
    def __init__(self, data, next_node=None):
        """
        The instantiator of the Node

        Args:
            data (int): the element of the node
            next_node (Node): pointer to the next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        The data getter

        Returns:
            The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        The setter for the data

        Args:
            value (int): the value of the data

        Raises:
            TypeError: when value is not an integer

        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        The getter for the next_node

        Returns:
            The next node in the linked list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        The setter for the next_node

        Args:
            value (Node): the pointer to the next node
        Returns:
            None
        Raises:
            TypeError: when value is not a Node or None
        """
        if not isinstance(value, Node) or value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""Defines a singly liked list"""


class SinglyLinkedList:
    """
    Singly linked list

    Attributes:
        head (Node): The head of the list
    """
    def __init__(self):
        """
        The instantiator
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new node in the correct position

        Args:
            value (int): The element of the list

        Returns:
            None
        """
        tmp = Node(value)
        cnode = self.__head
        if self.__head is None or value < self.__head.data:
            tmp.next_node = self.__head
            self.__head = tmp
            return
        else:
            cnode = self.__head
        while cnode.next_node is not None and value >= cnode.next_node.data:
            cnode = cnode.next_node
        tmp.next_node = cnode.next_node
        cnode.next_node = tmp

    def __str__(self):
        """
        Prints the entire linked list

        Returns:
            A representation of the linked list
        """
        if self.__head is None:
            return ""
        cnode = self.__head
        res = str(cnode.data) + "\n"
        while cnode.next_node is not None:
            cnode = cnode.next_node
            res += str(cnode.data) + "\n"
        return res
