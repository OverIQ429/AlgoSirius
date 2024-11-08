class Note:
    def __init__(self, date):
        self.data = date
        self.left = None
        self.right = None
        self.color = "black"
        self.parent = None
class RedBlackTree:
    def __init__(self):
        self.root = None
        self.count = 0

    def change_root(self, new_root, aim):
        old_root = Note(self.root.data)
        old_root.color = self.root.color
        self.root.data = new_root.data
        self.root.color = new_root.color
        old_root.left = Note(None)
        old_root.right = Note(None)
        if aim == "left":
            self.root.left = old_root
        else:
            self.root.right = old_root
        old_root.parent = self.root

    def rotate_left(self, note):
        uncle = note.left
        father = note.right
        son = note.right.right
        if note == self.root:
            self.change_root(father, "left")
        else:
            old_note = note
            note.data = father.data
            note.color = father.color
            note.left = Note(None)
            note.right = Note(None)
            note.left = old_note
        note.right = son
        note.left.left = uncle

    def rotate_right(self, note):
        uncle = note.right
        father = note.left
        son = note.left.left
        if note == self.root:
            self.change_root(father, "right")
        else:
            old_note = note
            note.data = father.data
            note.color = father.color
            note.left = Note(None)
            note.right = Note(None)
            note.right = old_note

        note.right.right = uncle
        note.left = son

    def check_child(self, note):
        if note.parent.color == "red" and note.color == "red":
            if note.parent == note.parent.parent.right and note.parent.right == note:
                uncle = note.parent.parent.left
                if uncle and uncle.color == "black":
                    note.parent.color = "black"
                    note.parent.parent.color = "red"
                    self.rotate_left(note.parent.parent)
                else:
                    note.parent.color = "black"
                    if self.root != note.parent.parent:
                        note.parent.parent.color = "red"
                    uncle.color = "black"
            elif note.parent == note.parent.parent.left and note.parent.left == note:
                uncle = note.parent.parent.right
                if uncle and uncle.color == "black":
                    note.parent.color = "black"
                    note.parent.parent.color = "red"
                    self.rotate_right(note.parent.parent)
            elif note.parent == note.parent.parent.right and note.parent.left == note:
                tmc = Note(note.data)
                tmc.color = note.color
                tmc.left = Note(None)
                tmc.right = Note(None)
                father = Note(note.parent.data)
                father.color = note.parent.color
                father.left = Note(None)
                father.right = Note(None)
                note.parent = tmc
                note.parent.right = father
                note.left = None
                note.right = None
                note.color = "black"
                note.data = None
            elif note.parent == note.parent.parent.left and note.parent.right == note:
                tmc = Note(note.data)
                tmc.color = note.color
                tmc.left = Note(None)
                tmc.right = Note(None)
                father = Note(note.parent.data)
                father.color = note.parent.color
                father.left = Note(None)
                father.right = Note(None)
                note.parent = tmc
                note.parent.left = father
                note.left = None
                note.right = None
                note.color = "black"
                note.data = None
        self.root.color = 'black'


    def __rules(self, note):
        self.check_child(note)

    def check_value(self, root, note, deep=2 ):
        if note.data > root.data:
            if root.right and root.right.data is None:
                note.parent = root
                root.right = note
                note.color = "red"
                null_left = Note(None)
                note.left = null_left
                null_right = Note(None)
                note.right = null_right

            else:
                deep +=1
                self.check_value(root.right, note, deep)
        if note.data < root.data:
            if root.left and root.left.data is None:
                note.color = "red"
                root.left = note
                note.parent = root
                null_left = Note(None)
                note.left = null_left
                null_right = Note(None)
                note.right = null_right
            else:
                deep += 1
                self.check_value(root.left, note, deep)
        self.__rules(note)
    def append(self, value):
        node = Note(value)
        if self.root is None:
            node.color = "black"
            null_left = Note(None)
            node.left = null_left
            null_right = Note(None)
            node.right = null_right
            self.root = node
            self.count = 2
        else:
            self.check_value(self.root, node)
    def find(self,node, root=None, iteration = 0):
        if root is None:
            root = self.root
        iteration += 1
        if node == root.data:
            print("Note {} find on {} level of tree".format(node, iteration))
            return root
        elif node > root.data and root.right is not None:
            self.find(node, root.right, iteration)
        elif node < root.data and root.left is not None:
            self.find(node, root.left, iteration)
        else:
            return "Error. Not find this Note"

    def delete(self, node, root=None):
        if root is None:
            root = self.root
        if node < root.data:
            root.left = self.delete(node, root.left)
        elif node > root.data:
            root.right = self.delete(node, root.right)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                min_larger_node = self.find_min(root.right)
                root.data = min_larger_node.data
                root.right = self.delete(min_larger_node.data, root.right)
        return root

    def find_min(self, node):
        while node.left is not None:
            node = node.left
        return node
    def print_tree(self, root=None):
        if root is None:
            root = self.root
        print(root.data, "Color is ", root.color )
        if root.left is not None:
            print("left from",root.data)
            self.print_tree(root.left)
        if root.right is not None:
            print("right from", root.data)
            self.print_tree(root.right)

BTR = RedBlackTree()
BTR.append(25)
BTR.append(9)
BTR.append(4)
BTR.append(28)
BTR.append(2)
BTR.append(5)
BTR.append(10)
BTR.print_tree()

