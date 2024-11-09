class Note:
    def __init__(self, value):
        self.date = value
        self.left = None
        self.right = None
        self.color = "red"
        self.parent = None

class RedBlackTree:
    def __init__(self):
        self.root = None

    def case1(self, father, uncle, grantpa):
        grantpa.color = "red"
        father.color = uncle.color = "black"
        if grantpa is self.root:
            grantpa.color = "black"
        self.check_rules(grantpa)

    def rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left is not None:
            right_child.left.parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node is node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child
        right_child.left = node
        node.parent = right_child

    def rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right is not None:
            left_child.right.parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node is node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child
        left_child.right = node
        node.parent = left_child

    def check_rules(self, root):
        while root != self.root and root.parent.color == "red":
            if root.parent:
                if root.parent.color == root.color == "red":
                    if root.parent.parent.left == root.parent:
                        uncle = root.parent.parent.right
                    else:
                        uncle = root.parent.parent.left
                    if uncle.color == "red":
                        self.case1(root.parent, uncle, root.parent.parent)
                    else:
                        if root.parent.parent.left == root.parent and root.parent.right == root:
                            root = root.parent
                            self.rotate_left(root)
                        elif root.parent.parent.right == root.parent and root.parent.left == root:
                            root = root.parent
                            self.rotate_right(root)
                        elif root.parent.parent.left == root.parent and root.parent.left == root:
                            root.parent.color = "black"
                            root.parent.parent.color = "red"
                            self.rotate_right(root.parent.parent)
                        elif root.parent.parent.right == root.parent and root.parent.right == root:
                            root.parent.color = "black"
                            root.parent.parent.color = "red"
                            self.rotate_left(root.parent.parent)

        self.root.color = "black"

    def new_value(self, note, root = None):
        if root is None:
            root = self.root
        if note.date > root.date:
            if root.right and root.right.date is None:
                note.parent = root
                root.right = note
                self.check_rules(note)
            else:
                self.new_value(note, root.right)
        elif note.date < root.date:
            if root.left and root.left.date is None:
                note.parent = root
                root.left = note
                self.check_rules(note)
            else:
                self.new_value(note, root.right)


    def append(self, value):
        note = Note(value)
        note.left = Note(None)
        note.right = Note(None)
        note.right.color = "black"
        note.left.color = "black"
        if self.root is None:
            note.color = "black"
            self.root = note
            self.count = 2
        else:
            self.new_value(note)

    def print_tree(self, root=None):
        if root is None:
            root = self.root
        print(root.date, "Color is ", root.color )
        if root.left is not None:
            print("left from",root.date)
            self.print_tree(root.left)
        if root.right is not None:
            print("right from", root.date)
            self.print_tree(root.right)

BTR = RedBlackTree()
BTR.append(1)
BTR.append(2)
BTR.append(3)
BTR.append(4)
BTR.append(5)
BTR.append(6)
BTR.append(7)
BTR.append(8)
BTR.append(9)
BTR.append(10)
BTR.print_tree()