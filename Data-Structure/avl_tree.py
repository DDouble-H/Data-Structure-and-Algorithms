class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class AVL:
    def __init__(self):
        self.root = None
        self.node = None
        self.height = -1
        self.balance = 0

    def height(self):
        if self.node is None:
            return 0
        else:
            return self.node.height

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def _insert(self, node, data, new_node):
        if node < new_node.data:
            self.node.left.insert(data)
        else:
            self.node.right.insert(data)
