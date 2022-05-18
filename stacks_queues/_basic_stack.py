from aifc import Error


class StackNode:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def pop(self):
        t = self.top
        if t is None:
            return Error

        item = t.data
        self.top = t.next
        return item

    def push(self, item):
        t = StackNode(item)
        t.next = self.top
        self.top = t

    def peek(self):
        if self.top is None:
            return Error
        return self.top.data

    def is_empty(self):
        return self.top is None
