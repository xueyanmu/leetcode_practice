class Node:
    def __init__(self, data: int):
        self.next = None
        self.data = data

    def insertBefore(self, list, data):
        node = Node(data)
        if list is not None:
            node.next = list
        return node

    def padList(self, l, padding):
        self.head = l
        for i in range(len(0, padding)):
            self.head = self.insertBefore(self.head, 0)
        return self.head


class LinkedList:
    def __init__(self):
        self.head = None

    def append_to_tail(self, d: int):
        end = Node(d)
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = end

    def delete_node(self, d: int):
        """
        most important notes in delete_node:
            check for null pointer
            update head or tail pointer as necessary

        :param d:
        :return:
        """
        if self.head is None:
            return None

        n = self.head

        # moved head
        if n.data == d:
            return self.head.next

        while n.next is not None:
            if n.next.data == d:
                n.next = n.next.next
                # head didn't change
                return self.head

            n = n.next
        return self.head
