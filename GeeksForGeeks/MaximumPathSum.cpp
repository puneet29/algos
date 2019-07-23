// Problem Description: https://practice.geeksforgeeks.org/problems/maximum-path-sum/1/

#include <bits/stdc++.h>
using namespace std;

struct Node
{
    int data;
    Node *left, *right;
};

Node *newNode(int data)
{
    Node *node = new Node;
    node->data = data;
    node->left = node->right = NULL;
    return (node);
}

void insert(Node *root, int a1, int a2, char lr)
{
    if (root == NULL)
        return;
    if (root->data == a1)
    {
        switch (lr)
        {
        case 'L':
            root->left = newNode(a2);
            break;
        case 'R':
            root->right = newNode(a2);
            break;
        }
    }
    insert(root->left, a1, a2, lr);
    insert(root->right, a1, a2, lr);
}

void inorder(Node *root)
{
    if (root == NULL)
    {
        return;
    }
    inorder(root->left);
    cout << root->data << " ";
    inorder(root->right);
}

int maxPathSumUtil(Node *root, int &res)
{
    if (!root)
    {
        return 0;
    }
    if (!root->right && !root->left)
    {
        return root->data;
    }
    int ls = maxPathSumUtil(root->left, res);
    int rs = maxPathSumUtil(root->right, res);
    if (root->left && root->right)
    {
        res = max(res, root->data + ls + rs);
        return root->data + max(ls, rs);
    }
    if (root->left)
    {
        return ls + root->data;
    }
    else
    {
        return rs + root->data;
    }
}

int maxPathSum(struct Node *root)
{
    int res = INT_MIN;
    maxPathSumUtil(root, res);
    return res;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        Node *root = NULL;
        while (n--)
        {
            int a1, a2;
            char lr;
            cin >> a1 >> a2 >> lr;
            if (root == NULL)
            {
                root = newNode(a1);
                switch (lr)
                {
                case 'L':
                    root->left = newNode(a2);
                    break;
                case 'R':
                    root->right = newNode(a2);
                    break;
                }
            }
            else
                insert(root, a1, a2, lr);
        }
        //inorder(root);
        //cout<<endl;
        cout << maxPathSum(root) << endl;
    }
}