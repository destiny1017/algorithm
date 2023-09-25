
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.__insert_recursive(self.root, value)

    def __insert_recursive(self, node, value):

        if node.value > value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.__insert_recursive(node.left, value)
        elif node.value < value:
            if node.right is None:
                node.right = Node(value)
            else:
                self.__insert_recursive(node.right, value)
        else:
            return None

    def search(self, value):
        return self.__search_recursive(self.root, value)

    def __search_recursive(self, node, value):

        if node is None:
            return False
        elif node.value == value:
            return True
        elif node.value > value:
            return self.__search_recursive(node.left, value)
        elif node.value < value:
            return self.__search_recursive(node.right, value)

    def __node_change(self, left_change, target, value):
        if left_change:
            target.left = value
        else:
            target.right = value

    def __node_value_change(self, left_change, target, value):
        if left_change:
            target.left.value = value
        else:
            target.right.value = value

    def delete(self, value):
        node = self.root
        parent = None
        smaller_than_parent = None

        # 요소 찾기
        while True:
            if node is None:
                return False
            if node.value == value:
                break
            elif node.value > value:
                parent = node
                node = node.left
                smaller_than_parent = True
            elif node.value < value:
                parent = node
                node = node.right
                smaller_than_parent = False

        if parent is not None:
            if node.left is None and node.right is None:
                self.__node_change(smaller_than_parent, parent, None)
            elif node.left is None:
                self.__node_change(smaller_than_parent, parent, node.right)
            elif node.right is None:
                self.__node_change(smaller_than_parent, parent, node.left)
            else:
                max_node = node.left
                max_node_parent = node
                is_left_max = True
                while max_node.right is not None:
                    max_node_parent = max_node
                    max_node = max_node.right
                    is_left_max = False

                if max_node.left is None:
                    # self.__node_value_change(smaller_than_parent, parent, max_node.value)
                    node.value = max_node.value
                    if is_left_max:
                        max_node_parent.left = None
                    else:
                        max_node_parent.right = None
                else:
                    if is_left_max:
                        max_node.right = node.right
                        node.left = max_node
                    else:
                        max_node_parent.right = max_node.left
                        node.value = max_node.value
        else:
            if node.left is None and node.right is None:
                self.root = None
            elif node.left is None:
                self.root = node.right
            else:
                max_node = node.left
                max_node_parent = node
                is_left_max = True
                while max_node.right is not None:
                    max_node_parent = max_node
                    max_node = max_node.right
                    is_left_max = False

                if max_node.left is None:
                    if is_left_max:
                        max_node.right = self.root.right
                        self.root = max_node
                    else:
                        self.root.value = max_node.value
                        max_node_parent.right = None
                else:
                    if is_left_max:
                        max_node.right = self.root.right
                        self.root = max_node
                    else:
                        self.root.value = max_node.value
                        max_node_parent.right = max_node.left

        return True


def print_tree(node, level=0):
    if node is None:
        return

    print_tree(node.right, level + 1)
    print('    ' * level + str(node.value))
    print_tree(node.left, level + 1)


def set_tree_value(tree):
    tree.insert(7)
    tree.insert(4)
    tree.insert(2)
    tree.insert(9)
    tree.insert(5)
    tree.insert(1)
    tree.insert(3)
    tree.insert(8)
    tree.insert(11)
    tree.insert(10)


tree = BinarySearchTree()
set_tree_value(tree)

print_tree(tree.root)
print("-------------------------------")
tree.delete(7)
print_tree(tree.root)
print("-------------------------------")
tree.delete(5)
print_tree(tree.root)
print("-------------------------------")
tree.delete(3)
print_tree(tree.root)
print("-------------------------------")
tree.delete(1)
print_tree(tree.root)
print("-------------------------------")
tree.delete(9)
print_tree(tree.root)
print("-------------------------------")
tree.delete(4)
print_tree(tree.root)
print("-------------------------------")
tree.delete(2)
print_tree(tree.root)
print("-------------------------------")
tree.delete(8)
print_tree(tree.root)
print("-------------------------------")
tree.insert(5)
tree.insert(3)
tree.insert(4)
tree.insert(15)
tree.insert(13)
tree.insert(14)
print_tree(tree.root)


