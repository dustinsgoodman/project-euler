"""
Implements a binary search tree.
Space: O(N)
"""

class BTNode(object):
    """
    Node object for a binary tree structure.
    """

    def __init__(self, parent, data = None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = parent

    def children_count(self):
        """
        Returns the number of children nodes

        @returns number of children: 0, 1, 2
        """
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count

class BinaryTree(object):
    """
    Implements ADT for a binary tree.
    """

    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, data, NodeType = BTNode):
        """
        Inserts new element into the tree.
        O(log(n))

        @return: inserted node      
        """
        self.count += 1

        if self.root is None:
            self.root = NodeType(None, data)
        else:
            current = self.root
            while True:
                if data < current.data:
                    if current.left is None:
                        current.left = NodeType(current, data)
                        return current.left
                    else:
                        current = current.left
                elif data > current.data:
                    if current.right is None:
                        current.right = NodeType(current, data)
                        return current.right
                    else:
                        current = current.right
                else:
                    return current

    def search(self, data):
        """
        Searches for data in tree. Returns node or None.
        O(log(n))

        @return: node matching search criteria
        """
        if self.root is None:
            return None
        else:
            current = self.root
            while True:
                if data == current.data:
                    return current
                elif data < current.data:
                    if current.left is None:
                        return None
                    else:
                        current = current.left
                elif data > current.data:
                    if current.right is None:
                        return None
                    else:
                        current = current.right

    def __remove_helper(self, node):
        """
        * Decrement total count of nodes in tree
        * Delete removed node object from memory

        @return: value of deleted node
        """
        self.count -= 1
        ret = node.data
        del node
        return ret

    def remove(self, data):
        """
        Removes data from tree if it exists and return data.
        O(log(n))

        @return: value of removed node
        """
        node = self.search(data)
        if node is None:
            return
        else:
            children_count = node.children_count()
            parent = node.parent
            if children_count == 0:
                if parent.left is node:
                    parent.left = None
                else:
                    parent.right = None
                return self.__remove_helper(node)
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
                return self.__remove_helper(node)
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
                return self.__remove_helper(node)

    def minimum(self, node):
        """
        @return: minimum of subtree rooted at node
        """
        if node is None:
            return None
        min_node = node
        while min_node.left:
            min_node = min_node.left
        return min_node

    def maximum(self, node):
        """
        @return: maximum of subtree rooted at node
        """
        if node is None:
            return None
        max_node = node
        while max_node.right:
            max_node = max_node.right
        return max_node

    def size(self):
        """
        @return: number of nodes in tree
        """
        return self.count

    def isEmpty(self):
        """
        @return: True if tree is empty, else false
        """
        return self.count == 0

    def isInternal(self, node):
        """
        @return: True if node is an internal node, else false
        """
        return not self.isExternal(node)

    def isExternal(self, node):
        """
        @return: True if node is an external/leaf node, else false
        """
        return node.left is None and node.right is None

    def isRoot(self, node):
        """
        @return: True if node is root node, else false
        """
        return node is self.root

    # equivalent to preorder
    def print_dfs(self):
        """
        Print a tree using depth first traversal from the given node.
        """
        stack = [self.root]
        while stack:
            node = stack.pop()
            print node.data
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)

    def print_bfs(self):
        """
        Print a tree using breadth first traversal from the given node.
        """
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            print node.data
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    def print_inorder(self, node):
        """
        Print a tree using inorder traversal from the given node.
        """
        if node is None:
            return
        self.print_inorder(node.left)
        print node.data
        self.print_inorder(node.right)

    # equivalent to dfs
    def print_preorder(self, node):
        """
        Print a tree using preorder traversal from the given node.
        """
        if node is None:
            return
        print node.data
        self.print_preorder(node.left)
        self.print_preorder(node.right)

    def print_postorder(self, node):
        """
        Print a tree using postorder traversal from the given node.
        """
        if node is None:
            return
        self.print_postorder(node.left)
        self.print_postorder(node.right)
        print node.data