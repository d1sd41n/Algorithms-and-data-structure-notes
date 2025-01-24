# Return Kth to Last

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


# solution #1
# def kth_to_last(ll, k):
#     node = ll.head
#     values = []

#     for node in custom_linked_list:
#         values.append(node.value)

#     return values[-k]

# print(kth_to_last(custom_linked_list, 3))


# solution #2
def kth_to_last(ll, k):
    pointer_1 = ll.head
    pointer_2 = ll.head

    counter = 0
    return_value = False

    while pointer_1:
        pointer_1 = pointer_1.next

        if counter >= k:
            pointer_2 = pointer_2.next
            return_value = True

        counter += 1

    return pointer_2.value if return_value else None


print(kth_to_last(custom_linked_list, 4))
