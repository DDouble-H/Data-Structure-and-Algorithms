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
        i = len(current_node.keys) - 1

        if current_node.leaf:  # true
            current_node.keys.append((None, None))
            while i >= 0 and key[0] < current_node.keys[i][0]:
                current_node.keys[i + 1] = current_node.keys[i]
                i -= 1
            current_node.keys[i+1] = key
        else:
            while i >= 0 and key[0] < current_node.keys[i][0]:
                i -= 1
            i += 1
            if len(current_node.child[i].keys) == (2 * self.order) - 1:
                self._split_child(current_node, i)
                if key[0] > current_node.keys[i][0]:
                    i += 1
            self._insert(current_node.child[i], key)

    def _split_child(self, split_node, idx):
        temp_node = split_node.child[idx]
        temp = Node(temp_node.leaf)

        split_node.child.insert(idx+1, temp)
        split_node.keys.insert(idx, temp_node.keys[self.order-1])

        temp.keys = temp_node.keys[self.order:(self.order*2)-1]
        temp_node.keys = temp_node.keys[0:self.order-1]

        if not temp_node.leaf:
            temp.child = temp_node.child[self.order:self.order * 2]
            temp_node.child = temp_node.child[0:self.order-1]

    def tree_print(self, current_node, l=0):
        print("Level ", l, " ", len(current_node.keys), end=">")
        for i in current_node.keys:
            print(i, end=" ")
        print()
        l += 1
        if len(current_node.child) > 0:
            for i in current_node.child:
                self.tree_print(i, l)

    def delete(self, current_node, key):
        if current_node.key is not None and current_node.leaf:
            del current_node.key
        else:
            self._delete(current_node, key, idx)

    def _delete(self, current_node, key, idx):
        pass
    def _delete_predeessor(self, current_node):
        pass
    def _delete_successor(self, current_node):
        pass
    def _del_merge(self, parent_node, i, j):
        pass
    def _delete_sibling(self, parent_node, i, j):
        pass


if __name__ == '__main__':

    Btree = btree(5)

    node = [5, 10, 4, 3, 17, 2, 9, 19, 6, 13]
    for num in node:
        Btree.insert((num, 2 * num))

    Btree.tree_print(Btree.root)
