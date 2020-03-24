from binary_tree_with_parent_base import Binary_Tree_Node
from binary_tree_utils import binary_tree_to_string

# Time complexity O(h)
# Space complexity O(1)
# h: depth of tree

def lca(node_0, node_1):
	def get_depth(node):
		depth = 0
		while node:
			node = node.parent 
			depth += 1
		return depth

	depth_0, depth_1 = map(get_depth, (node_0, node_1))
	#depth_0, depth_1 = get_depth(node_0), get_depth(node_1)
	if depth_1 > depth_0:
		node_0, node_1 = node_1, node_0
		# assign node_0 as a deeper node for simplicity

	# ascend from the deeper node, to walk to the node that has the same depth with node_1
	depth_diff = abs(depth_0 - depth_1)
	while depth_diff:
		node_0 = node_0.parent
		depth_diff -= 1

	# ascend/walk upward both nodes until reaching LCA
	while node_0 is not node_1:
		node_0 = node_0.parent
		node_1 = node_1.parent

	return node_0.data #LCA data

def main():
	#		3
	#	2		6
	#1		  4   8

	root = Binary_Tree_Node(3)
	root.left = Binary_Tree_Node(2, None, None, root)
	root.left.left = Binary_Tree_Node(1, None, None, root.left)
	root.right = Binary_Tree_Node(6, None, None, root)
	root.right.left = Binary_Tree_Node(4, None, None, root.right)
	root.right.right = Binary_Tree_Node(8, None, None, root.right)

	#print(root)
	print(lca(root.right.right, root.left.left)) # return 3
	print(lca(root.left, root.right.left)) # return 3
	print(lca(root.right.left, root.right.right)) # return 6
	print(lca(root.right, root.right.right)) # return 6
if __name__ == '__main__':
		main()	