from binary_tree_base import Binary_Tree_Node

# Time complexity O(n)
# space complexity O(h)
# n: numbers of nodes
# h: height of tree

def is_symmetric(tree):
	def check_symmetric(subtree_0, subtree_1):
		if not subtree_0 and not subtree_1:
			return True 

		elif subtree_0 and subtree_1:
			return (subtree_0.data == subtree_1.data \
					and check_symmetric(subtree_0.left, subtree_1.right) \
					and check_symmetric(subtree_0.right, subtree_1.left))
		return False # one subtree is empty
	return not tree or check_symmetric(tree.left, tree.right)

def main():
	#			3
	#		2		5
	#	1		  4   6

	# non symmetric test
	tree = Binary_Tree_Node()
	tree.left = Binary_Tree_Node()
	tree.left.left = Binary_Tree_Node()
	tree.right = Binary_Tree_Node()
	tree.right.right = Binary_Tree_Node()
	tree.right.left = Binary_Tree_Node()
	print('Non symmetric binary tree test: ', is_symmetric(tree))

	# symmetric test
	tree = Binary_Tree_Node()
	tree.left = Binary_Tree_Node()
	tree.left.left = Binary_Tree_Node()
	tree.right = Binary_Tree_Node()
	tree.right.right = Binary_Tree_Node()
	print('Symmetric binary tree test: ', is_symmetric(tree))

if __name__ == '__main__':
	main()
