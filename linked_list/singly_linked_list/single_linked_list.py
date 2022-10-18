class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None


class SingleLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

single_linked_list = SingleLinkedList()

node_1 = Node(1)
node_2 = Node(2)

single_linked_list.head = node_1
single_linked_list.head.next = node_2
single_linked_list.tail = node_2
