# Problem Description: https://practice.geeksforgeeks.org/problems/array-to-bst/0


class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


def preorder(root):
    if(not root):
        return

    print(root.data, end=' ')
    preorder(root.left)
    preorder(root.right)


def arrToBST(a, low, high):
    if(low >= high):
        return None

    mid = low + (high-low)//2
    if((high-low) % 2 == 0):
        mid -= 1

    root = Node(a[mid])
    root.right = arrToBST(a, mid+1, high)
    root.left = arrToBST(a, low, mid)

    return root


t = int(input())

for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]

    root = arrToBST(a, 0, n)

    preorder(root)
    print()
