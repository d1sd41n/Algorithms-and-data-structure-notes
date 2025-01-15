# Write a function to remove duplicates from an unsorted linked list. Input 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 4 -> 5 Output 1 -> 2 -> 3 -> 4 -> 5

from random import randint


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current_node = self.head

        while current_node:
            yield current_node

            current_node = current_node.next

    def __str__(self):
        values = [str(x.value) for x in self]

        return " -> ".join(values)

    def __len__(self):
        result = 0

        node = self.head
        while node:
            result += 1
            node = node.next

        return result

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next

        return self.tail

    def generate(self, number, min_value, max_value):
        from random import randint

        self.head = None
        self.tail = None

        for _ in range(number):
            self.add(randint(min_value, max_value))

        return self


custom_linked_list = LinkedList()
custom_linked_list.generate(10, 0, 5)

print(custom_linked_list)
print(len(custom_linked_list))

print("##########################")


def remove_duplicates(ll):
    numbers = []
    nodes = []
    prev = None

    debug = []
    last_non_repeated = ll.head

    for i, node in enumerate(ll):

        if not node.value in numbers:
            numbers.append(node.value)
            nodes.append(node)

            if i == 0:
                continue

            last_non_repeated.next = node
            last_non_repeated = node

    ll.tail = last_non_repeated
    last_non_repeated.next = None

    print(numbers)


remove_duplicates(custom_linked_list)

print(custom_linked_list)
print(len(custom_linked_list))
