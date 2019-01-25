"""Doubly-Linked List Class."""


class Node(object):
    """Node class."""

    def __init__(self, data, prev, next):
        """Init."""
        self.data = data
        self.prev = prev
        self.next = next


class DoubleList(object):
    """Doubly-Linked list class."""

    head = None
    tail = None

    def append(self, data):
        """Add a new node object to the end of the list."""
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node

    def remove(self, node_value):
        """Remove the specified node value."""
        current_node = self.head

        while current_node is not None:
            if current_node.data == node_value:
                # if it's not the first element
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                    current_node.next.prev = current_node.prev
                else:
                    # otherwise we have no prev (it's None), head is the
                    # next one, and prev becomes None
                    self.head = current_node.next
                    current_node.next.prev = None

            current_node = current_node.next

    def show(self):
        """Display the contents of the list."""
        print ('Show list data:', '-' * 34)
        cur = self.head
        while cur is not None:
            prev_val = cur.prev.data if hasattr(cur.prev, 'data') else None
            next_val = cur.next.data if hasattr(cur.next, 'data') else None
            print (prev_val, cur.data, next_val)

            cur = cur.next
        print ('-' * 50)


d = DoubleList()

d.append(5)
d.append(6)
d.append(50)
d.append(30)

d.show()

d.remove(50)
d.remove(5)

d.show()
