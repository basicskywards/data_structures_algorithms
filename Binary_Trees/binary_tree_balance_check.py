# follow PEP8 coding style

from binary_tree_base import Binary_Tree_Node
import collections

def is_binary_tree_balanced(tree):
	status = collections.namedtuple(
		'status_balaced_height', ('balanced', 'height'))

	def check_balanced(tree):
		if not tree:
			return status(True, -1) # base case for recursive

		left_result = check_balanced(tree.left)
		if not left_result.balanced:
			return status(False, 0) # left subtree not balanced

		right_result = check_balanced(tree.right)
		if not right_result.balanced:
			return status(False, 0)


		is_balanced = abs(left_result.height - right_result.height) <= 1
		height = max(left_result.height, right_result.height) + 1
		return status(is_balanced, height)

	return check_balanced(tree).balanced

def main():
    #  balanced binary tree test
    #      3
    #    2   5
    #  1    4 6
    tree = Binary_Tree_Node(3)
    tree.left = Binary_Tree_Node(2)
    tree.left.left = Binary_Tree_Node(1)
    tree.right = Binary_Tree_Node(5)
    tree.right.left = Binary_Tree_Node(4)
    tree.right.right = Binary_Tree_Node(6)
    assert is_binary_tree_balanced(tree)
    print(is_binary_tree_balanced(tree))
    print(tree)
    # Non-balanced binary tree test.
    tree = Binary_Tree_Node(2)
    tree.left = Binary_Tree_Node(3)
    tree.left.left = Binary_Tree_Node(3)
    tree.left.left.left = Binary_Tree_Node(5)
    assert not is_binary_tree_balanced(tree)
    print(is_binary_tree_balanced(tree))
    print(tree)


if __name__ == '__main__':
    main()	