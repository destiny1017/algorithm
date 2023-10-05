# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def __dfs(self, node, ordered_list):
        if node.left is not None:
            self.__dfs(node.left)
        ordered_list.append(node)
        if node.right is not None:
            self.__dfs(node.right)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        ordered_list = []
        self.__dfs(root, ordered_list)
        print(' '.join(str(node.val) for node in ordered_list))
        err_node = [None, None]
        continue_idx = 0
        for i in range(len(ordered_list) - 1):
            if ordered_list[i].val > ordered_list[i + 1].val:
                err_node[0] = ordered_list[i]
                continue_idx = i + 1
                break

        for i in range(continue_idx, len(ordered_list)):
            if ordered_list[i - 1].val > ordered_list[i].val:
                err_node[1] = ordered_list[i]

        err_node[0].val, err_node[1].val = err_node[1].val, err_node[0].val





