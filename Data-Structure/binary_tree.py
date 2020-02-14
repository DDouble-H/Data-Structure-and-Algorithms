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
        if current_node.data is None:
            print('Not found')
        elif current_node.data < target:
            if current_node.right.data == target:
                return current_node.right.data
            else:
                self._search(current_node.right, target)
        else:
            if current_node.left.data == target:
                return current_node.left.data
            else:
                self._search(current_node.left, target)

    def preorder(self, current_node):
        if current_node is None:
            return None
        else:
            print(current_node.data, end='->')
            self.preorder(current_node.left)
            self.preorder(current_node.right)

    def inorder(self, current_node):
        if current_node is None:
            return None
        else:
            self.inorder(current_node.left)
            print(current_node.data, end='->')
            self.inorder(current_node.right)

    def postorder(self, current_node):
        if current_node is None:
            return None
        else:
            self.postorder(current_node.left)
            self.postorder(current_node.right)
            print(current_node.data, end='->')

    def delete(self, remove_target):
        self.root, deleted =  self._delete(self.root, remove_target)  # 삭제여부 확인(True : 삭제, False)
        return deleted

    def _delete(self, current_node, remove_target):
        deleted = False

        # i) 데이터가 없을 때
        if current_node is None:
            return current_node, deleted

        # ii) 데이터와 타겟이 동일할 때 (삭제부분)
        # data 가 둘 다 없을 때, 둘 중에 하나만 있을 때, 둘 다 있을 때
        if current_node.data == remove_target:

            if current_node.left is None and current_node.right is None:  # left, right 둘 다 없을 때
                current_node = None

            elif current_node.left is None and current_node.right is not None:  # L, R 둘 중에 하나만 있을 때
                # 삭제할 노드의 오른쪽의 제일 작은 값이 위치, 노드끼리 연결
                current_node = current_node.right

            elif current_node.left is not None and current_node.right is None:
                current_node = current_node.left

            else:  # L, R 둘 다 있을 때 ## 트리 오른쪽위치에서 최솟값을 가지고 오고, 부모와 자식을 연결해줌

                parent, child = current_node, current_node.right  # 오른쪽이라고 방향만 지정

                while child.left is not None:
                    parent, child = child, child.left  # 최솟값을 찾는 과정

                child.left = current_node.left  # 이전 노드의 자식과 현재 노드를 연결

                if parent != current_node:
                    parent.left = child.right
                    child.right = current_node.right

                current_node = child

        # iii) 데이터가 타겟과 다를 때
        elif current_node.data > remove_target:
            current_node.left, deleted = self._delete(current_node.left, remove_target)

        else:
            current_node.right, deleted = self._delete(current_node.right, remove_target)

        return current_node, deleted


if __name__ == '__main__':
    import random
    node = [random.randrange(1, 10) for i in range(10)]

    node = []
    while len(node) != 10:
        node.append(random.randint(1,20))
        node = list(set(node))

    random.shuffle(node)

    node = [3, 16, 20, 5, 8, 17, 1, 10, 11, 9] # 재현성을 위한 값 고정
    BT = BinaryTree()

    for num in node:
        BT.insert(num)

    print(BT.search(10))

    BT.preorder(BT.root)
    print()
    BT.inorder(BT.root)
    print()
    BT.postorder(BT.root)
    print()

    print('삭제전')
    BT.preorder(BT.root)
    print()
    BT.delete(17)
    print('삭제후')
    BT.preorder(BT.root)
