class Node:
    def __init__(self, leaf=False):
        self.keys = []
        self.leaf = leaf
        self.child = []


class btree:
    def __init__(self, order):
        self.root = Node(True)
        self.order = order

    def insert(self, key):
        root = self.root

        if len(root.keys) == (2 * self.order) -1:
            temp = Node()
            self.root = temp
            # root 새로운 루트의 0번째 자식
            temp.child.insert(0, root)
            self._child_split(temp, 0)
            self._insert(temp, key)
        else:
            self._insert(root, key)

    def _insert(self, current_node, key):
        i = len(current_node.key-1)
        # current_node가 leaf 일 때, 아닐 때
        if current_node.leaf:  # true
            # 삽입할 새 키의 위치 찾기
            # 키 앞으로 이동
            while i >= 0 and key[i] < current_node.key[i]:
                current_node.keys[i+1] = current_node.key[i]
                i -= 1
            current_node.keys[i+1] = key
        else:
            while i >= 0 and key[i] > current_node.key[i]:
                i -= 1
            if len(current_node[i].keys) == (2 * self.order) -1:
                    self._child_split(current_node, i)
                    if current_node.keys[i+1] < key:
                        i += 1
            self._insert(current_node.child, key)


    # split_node 분할(idx 기준) 분할하고자 하는 노드의 부모
    # 기준값이 노드의 부모(가운데 값 올리면 됨)
    def _child_split(self, split_node, idx):
        pass

    def delete(self, current_node, key):
        pass

    def _delete(self, current_node, key, idx):
        pass


if __name__ == '__main__':

    Btree = btree()

    node = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
    for num in node:
        Btree.insert(num)

