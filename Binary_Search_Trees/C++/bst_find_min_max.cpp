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

int find_min(BstNode* root){
	if(root == NULL){
		cout<<"Tree is empty!\n";
		return -1;
	}
	else if (root->left == NULL){
		return root->data;
	}
	return find_min(root->left);
}

int find_max(BstNode* root){
	if (root == NULL){
		cout<<"Tree is empty!\n";
		return -1;
	}
	else if (root->right == NULL){
		return root->data;
	}
	return find_max(root->right);
}

int main(){
	BstNode* root = NULL;
	root = Insert(root, 15);
	root = Insert(root, 10);
	root = Insert(root, 20);
	root = Insert(root, 25);
	root = Insert(root, 8);
	root = Insert(root, 12);

	cout<< "Min: " << find_min(root) << endl;
	cout<< "Max: " << find_max(root) << endl;
}