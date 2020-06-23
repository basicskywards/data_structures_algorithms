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

int find_height(BstNode* root){

	// Height of the BST is the number of edges from the root node to the furthest leaf.
	if (root == NULL){
		return -1;
	}

	int left_height = find_height(root->left);
	int right_height = find_height(root->right);

	cout << "Left height: " << left_height << endl;
	cout << "Right height: " << right_height << endl;
	return max(left_height, right_height) + 1;
}

int main(){
	BstNode* root = NULL;
	root = Insert(root, 15);
	root = Insert(root, 10);
	root = Insert(root, 20);
	root = Insert(root, 25);
	root = Insert(root, 8);
	root = Insert(root, 12);
	root = Insert(root, 35);
	root = Insert(root, 13);
	root = Insert(root, 2);
	root = Insert(root, 100);
	cout<< "Height of Tree: " << find_height(root) << endl;
}