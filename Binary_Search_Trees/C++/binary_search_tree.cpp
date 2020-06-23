#include <iostream>
using namespace std;


// Binary Search Tree
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

bool Search(BstNode* root, int data){
	if (root == NULL) return false;
	else if (root->data == data) return true;
	else if (root->data >= data) return Search(root->left, data);
	else return Search(root->right, data);

}

int main(int argc, char const *argv[])
{
	BstNode* root = NULL; // creat an empty tree
	root = Insert(root, 15);
	root = Insert(root, 10);
	root = Insert(root, 20);
	root = Insert(root, 25);
	root = Insert(root, 8);
	root = Insert(root, 12);
	int number;
	std::cout<<"Search number: \n";
	std::cin>>number;
	if (Search(root, number) == true) std::cout << "Found!\n";
	else std::cout << "Not found!\n";
	return 0;
}