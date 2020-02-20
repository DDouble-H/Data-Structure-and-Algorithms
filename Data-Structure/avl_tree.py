class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class AVL:
    def __init__(self):
        self.root = None
        self.height = -1
        self.balance = 0  # -1,0,1

    def height(self):
        if self.root:
            return self.root.height
        else:
            return 0

    def update_balances(self, recursive=True):
        if self.root is not None:
            if recursive:
                if self.root.left is not None:
                    self.root.left.update_balances()
                if self.root.right is not None:
                    self.root.right.update_balances()
            self.balance = self.root.left.height - self.root.right.height

    def update_heights(self, recursive=True):  # height

        if self.root is not None:
            if recursive:
                if self.root.left is not None:
                    self.root.left.update_heights()
                if self.root.right is not None:
                    self.root.right.update_heights()
            self.height = max(self.root.left.height, self.root.right.height) + 1

    def rebalance(self):
        self.update_heights(False)
        self.update_balances(False)

        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.root.left.balance < 0:
                    self.root.left.RR()
                    self.update_heights()
                    self.update_balances()
                self.LL()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.root.right.balance > 0:
                    self.root.right.LL()
                    self.update_heights()
                    self.update_balances()
                self.RR()
                self.update_heights()
                self.update_balances()


    def insert(self, data):
        tree = self.root
        new_node = Node(data)
        if tree is None:
            self.root = new_node
            self.root.left = AVL()  # 서브트리 생성
            self.root.right = AVL()

        elif tree.data < data:
            self.root.left.insert(data)

        elif tree.data > data:
            self.root.right.insert(data)

        self.rebalance()

    def delete(self, remove_target):
        self.root, deleted = self._delete(self.root, remove_target)  # 삭제여부 확인(True : 삭제, False)
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

        # iii) 데이터가 타켓과 다를 때
        elif current_node.data > remove_target:
            current_node.left, deleted = self._delete(current_node.left, remove_target)

        else:
            current_node.right, deleted = self._delete(current_node.right, remove_target)

        return current_node, deleted

    def LL(self):
        a = self.root
        b = self.root.left.root
        t = b.right.root

        self.root = b
        self.root.right.root = a
        a.left.root = t

    def RR(self):
        a = self.root
        b = self.root.right.root
        t = b.left.root

        self.root = b
        self.root.left.root = a
        a.right.root = t

    def inorder(self):
        if self.root is None:
            return None
        else:
            # self.root.left.insert(data)
            self.root.left.inorder()
            print(self.root.data, end='->')
            self.root.right.inorder()


if __name__ == '__main__':
    node = [12, 8, 18, 17, 11, 5, 4]
    avl = AVL()
    for num in node:
        avl.insert(num)
    print(node)

    avl.inorder()