from BinaryTree import *

class SplayNode(BTNode):

    def __init__(self, parent, data = None):
        super(SplayNode, self).__init__(parent, data)

    def children _count(self):
        return super(SplayNode, self).children_count()

    def __str__(self):
        return str(self.data)

class SplayTree(BinaryTree):

    def __init__(self):
        super(SplayTree, self).__init__()

    def search(self, data):
        node = self.find_entry(data)
        self.splay(node)
        if node.data == data:
            return node
        else:
            return None

    def insert(self, data):
        if self.root is None:
            self.root = SplayNode(None, data)
            return self.root

        node = self.find_entry(data)
        if node.data == data:
            self.splay(node)
            return node

        new_node = SplayNode(node, data)
        if data < node.data:
            node.left = new_node
        else:
            node.right = new_node
        self.splay(new_node)
        return new_node

    def remove(self, data):
        node = self.find_entry(data)

        if data != node.data:
            self.splay(node)
            return None

        children_count = node.children_count()
        parent = node.parent
        if children_count == 0:
            if parent.left is node:
                parent.left = None
            else:
                parent.right = None
            self.splay(parent)
            return self.remove_helper(node)
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
                self.splay(parent)
            return self.remove_helper(node)
        else:
            successor = self.minimum(node.right)

            if successor.parent is not node:
                successor.parent.left = None
            successor.parent = node.parent

            successor.left = node.left
            node.left.parent = successor
            successor.right = node.right
            node.right.parent = successor

            if node.parent.left is node:
                node.parent.left = successor
            else:
                node.parent.right = successor
            self.splay(node.parent)
            return self.remove_helper(node)

    def minimum(self, node):
        return super(SplayTree, self).minimum(node)

    def maximum(self, node):
        return super(SplayTree, self).maximum(node)

    def size(self):
        return super(SplayTree, self).size()

    def isEmpty(self, data):
        return super(SplayTree, self).isEmpty(data)

    def isInteral(self, node):
        return super(SplayTree, self).isInteral(node)

    def isExternal(self, node):
        return super(SplayTree, self).isExternal(node)

    def isRoot(self, node):
        return super(SplayTree, self).isRoot(node)

    def print_dfs(self):
        super(SplayTree, self).print_dfs()

    def print_bfs(self):
        super(SplayTree, self).print_bfs()

    def print_inorder(self, node):
        super(SplayTree, self).print_inorder(node)

    def print_preorder(self, node):
        super(SplayTree, self).print_preorder(node)

    def print_postorder(self, node):
        super(SplayTree, self).print_postorder()

    def out(self, start_node = None):
        return super(SplayTree, self).out(start_node)

    def find_entry(self, data):
        curr_node, prev_node = self.root, self.root
        while curr_node:
            if data < curr_node.data:
                prev_node, curr_node = curr_node, curr_node.left
            elif data > curr_node.data:
                prev_node, curr_node = curr_node, curr_node.right
            else:
                return curr_node
        return prev_node

    def splay(self, node):
        while not self.isRoot(node):
            if node.parent is self.root:
                self.zig1(node)
            else:
                self.zig2(node)

    def zig1(self, A):
        """
        Handles case of zig or zag. These only happen when dealing with root node.

              B             A
            /  \           / \
           A    z    =>   C   B
         /  \                / \
        C    y              y   z

        or

           B               A
         /   \            / \
        w     A     =>   B   C
             / \        / \
            x   C      w   x
        """
        B = A.parent
        if node is parent.left:
            C, y, z = A.left, A.right, B.right

            A.left = C
            if C is not None:
                C.parent = A
            A.right, B.parent = B, A
            B.left = y
            if y is not None:
                y.parent = B
            B.right = z
            if z is not None:
                z.parent = B
        else:
            C, w, x = A.right, B.left, A.left

            A.left, B.parent = B, A
            A.right = C
            if C is not None:
                C.parent = A
            B.left = w
            if w is not None:
                w.parent = B
            B.right = x
            if x is not None:
                x.parent = B

        self.root = x
        x.parent = None

    def zig2(self, A):
        """
        Handles zig-zig and zig-zag caes
        """
        B, C, Cparent = A.parent, B.parent, C.parent
        

