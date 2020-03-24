from binary_tree_utils import binary_tree_to_string

class Binary_Tree_Node(object):
	"""docstring for Binary_Tree_Node"""
	def __init__(self, data=None, left=None, right=None, parent=None):
		#super(Binary_Tree_Node, self).__init__()
		self.data = data
		self.left = left
		self.right = right
		self.parent = parent

	def __repr__(self):
		return str(binary_tree_to_string(self))

	def __str__(self):
		return self.__repr__()