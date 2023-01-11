class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self, node_value=None):
        self.head = Node(node_value)
        self.tail = self.head

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert_node(self, node_value, location):
        new_node = Node(node_value)
        if location == 0:
            self.prepend(node_value)
        elif location == -1:
            self.append(node_value)
        else:
            index = 0
            for node in self:
                if index == location:
                    prev_node = node.prev
                    new_node.prev = prev_node
                    new_node.next = node
                    prev_node.next = new_node
                    node.prev = new_node
                    break
                index += 1
            else:
                # Node was not inserted, so append it to the end of the list
                self.append(node_value)

    def prepend(self, node_value):
        """Prepend a new node with the given data to the beginning of the list."""
        new_node = Node(node_value)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def append(self, node_value):
        """Append a new node with the given data to the end of the list."""
        new_node = Node(node_value)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
    
    def traverse_ll(self):
        for node in self:
            print(node.value)

    def reverse_traverse_ll(self):
        node = self.tail
        while node:
            print(node.value)
            node = node.prev

    def search_node(self, value):
        for i, node in enumerate(self):
            if value == node.value:
                return i
        return None
    
    def delete_entire_ll(self):
        self.head = None
        self.tail = None
    
    def delete_node(self, index):
        if index == 0:
            if self.head == self.tail:
                self.delete_entire_ll()
                return
            self.head = self.head.next
            self.head.prev = None
            return

        if index == -1:
            if self.head == self.tail:
                self.delete_entire_ll()
                return
            self.tail = self.tail.prev
            self.tail.prev = None
            return

        for i, node in enumerate(self):
            pass
        

                


double_ll = DoubleLinkedList(1)


print([node.value for node in double_ll])

double_ll.insert_node(0, 0)


double_ll.insert_node(2, -1)
double_ll.insert_node(3, -1)


print([node.value for node in double_ll])


double_ll.insert_node(55, 5)
double_ll.insert_node(777, 1)

print([node.value for node in double_ll])
print("-"*10)

# double_ll.traverse_ll()
# print("-"*10)
print(double_ll.search_node(777))

