class BTNode(object):
	"""
	Node object for basic binary tree structure.
	"""

	def __init__(self, data = None, parent = None):
		"""
		Implementing the tree where data can be an object.
		Should probably refactor to use key/value pairs
		for nodes.

		@return: node object
		"""
		self.data = data
		self.left = None
		self.right = None
		self.parent = parent

	def __str__(self):
		"""
		@return: string containing the node's data
		"""
		return str(self.data)

	def children_count(self):
		"""
		@return: number of children: 0, 1, 2
		"""
		count = 0
		if self.left:
			count += 1
		if self.right:
			count += 1
		return count