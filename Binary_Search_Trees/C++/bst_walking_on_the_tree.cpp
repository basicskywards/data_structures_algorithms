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

void walking_on_the_tree_inorder(BstNode* root){
	if (root == NULL) return;
	walking_on_the_tree_inorder(root->left);
	cout << root->data;
	walking_on_the_tree_inorder(root->right);
}

void walking_on_the_tree_postorder(BstNode* root){
	if (root == NULL) return;
	walking_on_the_tree_postorder(root->left);
	walking_on_the_tree_postorder(root->right);
	cout << root->data;

}


int main(){
	BstNode* root = NULL;
	root = Insert(root, 1);
	root = Insert(root, 6);
	root = Insert(root, 4);
	root = Insert(root, 3);
	root = Insert(root, 2);
	root = Insert(root, 5);
	// root = Insert(root, 35);
	// root = Insert(root, 13);
	// root = Insert(root, 2);
	// root = Insert(root, 100);
	cout << "\nPreOrder Walk: ";
	walking_on_the_tree_preorder(root);
	cout << "\nInOrder Walk: ";
	walking_on_the_tree_inorder(root);
	cout << "\nPostOrder Walk: ";
	walking_on_the_tree_postorder(root);
}