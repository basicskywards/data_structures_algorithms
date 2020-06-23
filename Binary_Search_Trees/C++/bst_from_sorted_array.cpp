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

BstNode* sorted_array_2_bst(int sorted_arr[],
								int start, int end){
	//base case
	if (start > end) return NULL;

	// get the middle of array
	int mid = (start + end) / 2;
	BstNode* root = GetNewNode(sorted_arr[mid]); //use mid value to be root 

	// recursive
	root->left = sorted_array_2_bst(sorted_arr, start, mid-1);
	root->right = sorted_array_2_bst(sorted_arr, mid+1, end);
	return root;
}


int main(){
	int arr[] = {1, 2, 3, 4, 5, 6, 7, 8};
	int n = sizeof(arr) / sizeof(arr[0]); //32/4 = 8

	// cout << "sizeof(arr[0]): " << sizeof(arr[0]) << endl;
	// cout << "sizeof(arr): " << sizeof(arr) << endl;
	BstNode* root = sorted_array_2_bst(arr, 0, n-1);
	walking_on_the_tree_preorder(root);

}