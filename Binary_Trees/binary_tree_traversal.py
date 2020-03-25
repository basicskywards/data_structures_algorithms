from binary_tree_base import Binary_Tree_Node

def tree_traversal(root):
	if root:
		# Preorder: Process the root before the traversals/walk of left and right children
		print('Preorder: %d' % root.data)
		tree_traversal(root.left)

		# Inorder: Process the root after ther traversal of left child and before the traversal of right child
		print('Inorder: %d' % root.data)
		tree_traversal(root.right)

		# Postorder: Process the root after the traversals of left and right children
		print('Postorder: %d' % root.data)
def main():
	#			3
	#		2		5
	#	1		  4   6

	# non symmetric test
	tree = Binary_Tree_Node(3)
	tree.left = Binary_Tree_Node(2)
	tree.left.left = Binary_Tree_Node(1)
	tree.right = Binary_Tree_Node(5)
	tree.right.right = Binary_Tree_Node(4)
	tree.right.left = Binary_Tree_Node(6)
	tree_traversal(tree)

if __name__ == '__main__':
	main()