class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(self.root, new_node)

    def _insert(self, current_node, new_node):
        if current_node.data < new_node.data:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert(current_node.right, new_node)
        else:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert(current_node.left, new_node)

    def search(self, target):
        if self.root.data == target:
            return self.root.data
        else:
            return self._search(self.root, target)

    def _search(self, current_node, target):
        if current_node.data < target:
            if current_node.right.data == target:
                return current_node.right.data
            else:
                self._search(current_node.right, target)
        else:
            if current_node.left.data == target:
                return current_node.left.data
            else:
                self._search(current_node.left, target)

    def delete(self, remove_target):
        if self.root == remove_target:
            del self.root
            # 루트 노드가 지워지면 왼, 오 자식노드에서 루트로 올라와야함
            # if current_node.left.data < current_node.right.data:
            #     self.root = current_node.left
            # else:
            #     self.root = current_node.right
            return 'remove the node'
        else:
            return self._delete(self.root, remove_target)

    def _delete(self, current_node, remove_target):
        if current_node.data < remove_target:  # 자식노드가 없을 때
            if current_node.right.data == remove_target:
                self.root.right = None
        else:
            if current_node.left.data == remove_target:
                self.root.left = None
        # 자식노드가 있을 때


if __name__ == '__main__':

    BT = BinaryTree()

    BT.insert(2)
    BT.insert(1)
    BT.insert(3)

    print(BT.root.data)
    print(BT.root.left.data)
    print(BT.root.right.data)

    BT.search(1)
    BT.search(2)
    BT.search(3)

    print(BT.search(3))
    print(BT.search(1))
    print(BT.search(2))

    BT.delete(2)
    print(BT.delete(2))