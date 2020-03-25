from binary_tree_with_parent_base import Binary_Tree_Node
from binary_tree_traversal import tree_traversal
# Time & Space complexity O(n)

def binary_tree_rebuild(preorder, inorder):
	node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}

	def build_subtree(preorder_start, preorder_end, inorder_start, inorder_end):
		if preorder_end <= preorder_start or inorder_end <= inorder_start:
			return None 
		root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
		left_subtree_size = root_inorder_idx - inorder_start
		return Binary_Tree_Node(preorder[preorder_start],
								# recursively build the left subtree
								build_subtree(preorder_start + 1, preorder_start + 1 + left_subtree_size, inorder_start, root_inorder_idx),
								# recursively build the right subtree
								build_subtree(preorder_start + 1 + left_subtree_size, preorder_end, root_inorder_idx + 1, inorder_end))
	return build_subtree(0, len(preorder), 0, len(inorder))

def main():
	preorder = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	inorder = [3, 2, 5, 4, 1, 6, 7, 9, 8]
	print('preorder: ', preorder)
	print('inorder: ', inorder)
	print('\nrebuild binary_tree_rebuild resutls:')
	tree_traversal(binary_tree_rebuild(preorder, inorder))

if __name__ == '__main__':
	main()