// Problem Description: https://practice.geeksforgeeks.org/problems/check-for-balanced-tree/1/

#include <bits/stdc++.h>
using namespace std;

struct Node
{
    int data;
    struct Node *left;
    struct Node *right;

    Node(int x)
    {
        data = x;
        left = right = NULL;
    }
};

bool isBalancedUtil(Node *root, int &height){
    if(!root){
        return true;
    }
    int lh = 0;
    int rh = 0;

    bool l = isBalancedUtil(root->left, lh);
    bool r = isBalancedUtil(root->right, rh);
    
    height = 1 + max(lh, rh);

    if(abs(lh-rh) < 2){
        return l && r;
    }
    return false;
}

bool isBalanced(Node *root)
{
    int height = 0;
    return isBalancedUtil(root, height);
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        map<int, Node *> m;
        int n;
        cin >> n;
        struct Node *root = NULL;
        struct Node *child;
        while (n--)
        {
            Node *parent;
            char lr;
            int n1, n2;
            cin >> n1 >> n2 >> lr;
            if (m.find(n1) == m.end())
            {
                parent = new Node(n1);
                m[n1] = parent;
                if (root == NULL)
                    root = parent;
            }
            else
                parent = m[n1];
            child = new Node(n2);
            if (lr == 'L')
                parent->left = child;
            else
                parent->right = child;
            m[n2] = child;
        }
        cout << isBalanced(root) << endl;
    }
    return 0;
}