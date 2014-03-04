from BinaryTree import *

class AVLNode(BTNode):
    """
    Node object for a binary tree structure.
    """

    def __init__(self, parent, data = None):
        super(BinaryTree, self).__init__(parent, data)
        self.height = 1

    def children_count(self):
        return super(BinaryTree, self).children_count()

class AVLTree(BinaryTree):

    def __init__(self):
        super(BinaryTree, self).__init__()

    def insert(self, data):
        node = super(BinaryTree, self).insert(data, AVLNode)
        self.__recompute_height(node.parent)

    def search(self, data):
        super(BinaryTree, self).search(data)

    def remove(self, data):
        super(BinaryTree, self).remove(data)

    def minimum(self, node):
        super(BinaryTree, self).minimum(node)

    def maximum(self, node):
        super(BinaryTree, self).maximum(node)

    def size(self):
        super(BinaryTree, self).size(data)

    def isEmpty(self, data):
        super(BinaryTree, self).isEmpty(data)

    def isInteral(self, node):
        super(BinaryTree, self).isInteral(node)

    def isExternal(self, node):
        super(BinaryTree, self).isExternal(node)

    def isRoot(self, node):
        super(BinaryTree, self).isRoot(node)

    def print_dfs(self):
        super(BinaryTree, self).print_dfs

    def print_bfs(self):
        super(BinaryTree, self).print_bfs

    def print_inorder(self):
        super(BinaryTree, self).print_inorder

    def print_preorder(self):
        super(BinaryTree, self).print_preorder

    def print_postorder(self):
        super(BinaryTree, self).print_postorder

    def __recompute_height(self, node):
        """
        @return: recompute heights of all nodes from the given node and up
        """
        while node:
            node.height = max_height(node.left, node.right) + 1
            node = node.parent

    def __max_height(self, left, right):
        """
        @return: max height of two subtrees
        """
        left_height = 0 if left is None else left.height
        right_height = 0 if right is None else right.height
        return max(left_height, right_height)

    def __diff_height(self, left, right):
        """
        @return: difference in height of two subtrees
        """
        left_height = 0 if left is None else left.height
        right_height = 0 if right is None else right.height
        return abs(left_height - right_height)