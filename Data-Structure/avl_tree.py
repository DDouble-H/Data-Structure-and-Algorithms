class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = -1
        self.balance = 0


class AVL:
    def __init__(self):
        self.root = None

    def height(self):
        if self.current_node is None:
            return 0
        else:
            return self.current_node.height

    def balance_factor(self, current_node):
        return self.height(current_node.left) - self.height(current_node.right)

    def balance(self, current_node):
        if self.balance_factor(current_node) > 1:
            self.LL(current_node)
        if self.balance_factor(current_node) < -1:
            self.RR(current_node)

    def update_height(self, current_node):
        if current_node.left is not None:
            current_node.left.height += 1
        elif current_node.right is not None:
            current_node.right.height += 1
        else:
            current_node.left.height += 1
            current_node.right.height += 1

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def _insert(self, current_node, data, new_node):
        if current_node.data < new_node.data:
            self.current_node.left.insert(data)
            self.update_height(current_node.left)
        else:
            self.current_node.right.insert(data)
            self.update_height(current_node.right)

    def delete(self, remove_target):
        self.root, deleted = self._delete(self.root, remove_target)
        return deleted

    def _delete(self, current_node, remove_target):
        deleted = False

        if current_node is None:
            return current_node, deleted
        if current_node.data == remove_target:
            pass
        elif current_node.data > remove_target:
            current_node.left, deleted = self._delete(current_node.left, remove_target)
        else:
            current_node.right, deleted = self._delete(current_node.right, remove_target)
        return current_node, deleted

    def LL(self, current_node):
        x = current_node.left
        current_node.left = x.right
        x.right = current_node

    def RR(self, current_node):
        x = current_node.right
        current_node.right = x.left
        x.left = current_node


if __name__ == '__main__':
    node = [12, 8, 18, 17, 11, 5, 4]