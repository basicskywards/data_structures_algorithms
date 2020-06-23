#include <iostream>
using namespace std;

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
	cout << root->data;
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


// Find min by Recursive
BstNode* find_min(BstNode* root){
	if (root->left == NULL) return root; //return a pointer to the min node
	else find_min(root->left);
}

//Function to find minimum in a tree by While Loop
int FindMin(BstNode* root)
{
	while(root->left != NULL) root = root->left;
	return root->data; //return min value, not min node
}

// Recursive + Find Min + Pointer
BstNode* delete_a_value(BstNode* root, int data){
	if (root == NULL) return root;
	else if (data < root->data) root->left = delete_a_value(root->left, data);
	else if (data > root->data) root->right = delete_a_value(root->right, data);
	else{ //found data, go to delete it!
		//Case 1: no child
		if(root->left == NULL && root->right == NULL){
			delete root;
			root = NULL;
		}

		//Case 2: 1 child
		else if (root->left == NULL){
			BstNode* tmp = root;
			root = root->right;
			delete tmp;

		}
		else if (root->right == NULL){
			BstNode* tmp = root;
			root = root->left;
			delete tmp;

		}

		//Case 3: 2 child
		else {
			//find Min Node of the Right Subtree
			BstNode* tmp = find_min(root->right); //return Min Node of the right subtree
			// delete root;
			root->data = tmp->data;
			root->right = delete_a_value(root->right, tmp->data);
		}

	}

	return root;
}

int main(){
	BstNode* root = NULL;
	root = Insert(root, 1);
	root = Insert(root, 6);
	root = Insert(root, 4);
	root = Insert(root, 3);
	root = Insert(root, 2);
	root = Insert(root, 5);
	root = Insert(root, -1);
	root = Insert(root, 35);
	root = Insert(root, 13);
	root = Insert(root, 2);
	root = Insert(root, 100);
	cout <<"\nMin before delete min: " << FindMin(root);

	delete_a_value(root, FindMin(root)); // delete MIN
	cout <<"\nMin after delete min: " << FindMin(root) << endl;

}