class Node:

    def __init__(self, data):

        self.data = data

        self.left = None

        self.right = None


class BinaryTree:

    def __init__(self):

        self.root = None


    def delete(self, node, root=None):

        if root is None:

            root = self.root


        if root is None:

            return None  # Дерево пустое


        # Если значение меньше, идем в левое поддерево

        if node < root.data:

            root.left = self.delete(node, root.left)

        # Если значение больше, идем в правое поддерево

        elif node > root.data:

            root.right = self.delete(node, root.right)

        else:

            # Узел для удаления найден

            if root.left is None and root.right is None:

                # Узел - лист, возвращаем None

                return None

            elif root.left is None:

                # Узел с одним правым потомком

                return root.right

            elif root.right is None:

                # Узел с одним левым потомком

                return root.left

            else:

                # Узел с двумя потомками (необработанный случай)

                min_larger_node = self.find_min(root.right)

                root.data = min_larger_node.data  # Заменяем данные

                root.right = self.delete(min_larger_node.data, root.right)  # Удаляем минимальный узел


        return root


    def find_min(self, node):

        while node.left is not None:

            node = node.left

        return node


    def insert(self, data):

        if self.root is None:

            self.root = Node(data)

        else:

            self._insert(data, self.root)


    def _insert(self, data, root):

        if data < root.data:

            if root.left is None:

                root.left = Node(data)

            else:

                self._insert(data, root.left)

        else:

            if root.right is None:

                root.right = Node(data)

            else:

                self._insert(data, root.right)


    def print_in_order(self, node):

        if node is not None:

            self.print_in_order(node.left)

            print(node.data, end=' ')

            self.print_in_order(node.right)


# Пример использования

tree = BinaryTree()

tree.insert(10)

tree.insert(5)

tree.insert(15)

tree.insert(3)


print("Дерево до удаления:")

tree.print_in_order(tree.root)  # Вывод: 3 5 10 15


# Удаляем узел без детей (лист)

tree.root = tree.delete(3)


print("\nДерево после удаления узла 3:")

tree.print_in_order(tree.root)  # Вывод: 5 10 15