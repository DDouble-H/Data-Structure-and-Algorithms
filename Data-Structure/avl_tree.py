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

    def delete(self, remove_target):
        self.root, deleted = self._delete(self.root, remove_target)  # 삭제여부 확인(True : 삭제, False)
        return deleted

    def _delete(self, node, remove_target):
        deleted = False

        if node is None:
            return node, deleted

        if node.data == remove_target:
            pass

        elif node.data > remove_target:
            node.left, deleted = self._delete(node.left, remove_target)

        else:
            node.right, deleted = self._delete(node.right, remove_target)

        return node, deleted


if __name__ == '__main__':
    node = [12, 8, 18, 17, 11, 5, 4]