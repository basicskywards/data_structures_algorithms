class Binary_Tree_Node:
	
	def __init__(self, data=None, left=None, right=None):
			self.data = data
			self.left = left
			self.right = right

	def __repr__(self):
		return '%s <- %s -> %s' %(self.left and self.left.data, self.data, self.right and self.right.data)
		
