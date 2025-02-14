# Write code to partition a linked list around a value x, such that all nodes less than x come before all nodes greater than or equal to x.


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
custom_linked_list.generate(10, 0, 20)

print(custom_linked_list)


# Solution #1

# def partition(ll, x):
#     new_head = None
#     second_head = None

#     previous_head = False
#     previous_tail = False

#     for node in ll:

#         if node.value < x:
#             if not previous_head:
#                 previous_head = node
#                 new_head = node
#             else:
#                 previous_head.next = node
#                 previous_head = node
#         else:
#             if not previous_tail:
#                 previous_tail = node
#                 second_head = node
#             else:
#                 previous_tail.next = node
#                 previous_tail = node

#     ll.head = new_head
#     previous_head.next = second_head
#     previous_tail.next = None
#     ll.tail = previous_tail


# Solution #2
# def partition(ll, x):
#     dummy_head = Node(0)
#     dummy_tail = Node(0)

#     left = dummy_head
#     right = dummy_tail

#     for node in ll:

#         if node.value < x:
#             left.next = node
#             left = node
#         else:
#             right.next = node
#             right = node


#     ll.head = dummy_head.next
#     left.next = dummy_tail.next

#     ll.tail = right
#     right.next = None

# partition(custom_linked_list, 10)

# print(custom_linked_list)

# solution 3
def partition(ll, x):
    node = ll.head
    ll.tail = ll.head

    while node:
        next_node = node.next
        node.next = None

        if node.value < x:
            node.next = ll.head
            ll.head = node
        else:
            ll.tail.next = node
            ll.tail = node

        # print(node.value)
        node = next_node

    ll.tail.next = None
        # node.next = None

        # node = next_node


partition(custom_linked_list, 10)

print(custom_linked_list)
