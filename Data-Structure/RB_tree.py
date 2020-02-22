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

    def left_rotate(self, current_node):
        y = current_node.right
        current_node.right = y.left
        y.left.p = current_node
        y.p = current_node.p

        if current_node.p == None:
            self.root = y
        elif current_node == current_node.p.left:
            current_node.p.left = y
        else:
            current_node.p.right = y
        y.left = current_node
        current_node.p = y

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node


if __name__ == '__main__':
    node = [10, 85, 15, 70, 20, 60, 30, 50]
