"""Defines Linked List data structure.

The data structure that represents a sequence of nodes. Might be singly linked or
doubly linked.
a -> b -> c -> d

  Typical usage example:

  foo = LinkedList()
  foo.add('a')
  foo.add('b')

  >> foo
     ['a', 'b']
"""

class Node:
    """Singly linked list node.

    Holds the actual value of the node, and the reference to the next node.
    If node is the last one, next will be None.

    Attributes:
        value: Node value.
        next: Next node.
    """

    def __init__(self, value = None, next = None):
        """Initializes Node class with default values.

        Args:
          value:
            Optional; Linked List Node value.
          next:
            Optional; reference to the next Linked List Node;

        Returns:
          A new instance of the Linked List Node.
        """
        self.value = value
        self.next = next

    def __str__(self):
        """Creates string representation of the Node.

        Returns:
          String representation of the node.
        """
        next_str = "Node" if self.next else "None"
        return f"Node(value = {self.value}, next = {next_str})"

class LinkedList:
    """Singly Linked List.

    Represents Singly linked list. Contains reference to the list head and
    number of items.

    Attributes:
        head: First node of the Linked List.
        tail: Last node of the Linked List.
    """

    def __init__(self):
        """Creates Emply Linked List"""
        self.head = None
        self.tail = None
        self._length = 0

    def __str__(self):
        """Creates string representation of the list

        Prints the list in the following format:
          (A) -> (B) -> (C)

        Returns:
          String representation of the list.
        """
        node = self.head
        output = str(node.value)
        while node.next != None:
            node = node.next
            output += f" -> {str(node.value)}"
        return output

    def __len__(self):
        """Length of the list.

        Returns:
          Number of items in list.
        """
        return self._length

    def add_last(self, value):
        """Inserts new node at the end of the list

        Creates node udpates tails, _length and head if required

        Args:
          value:
            Linked List Node value.
        """
        node = Node(value, None)
        if self.tail == None:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            self.tail = node
        self._length += 1

    def add_first(self, value):
        """Inserts new node at the beginning of the list.

        Creates node, updates head length and tail if required.

        Args:
          value:
            Linked List Node value.
        """
        node = Node(value, self.head)
        self.head = node
        if self.tail == None:
            self.tail = self.head
        self._length += 1

    def add_at(self, value, position: int):
        """Inserts new node at specific position.

        Args:
          value: Node value
          position:New node position

        Rises:
          IndexError: position is out of the list range.
        """
        new = Node(value)
        if position > self._length:
            raise IndexError("Position is out of the list range")
        self._length += 1
        if position == 0:
            new.next = self.head
            self.head = new
        node = self.head
        index = 0
        while node != None:
            if index + 1 == position:
                new.next = node.next
                node.next = new
                break
            node = node.next
            index += 1
        if new.next == None:
            self.tail = new

    def first(self):
        """Retrieves the first element of the Linked List.

        Returns:
          Value of the first node or None for empty list.
        """
        return self.head.value if self.head else None

    def last(self):
        """Retrieves the last element of the linked list.

        Returns:
          Value of the last node or none for empty list.
        """
        return self.tail.value if self.tail else None

    def __getitem__(self, key):
        """Retreives element at the specific position

        Args:
          key: item position

        Returns:
          element at postion

        Raises:
          IndexError: position is out of the list range.
        """
        if key < 0 or key >= len(self):
            raise IndexError("key is out of range")
        if key == 0:
            return self.first()
        if key == len(self) - 1:
            return self.last()
        node = self.head
        index = 0
        while node != None:
            if index == key:
                return node.value
            node = node.next
            index += 1

    def delete_first(self):
        """Removes first element form list

        Set the value of the head to head.next.

        Returns:
          Value of deleted node or None for empty list.
        """
        value = self.head.value if self.head else None
        self.head = self.head.next if self.head else None
        if self.head == None:
            self.tail = None
        self._length = self._length - 1 if self._length > 0 else 0
        return value

    def delete_last(self):
        """Removes last element from list.

        Set the tail to previous element. Takes 0(n) time.
        For better performance use Doubly Linked List. Here might
        be optimized if cache before last node.

        Returns:
          Value of the deleted node or None for empty list.
        """
        if self.tail == None:
            return None
        value = self.tail.value if self.tail else None
        node = self.head
        if node.next == None:
            node.next = None
            self.tail = None
            self.head = None
            self._length = 0
            return value
        while node != None:
            next_node = node.next
            if next_node.next == None:
                node.next = None
                self.tail = node
                self._length = self._length - 1 if self._length > 0 else 0
            node = node.next
        return value

    def delete_at(self, position: int):
        """Removes item at specific position.

        Args:
          position: int, position to remove.

        Returns:
          Deleted node value.

        Rises:
          IndexError: position is out of list range.
        """
        if position < 0 or position >= self._length:
            raise IndexError("position is out of list range")
        if position == 0:
            return self.delete_first()
        if position == self._length - 1:
            return self.delete_last()
        node = self.head
        index = 0
        while node != None:
            if index + 1 == position:
                value = node.next.value
                node.next = node.next.next
                self._length -= 1
                return value
            node = node.next
            index += 1

    def remove_dups(self):
        """Removes duplicates from list
        """
        if len(self) == 0:
            return
        node = self.head
        while node != None:
            next_node = node
            while next_node != None:
                if next_node.next != None and node.value == next_node.next.value:
                    next_node.next = next_node.next.next
                    self._length -= 1
                    if next_node.next == None:
                        self.tail = next_node
                next_node = next_node.next
            node = node.next
