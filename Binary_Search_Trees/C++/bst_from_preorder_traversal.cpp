#include <iostream>
using namespace std;

/* A Binary Tree node */
// class TNode  
// {  
//     public: 
//     int data;  
//     TNode* left;  
//     TNode* right;  
// };  

struct BstNode
{
	int data;
	BstNode* left;
	BstNode* right;
	
};

BstNode* GetNewNode(int data){
	BstNode* newNode = new BstNode();
	newNode->data = data;
	newNode->right = newNode->left = NULL;
}

BstNode* Insert(BstNode* root, int data){
	if (root == NULL){//empty tree
		root = GetNewNode(data);
		// return root;
	}
	else if(data <= root->data){
		root->left = Insert(root->left, data);
	}
	else {
		root->right = Insert(root->right, data);
	}
	return root;
}

void walking_on_the_tree_preorder(BstNode* root){

	if (root == NULL) return;
		//PreOrder: root-left-right
	cout << root->data << " ";
	walking_on_the_tree_preorder(root->left);
	walking_on_the_tree_preorder(root->right);
		
}

// void walking_on_the_tree_inorder(BstNode* root){
// 	if (root == NULL) return;
// 	walking_on_the_tree_inorder(root->left);
// 	cout << root->data;
// 	walking_on_the_tree_inorder(root->right);
// }

// void walking_on_the_tree_postorder(BstNode* root){
// 	if (root == NULL) return;
// 	walking_on_the_tree_postorder(root->left);
// 	walking_on_the_tree_postorder(root->right);
// 	cout << root->data;

// }

BstNode* preorder_traversal_2_bst(int preorder[], int start, int end){
	//base case
	if (start > end) return NULL;

	//construc root node
	BstNode* root = GetNewNode(preorder[start]);

	// find the idx that have value is greater than root
	int idx;
	for (idx = start; idx <= end; idx++){
		if (preorder[idx] > root->data)
			break;
	}

	// recursive 
	root->right = preorder_traversal_2_bst(preorder, idx, end);
	root->left = preorder_traversal_2_bst(preorder, start + 1, idx - 1);

	return root;

}

int main(){
	/** Construct below BST
              15
            /    \
           /      \
          10       20
         /  \     /  \
        /    \   /    \
       8     12 16    25
	*/

	int preorder[] = {15, 10, 8, 12, 20, 16, 25};
	int n = sizeof(preorder)/sizeof(preorder[0]);
	BstNode* root = preorder_traversal_2_bst(preorder, 0, n -1);
	walking_on_the_tree_preorder(root);
	return 0;
}