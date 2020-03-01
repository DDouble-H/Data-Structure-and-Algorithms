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

        # full
        if len(root.keys) == (2 * self.order) - 1:
            temp = Node()
            self.root = temp

            temp.child.insert(0, root)
            self._split_child(temp, 0)
            self._insert(temp, key)
        else:
            self._insert(root, key)

    def _insert(self, current_node, key):
        i = len(current_node.key-1)

        if current_node.leaf:  # true
            while i >= 0 and key[i] < current_node.key[i]:
                current_node.keys[i+1] = current_node.key[i]
                i -= 1
            current_node.keys[i+1] = key
        else:
            while i >= 0 and key[i] > current_node.key[i]:
                i -= 1
            if len(current_node[i].keys) == (2 * self.order) - 1:
                self._split_child(current_node, i)
                if current_node.keys[i+1] < key:
                    i += 1
            self._insert(current_node.child, key)

    def _split_child(self, split_node, idx):
        temp_node = split_node.child[idx]
        temp = Node(temp_node.leaf)

        split_node.child.insert(idx+1, temp)
        split_node.keys.insert(idx, temp_node.keys[self.order-1])

        temp.keys = temp_node.keys[self.order:(self.order*2)-1]
        temp_node.keys = temp_node.keys[0:self.order-1]

        if not temp_node.leaf:
            temp.child = temp_node.child[self.order:(self.order*2)-1]
            temp_node.child = temp_node.child[0:self.order-1]


if __name__ == '__main__':

    Btree = btree()

    node = [5, 10, 4, 3, 17, 2, 9, 19, 6, 13]
    for num in node:
        Btree.insert(num)
