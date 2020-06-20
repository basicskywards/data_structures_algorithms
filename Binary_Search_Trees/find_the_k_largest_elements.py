import random
import os
from binary_tree_base import Binary_Tree_Node


def find_the_k_largest_in_bst(tree, k):

	def helper(tree):
		# Recursive!
		# Perform reverse inorder traversal!
		if tree and len(k_largest_values) < k:
			helper(tree.right) # Recursively traversal to the right nodes.
			if len(k_largest_values) < k:
				k_largest_values.append(tree.data)
				helper(tree.left)
				
	k_largest_values = []
	helper(tree)

	return k_largest_values

def main():
    #      3
    #    2   5
    #  1    4 6
    tree = Binary_Tree_Node(3)
    tree.left = Binary_Tree_Node(2)
    tree.left.left = Binary_Tree_Node(1)
    tree.right = Binary_Tree_Node(5)
    tree.right.left = Binary_Tree_Node(4)
    tree.right.right = Binary_Tree_Node(6)
   
    # tree.data = 10
    # should output False.
    # print(tree)

    k_largest_values = find_the_k_largest_in_bst(tree, 4)
    print('The k_largest_values in BST: ', k_largest_values)

if __name__ == '__main__':
	main()