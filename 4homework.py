import time
start_time = time.time()
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
        if right_child.left.date is not None:
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
                    if root.parent.parent:
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
                    else:
                        return
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
                self.new_value(note, root.left)



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

    def find_min(self, node):
        while node.left.date is not None:
            node = node.left
        return node

    def del_v_with_kids(self, node):
        root = self.find_min(node.right)
        local_val = node.date
        node.date = root.date
        root.date = local_val
        if root.parent and node.parent:
            if root.parent.date == root.date:
                root.parent = node
        self.delete(root.date, root)

    def del_b_v_with_one_kid(self, node):
        if node.left.date is not None:
            local_val = node.date
            node.date = node.left.date
            node.left.date = local_val
            self.delete(node.left.date)
        else:
            local_val = node.date
            node.date = node.right.date
            node.right.date = local_val
            self.delete(node.right.date, node.right)

    def del_first_case(self, note, father, brother):
        note.date = father.date
        father.date  = brother.date
        if brother == father.right:
            note.right = brother.left
            father.right = brother.right
            father.right.color = "black"
        else:
            note.left = brother.right
            father.left = brother.left
            father.left.color = "black"

    def del_second_case(self, note, father, brother):
        local_val = brother.date
        brother.date = brother.left.date
        brother.left = Note(None)
        brother.left.color = "black"
        local_val1 = brother.right.date
        brother.right.date = local_val
        brother.right.color = "red"
        brother.right.right.date = local_val1
        self.del_first_case(note, father, brother)



    def two_kids_black(self, note, brother,father, node1 = None):
        brother.color = "red"
        if father.color == "red":
            father.color = "black"
            note.date = None
            note.left, note.right = None, None
            note.color = "black"
        else:
            if father.date != self.root.date:
                if father.parent.left == father:
                    uncle = father.parent.right
                else:
                    uncle = father.parent.left
                self.two_kids_black(father, uncle ,father.parent, note)
            else:
                return

    def del_b_v_with_no_kids(self, root):
        father = root.parent
        if father is None:
            return
        if father.left.date == root.date:
            brother = father.right
        else:
            brother = father.left
        if brother.color == "black":
            if brother.left and brother.right:
                if brother.left.color == "red" or brother.right.color == "red":
                    if brother.right.color == "red":
                        self.del_first_case(root, father, brother)
                    elif brother.right.color == "black":
                        self.del_second_case(root, father, brother)
                elif brother.left.color == "black" and brother.right.color == "black":
                    root.date = None
                    root.color = "black"
                    root.left, root.right = None, None
                    self.two_kids_black(root,brother,father)
        else:
            if brother == father.right:
                local = Note(root.date)
                local.color = "black"
                root.date = father.date
                root.right = brother.left
                root.color = "red"
                father.date = brother.date
                father.right = brother.right
                brother.date = brother.right.date
                brother.color = "black"
                brother.left, brother.right = brother.right.left, brother.right.right
            else:
                local = Note(root.date)
                local.color = "black"
                root.date = father.date
                root.left = brother.right
                root.color = "red"
                father.date = brother.date
                father.left = brother.left
                brother.date = brother.left.date
                brother.color = "black"
                brother.left, brother.right = brother.right.left, brother.right.right
            if root.left.date is None:
                root.left = local
                new_val = root.left
                root.left.left, root.left.right = Note(None), Note(None)
                root.left.left.color, root.left.right.color = "black", 'black'
                root.left.parent = root
            else:
                root.right = local
                new_val = root.right
                root.right.left, root.right.right = Note(None), Note(None)
                root.right.left.color, root.right.right.color = "black", 'black'
                root.right.parent = root
            self.del_b_v_with_no_kids(new_val)

    def find(self,node, root=None, iteration = 0):
        if root is None:
            root = self.root
        iteration += 1
        if node == root.date:
            print("Note {} find on {} level of tree. Color is {}".format(node, iteration, root.color))
            return root
        elif node < root.date and root.right.date is not None:
            return self.find(node, root.left, iteration)
        elif node > root.date and root.left.date is not None:
            return self.find(node, root.right, iteration)
        else:
            return False

    def delete(self, node, root=None):
        if root is None:
            root = self.root
        if node > root.date:
            self.delete(node, root.right)
        elif node < root.date:
            self.delete(node, root.left)
        else:
            if root.color == "red" and root.left.date is None and root.right.date is None:
                root.date = None
                root.color = "black"
                root.left, root.right = None, None
            elif root.left.date and root.right.date:
                self.del_v_with_kids(root)
            elif root.color == "black" and (root.left.date is not None and root.right.date is None or root.right.date is not None and root.left.date is None):
                self.del_b_v_with_one_kid(root)
            elif root.color == "black" and root.left.date is None and root.right.date is None:
                self.del_b_v_with_no_kids(root)


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
BTR.delete(7)
BTR.delete(9)
BTR.delete(3)
BTR.print_tree()
BTR.find(10)
end_time = time.time()
print(f"Время выполнения: {end_time - start_time:.12f} секунд")