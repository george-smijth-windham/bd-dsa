from node import Node


class LinkedList:
    def add_to_head(self, node):
        head = self.head
        node.set_next(head)
        self.head = node

    def add_to_tail(self, node):
        if None == self.head:
            self.head = node
            return
        tail = None
        for _node in self:
            tail = _node
        tail.set_next(node)

    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)
