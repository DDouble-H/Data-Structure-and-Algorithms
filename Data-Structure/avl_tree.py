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

    def update_heights(self, recursive=True):
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
        elif tree.data > data:
            self.root.left.insert(data)
        elif tree.data < data:
            self.root.right.insert(data)

        self.rebalance()

    # 노드 입력 > 값 입력, height 계산, bf 체크, >> 깨졌을 때 rr, ll, rl, lr  height가 -로 가는 경우?
    def delete(self, remove_target):
        if self.root is None:
            return self.root
        if self.root is not None:
            if self.root.data == remove_target:
                if self.root.left.root is None and self.root.right.root is None:  # left, right 둘 다 없을 때
                    self.root = None
                elif self.root.left.root is None and self.root.right.root is not None:  # L, R 둘 중에 하나만 있을 때
                    # 삭제할 노드의 오른쪽의 제일 작은 값이 위치, 노드끼리 연결
                    self.root = self.root.right.root
                elif self.root.left.root is not None and self.root.right.root is None:
                    self.root = self.root.left.root
            elif self.root.data > remove_target:
                self.root.left.delete(remove_target)
            else:
                self.root.right.delete(remove_target)

            self.rebalance()

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
    print()
    avl.delete(17)
    print()
    avl.inorder()
