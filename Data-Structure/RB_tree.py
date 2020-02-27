class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.p = None
        self.color = True  # True : Red, False: Black


class RB:
    def __init__(self):
        self.nil = Node(0)
        self.nil.color = False
        self.nil.left = None
        self.nil.right = None

        self.root = self.nil

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.p = x
        y.p = x.p
        if x.p is None:
            self.root = y
        elif x == x.p.right:
            x.p.right = y
        else:
            y = x.p.left
        y.right = x
        x.p = y

    def left_rotate(self, x):
        y = x.right
        x.right = y.left

        if y.left != self.nil:
            y.left.p = x
        y.p = x.p
        if x.p is None:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            y = x.p.right
        y.left = x
        x.p = y

    def insert(self, data):
        new_node = Node(data)
        new_node.p = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.color = True

        y = None
        x = self.root

        while x != self.nil:
            y = x
            if new_node.data < x.data:
                x = x.left
            else:
                x = x.right
        new_node.p = y

        if y is None:
            self.root = new_node
        elif new_node.data < y.data:
            y.left = new_node
        else:
            y.right = new_node

        if new_node.p is None:
            new_node.color = False
            return

        if new_node.p.p is None:
            return

        self.insert_fixup(new_node)

    def insert_fixup(self, new_node):
        while new_node.p.color:
            if new_node.p == new_node.p.p.right:
                y = new_node.p.p.left

                if y.color:
                    y.color = False
                    new_node.p.color = False
                    new_node.p.p.color = True
                    new_node = new_node.p.p
                else:
                    if new_node == new_node.p.left:
                        new_node = new_node.p
                        self.right_rotate(new_node)
                    new_node.p.color = False
                    new_node.p.p.color = True
                    self.left_rotate(new_node.p.p)

            else:
                y = new_node.p.p.right

                if y.color:
                    y.color = False
                    new_node.p.color = False
                    new_node.p.p.color = True
                    new_node = new_node.p.p

                else:
                    if new_node == new_node.p.right:
                        new_node = new_node.p
                        self.left_rotate(new_node)
                    new_node.p.color = False
                    new_node.p.p.color = True
                    self.right_rotate(new_node.p.p)

            if new_node == self.root:
                break
        self.root.color = False

    def inorder(self, x):
        if x == self.nil:
            return None
        else:
            self.inorder(x.left)
            if x.color:
                print((x.data, 'Red',), end='->')
            else:
                print((x.data, 'Black',), end='>')
            self.inorder(x.right)

    def delete(self, remove_target):
        node = self.root
        delete_node = self. nil

        if node is None:
            return node

        while node != self.nil:
            if node.data == remove_target:
                delete_node = node

            if node.data <= remove_target:
                node = node.right
            else:
                node = node.left

        if delete_node == self.nil:
            return

        if delete_node.left == self.nil or delete_node.right == self.nil:
            y = delete_node
        else:
            y = self.succesor(delete_node)

        if y.left != self.nil:
            x = y.left
        else:
            x = y.right
        x.p = y.p

        if y.p == self.nil:
            self.root = x
        elif y == y.p.left:
            y.p.left = x
        else:
            y.p.right = x

        if y != delete_node:
            delete_node.data == y.data

        if y.color is False:
            self.delete_fixup(x)
        return y

    def delete_fixup(self, x):
        while x != self.root and x.color is False:
            if x == x.p.left:
                w = x.p.right  # x의 형제노드
                # case 1:
                if w.color:  # red
                    w.color = False
                    x.p.color = True
                    self.left_rotate(x.p)
                    w = x.p.right

                if w.left.color is False and w.right.color is False:
                    w.color = True
                    x = x.p

                else:
                    if w.right.color is False:
                        w.color = True
                        self.right_rotate(w)
                        w = x.p.right  # red
                    w.color = x.p.color
                    x.p.color = False
                    w.right.color = False
                    self.left_rotate(x.p)
                    x = self.root
            else:
                w = x.p.left
                if w.color:
                    w.color = False
                    x.p.color = True
                    self.right_rotate(x.p)
                    w = x.p.left
                if w.left.color is False and w.right.color is False:
                    w.color = True
                    x = x.p

                else:
                    if w.left.color is False:
                        w.right.color = False
                        w.color = True
                        self.left_rotate(w)
                        w = x.p.left
                    w.color = x.p.color
                    x.p.color = False
                    w.left.color = False
                    self.right_rotate(x.p)
                    x = self.root
        x.color = False

    def succesor(self, x):
        if x.right is not None:
            return self.minimum(x.right)
        y = x.p
        while y is not None and x == y.right:
            x = y
            y = y.p
        return y

    def minimum(self, x):
        while x.left is not None:
            x = x.right
        return x


if __name__ == '__main__':
    node = [10, 85, 15, 70, 20, 60, 30, 50]
    print(node)
    rb = RB()
    for num in node:
        rb.insert(num)
    rb.inorder(rb.root)
    print()
    rb.delete(20)
    print()
    rb.inorder(rb.root)
    print()
