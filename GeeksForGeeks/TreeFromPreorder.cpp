// Problem Description: https://practice.geeksforgeeks.org/problems/construct-tree-from-preorder-traversal/1

#include <bits/stdc++.h>

using namespace std;

struct Node
{
    int data;
    struct Node *left;
    struct Node *right;
};
struct Node *newNode(int data)
{
    Node *temp = new Node;
    temp->data = data;
    temp->left = NULL;
    temp->right = NULL;
    return temp;
}
void printInorder(struct Node *node)
{
    if (node == NULL)
        return;
    printInorder(node->left);
    cout << node->data << " ";
    printInorder(node->right);
}

struct Node *constructTree(int n, int pre[], char preLN[])
{
    Node *root = newNode(pre[0]);
    if (n == 1)
        return (NULL);

    stack<Node *> st;
    st.push(root);
    int i = 1;
    Node *temp = root;
    while (i < n)
    {
        Node *curr_node = newNode(pre[i]);
        if (preLN[i] == 'N')
        {
            if (temp->left == NULL)
            {
                temp->left = curr_node;
                temp = temp->left;
            }
            else
            {
                temp = st.top();
                st.pop();
                temp->right = curr_node;
                temp = curr_node;
            }
            st.push(curr_node);
        }
        else if (preLN[i] == 'L' && preLN[i - 1] == 'N')
        {
            temp->left = curr_node;
        }
        else if (preLN[i] == 'L')
        {
            temp = st.top();
            st.pop();
            temp->right = curr_node;
        }
        i++;
    }
    return (root);
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        Node *root = NULL;
        int n;
        cin >> n;
        int pre[n];
        char preLN[n];
        for (int i = 0; i < n; i++)
            cin >> pre[i];
        for (int i = 0; i < n; i++)
            cin >> preLN[i];
        root = constructTree(n, pre, preLN);
        printInorder(root);
        cout << endl;
    }
    return 0;
}