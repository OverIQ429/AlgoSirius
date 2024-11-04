class Note:
    def __init__(self, date):
        self.data = date
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = None
        self.count = 0
    def check_value(self, root, note):
        if note.data > root.data:
            if root.left is None:
                root.left = note
            else: self.check_value(root.left, note)
        if note.data < root.data:
            if root.right is None:
                root.right = note
            else: self.check_value(root.right, note)
    def append(self, value):
        node = Note(value)
        if self.root is None:
            self.root = node
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
        print(root.data)
        if root.left is not None:
            print("left from",root.data)
            self.print_tree(root.left)
        if root.right is not None:
            print("right from", root.data)
            self.print_tree(root.right)

BTR = Tree()
BTR.append(25)
BTR.append(7)
BTR.append(2)
BTR.append(5)
BTR.append(10)
BTR.append(79)
BTR.append(71)
BTR.append(11)
BTR.append(12)
BTR.append(72)
BTR.append(6)
BTR.append(36)
BTR.append(73)
BTR.append(74)
BTR.append(4)
BTR.print_tree()

