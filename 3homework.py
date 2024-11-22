import time
class Note:
    def __init__(self, date):
        self.data = date
        self.left = None
        self.right = None
class Tree:
    def __init__(self):
        self.root = None
    def check_value(self, root, note):
        if note.data < root.data:
            if root.right is None:
                root.right = note
            else: self.check_value(root.right, note)
        if note.data > root.data:
            if root.left is None:
                root.left = note
            else: self.check_value(root.left, note)
    def append(self, value):
        node = Note(value)
        if self.root is None:
            self.root = node
        else:
            if not self.find(node.data):
                self.check_value(self.root, node)
    def find(self,node, root=None, iteration = 0):
        if root is None:
            root = self.root
        iteration += 1
        if node == root.data:
            print("Note {} find on {} level of tree".format(node, iteration))
            return root
        elif node < root.data and root.right is not None:
            return self.find(node, root.right, iteration)
        elif node > root.data and root.left is not None:
            return self.find(node, root.left, iteration)
        else:
            return False

    def delete(self, node, root=None):
        if root is None:
            root = self.root
        if node > root.data:
            root.left = self.delete(node, root.left)
        elif node < root.data:
            root.right = self.delete(node, root.right)
        else:
            if root.right is None and root.left is None:
                return None
            elif root.right is None:
                return root.left
            elif root.left is None:
                return root.right
            else:
                min_larger_node = self.find_min(root.left)
                root.data = min_larger_node.data
                root.left = self.delete(min_larger_node.data, root.left)
        return root

    def find_min(self, node):
        while node.right is not None:
            node = node.right
        return node
    def print_tree(self, root=None):
        if root is None:
            root = self.root
        print(root.data)
        if root.right is not None:
            print("right from",root.data)
            self.print_tree(root.right)
        if root.left is not None:
            print("left from", root.data)
            self.print_tree(root.left)
BTR = Tree()
BTR.append(25)
BTR.append(4)
BTR.append(4)
BTR.append(28)
BTR.append(2)
BTR.append(5)
BTR.append(10)
BTR.print_tree()
BTR.delete(4)
BTR.print_tree()
end_time = time.time()
start_time = time.time()
BTR.find(28)
print(f"Время выполнения: {end_time - start_time:.30f} секунд")