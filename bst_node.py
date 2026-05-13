class BSTNode:
    def height(self):
        if self.val is None:
            return 0
        left = right = 0
        if self.left is not None:
            left = self.left.height()
        if self.right is not None:
            right = self.right.height()
        return max(left, right) + 1

    def exists(self, val):
        if self.val is not None:
            if self.val < val:
                if self.right is not None:
                    return self.right.exists(val)
                return False
            if self.val > val:
                if self.left is not None:
                    return self.left.exists(val)
                return False
            return True
        return False

    def delete(self, val):
        if self.val is None:
            return None
        if val < self.val:
            if self.left is not None:
                self.left = self.left.delete(val)
                return self
        if val > self.val:
            if self.right is not None:
                self.right = self.right.delete(val)
                return self
        if self.left is None:
            return self.right
        if self.right is None:
            return self.left
        right = self.right
        successor = right.get_min()
        self.val = successor
        self.right = self.right.delete(successor)
        return self

    def inorder(self, visited):
        if self.left is not None:
            self.left.inorder(visited)
        if self.val is not None:
            visited.append(self.val)
        if self.right is not None:
            self.right.inorder(visited)
        return visited

    def preorder(self, visited):
        if self.val is not None:
            visited.append(self.val)
        if self.left is not None:
            visited.extend(self.left.preorder([]))
        if self.right is not None:
            visited.extend(self.right.preorder([]))
        return visited

    def postorder(self, visited):
        if self.left is not None:
            self.left.postorder(visited)
        if self.right is not None:
            self.right.postorder(visited)
        if self.val is not None:
            visited.append(self.val)
        return visited

    # don't touch below this line

    def __init__(self, val=None):
        self.left = None
        self.right = None
        self.val = val

    def insert(self, val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = BSTNode(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = BSTNode(val)

    def get_min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current.val

    def get_max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current.val
