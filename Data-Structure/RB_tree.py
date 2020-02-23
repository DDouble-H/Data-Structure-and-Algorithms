class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.p = None
        self.color = True  # True : Red, False: Black


class RB:
    def __init__(self):
        self.root = None
        self.nil = None

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        y.right.p = x
        x.p = y.p
        if x.p is self.nil:
            y = self.root
        elif x == x.p.right:
            y = x.p.left
        else:
            y = x.p.right

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        y.left.p = x
        x.p = y.p
        if x.p is self.nil:
            y = self.root
        elif x == x.p.left:
            y = x.p.right
        else:
            y = x.p.left

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def _insert(self, new_node):
        y = self.nil
        x = self.root
        while x is not self.nil:
            y = x
            if new_node.data < x.data:
                x = x.left
            else:
                y = y.right
            new_node.p = y
        if y is None: #mean is empty tree
            self.root = new_node
        elif new_node.data < y.data:
            y.left = new_node
        else:
            y.right = new_node
        new_node.left and new_node.right is None
        new_node.color = True
        self._insert_fix(self, new_node)

    def _insert_fix(self, new_node):
        pass


if __name__ == '__main__':
    node = [10, 85, 15, 70, 20, 60, 30, 50]
