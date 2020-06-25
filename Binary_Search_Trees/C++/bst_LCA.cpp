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

void lowest_common_ancestor(BstNode* root, int a, int b){
	// use recursive

	// Case 1: if a & b < root->data, then the LCA is on the left


	// Case 2 if a & b > root->data, then the LCA is on the right

	// Case 3: if a < root > b, then LCA = root

	//base case 
	if (root == NULL) return;
	if (root->data < a && root->data < b){
		lowest_common_ancestor(root->right, a, b);
	}

	else if (root->data > a && root->data > b){
		lowest_common_ancestor(root->left, a, b);
	}

	cout << root->data;
}

int main(){
	BstNode* root = NULL;
	root = Insert(root, 15);
	root = Insert(root, 10);
	root = Insert(root, 20);
	root = Insert(root, 25);
	root = Insert(root, 8);
	root = Insert(root, 12);
	root = Insert(root, 253);
	root = Insert(root, 2);
	root = Insert(root, 14);

	cout << "LCA of 2 and 25 is: ";
	lowest_common_ancestor(root, 2, 253);
	return 0;
}