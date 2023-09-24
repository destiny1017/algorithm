
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

        if node.left is None and node.right is None:
            if smaller_than_parent:
                parent.left = None
            else:
                parent.right = None
        elif node.left is None:
            if smaller_than_parent:
                parent.left = node.right
            else:
                parent.right = node.right
        elif node.right is None:
            if smaller_than_parent:
                parent.left = node.left
            else:
                parent.right = node.left
        else:
            max_node = node.left
            max_node_parent = node
            is_left_max = True
            while max_node.right is not None:
                max_node_parent = max_node
                max_node = max_node.right
                is_left_max = False

            if max_node.left is None:
                if smaller_than_parent:
                    parent.left.value = max_node.value
                else:
                    parent.right.value = max_node.value
            else:
                if is_left_max:
                    if smaller_than_parent:
                        parent.left = max_node
                    else:
                        parent.right = max_node
                else:
                    max_node_parent.right = max_node.left
                    if smaller_than_parent:
                        parent.left = max_node
                    else:
                        parent.right = max_node

        return True



def print_tree(node, level=0):
    if node is None:
        return

    print_tree(node.right, level + 1)
    print('    ' * level + str(node.value))
    print_tree(node.left, level + 1)


tree = BinarySearchTree()
tree.insert(5)
tree.insert(9)
tree.insert(7)
tree.insert(4)
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(8)

print_tree(tree.root)
print("-------------------------------")
tree.delete(3)
print_tree(tree.root)
print("-------------------------------")
tree.delete(8)
print_tree(tree.root)
print("-------------------------------")
tree.delete(7)
print_tree(tree.root)

print(tree.search(2))
print(tree.search(8))
print(tree.search(10))
print(tree.search(9))
print("=====================")
print(tree.delete(11))
print(tree.delete(5))
print_tree(tree.root)



