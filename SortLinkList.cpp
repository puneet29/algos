#include <iostream>

using namespace std;

struct Node
{
    int data;
    struct Node *next;
    Node(int x)
    {
        data = x;
        next = NULL;
    }
};

void printList(Node *node)
{
    while (node != NULL)
    {
        cout << node->data << " ";
        node = node->next;
    }
    cout << endl;
}

void push(struct Node **head_ref, int new_data)
{
    Node *new_node = new Node(new_data);
    new_node->next = (*head_ref);
    (*head_ref) = new_node;
}

void frontBackSplit(Node *head, Node **frontRef, Node **backRef)
{
    Node *slow_pointer = head;
    Node *fast_pointer = head->next;
    while (fast_pointer != NULL)
    {
        fast_pointer = fast_pointer->next;
        if (fast_pointer != NULL)
        {
            slow_pointer = slow_pointer->next;
            fast_pointer = fast_pointer->next;
        }
    }

    *frontRef = head;
    *backRef = slow_pointer->next;
    slow_pointer->next = NULL;
}

Node *sortedMerge(Node *first, Node *second)
{
    if (first == NULL)
    {
        return (second);
    }
    else if (second == NULL)
    {
        return (first);
    }

    Node *result = NULL;
    if (first->data <= second->data)
    {
        result = first;
        result->next = sortedMerge(first->next, second);
    }
    else
    {
        result = second;
        result->next = sortedMerge(first, second->next);
    }
    return (result);
}

Node *mergeSort(Node *head)
{
    Node *headRef = head;
    if ((headRef == NULL) || (headRef->next == NULL))
    {
        return headRef;
    }

    Node *a, *b;
    frontBackSplit(headRef, &a, &b);

    a = mergeSort(a);
    b = mergeSort(b);

    headRef = sortedMerge(a, b);
    return (headRef);
}

int main()
{
    long test;
    cin >> test;
    while (test--)
    {
        struct Node *a = NULL;
        long n, tmp;
        cin >> n;
        for (int i = 0; i < n; i++)
        {
            cin >> tmp;
            push(&a, tmp);
        }
        a = mergeSort(a);
        printList(a);
    }
    return 0;
}