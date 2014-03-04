from BinaryTree import *

class RBNode(BTNode):
    """
    Node object for a binary tree structure.
    """

    def __init__(self, parent, data = None):
        super(BinaryTree, self).__init__(parent, data)
        self.color = True # Red = True, Black = False

    def children_count(self):
        return super(BinaryTree, self).children_count()

class RBTree(BinaryTree):

    def __init__(self):
        super(BinaryTree, self).__init__()

    def insert(self, data):
        node = super(BinaryTree, self).insert(data, RBNode)
        self.__post_insert_fix(node)

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

    def __post_insert_fix(self, node):

    def __rotate_left(self, node):
        pass

    def __rotate_right(self, node):
        pass