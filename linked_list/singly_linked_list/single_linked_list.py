class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        # This method allows the linked list to be used in a for loop
        # It yields each node in the list in turn
        node = self.head

        while node:
            yield node
            node = node.next
    
    def insert(self, value, location):
        # This method inserts a new node with the given value at the specified location in the list
        # import pdb; pdb.set_trace()
        new_node = Node(value)
        if self.head is None:
            # If the list is empty, the new node becomes the head and the tail
            self.head = new_node
            self.tail = new_node
        else:
            if location == 0:
                # If the location is 0, the new node becomes the new head of the list
                new_node.next = self.head
                self.head = new_node
            elif location == -1:
                # If the location is 1, the new node becomes the new tail of the list
                new_node.next = None
                self.tail.next = new_node
                self.tail = new_node
            else:
                # For locations other than 0 or 1, the new node is inserted in between two existing nodes
                current_node = self.head
                for i in range(location - 1):
                    current_node = current_node.next
                new_node.next = current_node.next
                current_node.next = new_node

                if id(self.tail) == id(current_node):
                    self.tail = new_node

    def traverse(self):
        # This method prints the value of each node in the list
        if self.head is None:
            print("no hay linked list")
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def search(self, node_value):
        # This method searches the list for a node with the given value and returns it if found
        if self.head is None:
            print("no hay linked list")
        else:
            node = self.head
            while node is not None:
                if node.value == node_value:
                    return node.value
                node = node.next
            return "no existe el valor en la linked list"
    
    def delete_node(self, location):
        # This method deletes a node at the specified location in the list
        if self.head is None:
            print("no hay linked")
        else:
            if location == 0:
                # If the location is 0, the head is deleted
                if self.head == self.tail:
                    # If there is only one node in the list, both the head and tail are set to None
                    self.head = None
                    self.tail = None
                else:
                    # If there are multiple nodes, the second node becomes the new head
                    self.head = self.head.next
            elif location == -1:
                # If the location is -1, the tail is deleted
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    # If there are multiple nodes, the node before the tail becomes the new tail
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                # For locations other than 0 or -1, the node at the specified location is deleted
                temp_node = self.head
                index = 0
                while index < location - 1:
                    temp_node = temp_node.next
                    index += 1
                next_node = temp_node.next
                temp_node.next = next_node.next


    def delete_entire(self):
        # This method deletes the entire linked list by setting the head and tail to None
        if self.head is None:
            print("no hay liked list")
        else:
            self.head = None
            self.tail = None


single_linked_list = SingleLinkedList()

single_linked_list.insert(1, 1)

single_linked_list.insert(2, 1)
single_linked_list.insert(3, 1)
single_linked_list.insert(4, -1)
single_linked_list.insert(0, 0)
single_linked_list.insert(666, 3)
single_linked_list.insert(555, -1)


print([node.value for node in single_linked_list])
# single_linked_list.traverseSLL()

print("---")
single_linked_list.delete_node(0)
print([node.value for node in single_linked_list])




# print([node.value for node in self])