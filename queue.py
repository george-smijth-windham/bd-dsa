class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items = [item] + self.items

    def pop(self):
        return None if self.size() == 0 else self.items.pop()

    def peek(self):
        return None if self.size() == 0 else self.items[-1]

    def size(self):
        return len(self.items)
