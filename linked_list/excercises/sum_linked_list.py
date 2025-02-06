# Interview Questions - 4 : Sum Lists

# You have two numbers represented by a linked list, where each node contains a single digit.
# The digits are stored in reverse order, such that the 1's digit is at the head of the list.
# Write a function that adds the two numbers and returns the sum as a linked list.


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

        return "".join(values)

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


custom_linked_list_1 = LinkedList()
custom_linked_list_1.generate(5, 1, 9)

print(custom_linked_list_1)

custom_linked_list_2 = LinkedList()
custom_linked_list_2.generate(3, 1, 9)

print(custom_linked_list_2)

sum_ll = int(str(custom_linked_list_1)[::-1]) + int(str(custom_linked_list_2)[::-1])

print(f"sum: {sum_ll}")
print("---------------------")


# Solution #1
def sum_list(ll_a, ll_b):
    node_a = ll_a.head
    node_b = ll_b.head

    residue = 0
    sum_all = 0

    units = []

    sum_ll = LinkedList()

    while node_a or node_b:

        node_a_value = node_a.value if node_a else 0
        node_b_value = node_b.value if node_b else 0

        print(node_a_value, node_b_value)

        sum_nodes = node_a_value + node_b_value + residue

        residue = sum_nodes // 10
        unit = sum_nodes % 10

        units.append(unit)
        sum_ll.add(unit)

        node_a = node_a.next if node_a else None
        node_b = node_b.next if node_b else None

    if residue != 0:
        units.append(residue)
        sum_ll.add(residue)

    print(units)

    if unit == 0:
        current_node = sum_ll.head
        while current_node.next != sum_ll.tail:
            current_node = current_node.next

        current_node.next = None
        sum_ll.tail = current_node

    return sum_ll


custom_linked_list_3 = sum_list(custom_linked_list_1, custom_linked_list_2)
print(custom_linked_list_3)
