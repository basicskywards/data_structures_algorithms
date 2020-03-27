
import random
import sys
from binary_tree_base import Binary_Tree_Node

# naive time complexity O(n^2)
# time complexity O(n)
def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
	if not tree:
		return True
	elif not low_range <= tree.data <= high_range:
		return False
	return (is_binary_tree_bst(tree.left, low_range, tree.data)
		and is_binary_tree_bst(tree.right, tree.data, high_range))

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
    # should output True.
    print('\nResult: ', is_binary_tree_bst(tree))

        #      10
    #    2   5
    #  1    4 6
    tree.data = 10
    # should output False.
    print('\nResult: ', is_binary_tree_bst(tree))
if __name__ == '__main__':
	main()