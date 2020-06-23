
import random
import sys
from binary_tree_base import Binary_Tree_Node



def find_first_greater_than_k(tree, k):
    '''Time complexity O(h) & Space complexity O(1)'''
    subtree = tree
    candidate_temp = None
    while subtree:
        if subtree.data > k:
            # candidate_temp, subtree = subtree, tree.left
            candidate_temp = subtree # must update subtree  before assigning subtree = subtree.left 
            subtree = subtree.left
            # candidate_temp = subtree

        else:
            subtree = subtree.right
    return candidate_temp.data 

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

    x = find_first_greater_than_k(tree, 4)
    print('The 1st greater than 4 in BST: ', x)

if __name__ == '__main__':
	main()