class DoubleLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        """Append a new node with the given data to the end of the list."""
        new_node = DoubleLinkedListNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        """Prepend a new node with the given data to the beginning of the list."""
        new_node = DoubleLinkedListNode(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, node):
        """Delete the given node from the list."""
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif node == self.head:
            self.head = node.next
            node.next.prev = None
        elif node == self.tail:
            self.tail = node.prev
            node.prev.next = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev

    def find(self, data):
        """Find the first node with the given data and return it, or return None if not found."""
        current_node = self.head
        while current_node is not None:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return None

    def print_list(self):
        """Print the contents of the list from head to tail."""
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

# Create a new double-linked list
dl_list = DoubleLinkedList()

# Append some nodes to the list
dl_list.append(1)
dl_list.append(2)
dl_list.append(3)

# Prepend a node to the list
dl_list.prepend(0)

# Find a node in the list
node = dl_list.find(2)

# Delete the node from the list
dl_list.delete(node)

# Print the contents of the list
dl_list.print_list()  # Output: 0 1 3
