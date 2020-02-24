class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.p = None
        self.color = True  # True : Red, False: Black
        self.nil = None


class RB:
    def __init__(self):
        self.root = None
        self.nil = None

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        y.right.p = x
        y.p = x.p
        if x.p is self.nil:
            y = self.root
        elif x == x.p.right:
            y = x.p.left
        else:
            y = x.p.right
        y.right = x
        x.p = y

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        y.left.p = x
        y.p = x.p
        if x.p is self.nil:
            y = self.root
        elif x == x.p.left:
            y = x.p.right
        else:
            y = x.p.left
        y.left = x
        x.p = y

    def insert(self, data):
        new_node = Node(data)
        y = self.nil
        x = self.root

        while x is not None:
                y = x
                if new_node.data < x.data:
                    x = x.left
                else:
                    x = x.right
        new_node.p = y

        if y is self.nil:
            self.root = new_node
            self.root.color = False
        elif new_node.data < y.data:
            y.left = new_node
        else:
            y.right = new_node

        self.insert_fix(new_node)

    def insert_fix(self, new_node):
        while new_node.p.color is True:  # and new_node.p.nil is not None:  # (case 1,2,3)
            if new_node.p == new_node.p.p.left:
                y = new_node.p.p.right  # y는 new_node의 삼촌
                # case 1:
                if y.color is True:  # true: red, false:black
                    new_node.p.color = False
                    y.color = False
                    new_node.p.p.color = True
                    new_node = new_node.p.p
                else:
                    # case 2:
                    if new_node == new_node.p.right:
                        new_node = new_node.p
                        self.left_rotate(new_node)
                    # case 3:
                    new_node.p.color = False
                    new_node.p.p.color = True
                    self.right_rotate(new_node.p.p)

            else:  # (case 4,5,6)
                y = new_node.p.p.left
                # case 4:
                if y.color is True:  # true: red, false:black
                    new_node.p.color = False
                    y.color = False
                    new_node.p.p.color = True
                    new_node = new_node.p.p
                else:
                    # case 2:
                    if new_node == new_node.p.left:
                        new_node = new_node.p
                        self.right_rotate(new_node)
                    # case 3:
                    new_node.p.color = False
                    new_node.p.p.color = True
                    self.left_rotate(new_node.p.p)
            if new_node == self.root:
                break
        self.root.color = False


if __name__ == '__main__':
    node = [10, 85, 15, 70, 20, 60, 30, 50]
    rb = RB()
    for num in node:
        print(num)
        rb.insert(num)
    print(node)