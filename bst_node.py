class BSTNode:
    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if self.val is None:
            self.val = val
            return
        if self.val == val:
            return
        if val < self.val and self.left is None:
            self.left = BSTNode(val)
            return
        if val < self.val and self.left is not None:
            self.left.insert(val)
            return
        if val > self.val and self.right is None:
            self.right = BSTNode(val)
            return
        if val > self.val and self.right is not None:
            self.right.insert(val)
            return

    def get_min(self):
        return self.val if self.left is None else self.left.get_min()

    def get_max(self):
        return self.val if self.right is None else self.right.get_max()
