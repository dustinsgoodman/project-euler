from BinaryTree import *

class AVLNode(BTNode):
    """
    Node object for a binary tree structure.
    """

    def __init__(self, parent, data = None):
        super(AVLNode, self).__init__(parent, data)
        self.height = 1

    def children_count(self):
        return super(AVLNode, self).children_count()

    def __str__(self):
        x = "%dh%d" % (self.data, self.height)
        if self.parent:
            x += " P%d" % (self.parent.data)
        if self.left:
            x += " L%d" % (self.left.data)
        if self.right:
            x += " R%d" % (self.right.data)
        return x

class AVLTree(BinaryTree):

    def __init__(self):
        super(AVLTree, self).__init__()

    def search(self, data):
        return super(AVLTree, self).search(data)

    def insert(self, data):
        node = super(AVLTree, self).insert(data, AVLNode)
        self.recompute_height(node.parent)

        # check for height violation and fix it
        node_to_fix = node
        while node_to_fix: 
            if abs(self.diff_height(node_to_fix.left, node_to_fix.right)) <= 1:
                node_to_fix = node_to_fix.parent
            else:
                self.rebalance(node_to_fix)
                break
        return node

    def remove(self, data):
        node = self.search(data)
        if node is None:
            return

        children_count = node.children_count()
        parent = node.parent
        if children_count == 0:
            if parent.left is node:
                parent.left = None
            else:
                parent.right = None
            return self.remove_helper(node, parent)
        elif children_count == 1:
            if node.left:
                child = node.left
            else:
                child = node.right
            if parent:
                if parent.left is node:
                    parent.left = child
                else:
                    parent.right = child
            return self.remove_helper(node, parent)
        else:
            successor = self.minimum(node.right)
            parent = successor.parent

            if successor.parent is not node:
                successor.parent.left = None
            successor.parent = node.parent

            successor.left = node.left
            node.left.parent = successor
            successor.right = node.right
            node.right.parent = successor

            if self.isRoot(node):
                self.root = successor
            else:
                if node.parent.left is node:
                    node.parent.left = successor
                else:
                    node.parent.right = successor
            return self.remove_helper(node, parent)

    def minimum(self, node):
        return super(AVLTree, self).minimum(node)

    def maximum(self, node):
        return super(AVLTree, self).maximum(node)

    def size(self):
        return super(AVLTree, self).size()

    def isEmpty(self, data):
        return super(AVLTree, self).isEmpty(data)

    def isInteral(self, node):
        return super(AVLTree, self).isInteral(node)

    def isExternal(self, node):
        return super(AVLTree, self).isExternal(node)

    def isRoot(self, node):
        return super(AVLTree, self).isRoot(node)

    def print_dfs(self):
        super(AVLTree, self).print_dfs()

    def print_bfs(self):
        super(AVLTree, self).print_bfs()

    def print_inorder(self, node):
        super(AVLTree, self).print_inorder(node)

    def print_preorder(self, node):
        super(AVLTree, self).print_preorder(node)

    def print_postorder(self, node):
        super(AVLTree, self).print_postorder()

    def remove_helper(self, node, parent):
        self.recompute_height(parent)
        while parent:
            if not abs(self.diff_height(parent.left, parent.right)) <= 1:
                self.rebalance(parent)
                break
            parent = parent.parent
        return super(AVLTree, self).remove_helper(node)

    def recompute_height(self, node):
        """
        @return: recompute heights of all nodes from the given node and up
        """
        while node:
            node.height = self.max_height(node.left, node.right) + 1
            node = node.parent

    def max_height(self, left, right):
        """
        @return: max height of two subtrees
        """
        left_height = 0 if left is None else left.height
        right_height = 0 if right is None else right.height
        return max(left_height, right_height)

    def diff_height(self, left, right):
        """
        @return: difference in height of two subtrees
        """
        left_height = 0 if left is None else left.height
        right_height = 0 if right is None else right.height
        return left_height - right_height

    def rebalance(self, node):
        if self.diff_height(node.left, node.right) == 2:
            test = node.left
            if self.diff_height(test.left, test.right) == -1:
                self.rotate_left_right(test)
                self.recompute_height(test)
            else:
                self.rotate_left_left(node)
                self.recompute_height(node)
        else:
            test = node.right
            if self.diff_height(test.left, test.right) == 1:
                self.rotate_right_left(test)
                self.recompute_height(test)
            else:
                self.rotate_right_right(node)
                self.recompute_height(node)

    def rotate_left_right(self, node): #rotate left
        root, left, right = node.right, node, node.parent

        if self.isRoot(node.parent):
            self.root = node.right
        else:
            if node.parent.parent.right is node.parent:
                node.parent.parent.right = root
            else:
                node.parent.parent.left = root

        root.parent = right.parent
        left.parent, left.right = root, root.left
        right.parent, right.left = root, root.right
        root.left, root.right = left, right
        self.recompute_height(right)

    def rotate_left_left(self, node): #rotate right
        root, left, right = node.left, node.left.left, node

        if self.isRoot(node.parent):
            self.root = node
        else:
            if node.parent.right is node:
                node.parent.right = root
            else:
                node.parent.left = root

        root.parent = right.parent
        right.parent, right.left = root, root.right
        root.right = right
        root.parent.left = root
        self.recompute_height(left)


    def rotate_right_left(self, node): #rotate right
        root, left, right = node.left, node.parent, node
        
        if self.isRoot(node.parent):
            self.root = node.left
        else:
            if node.parent.parent.right is node.parent:
                node.parent.parent.right = root
            else:
                node.parent.parent.left = root
        
        root.parent = node.parent.parent
        left.parent, left.right = root, root.left
        right.parent, right.left = root, root.right
        root.left, root.right = left, right
        self.recompute_height(left)

    def rotate_right_right(self, node): #rotate left
        root, left, right = node.right, node, node.right.right

        if self.isRoot(node.parent):
            self.root = node
        else:
            if node.parent.parent.right is node:
                node.parent.parent.right = root
            else:
                node.parent.parent.left = root

        root.parent = node.parent
        left.parent, left.right = root, root.left
        right.parent = root
        root.left = left
        self.recompute_height(right)

    def out(self, start_node = None):
        return super(AVLTree, self).out(start_node)