# Problem Description: https://practice.geeksforgeeks.org/problems/mirror-tree/1

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


def inorderTraversalUtil(root):
    if root is None:
        return
    inorderTraversalUtil(root.left)
    print(root.data, end=' ')
    inorderTraversalUtil(root.right)


def inorderTraversal(root):
    inorderTraversalUtil(root)
    print()


def mirror(root):
    if(not root):
        return None
    
    mirror(root.left)
    mirror(root.right)

    root.right, root.left = root.left, root.right

    return(root)

if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        if n == 0:
            print(0)
            continue

        root = None
        dictTree = dict()

        for j in range(n):
            if arr[3*j] not in dictTree:
                dictTree[arr[3*j]] = Node(int(arr[3*j]))
                parent = dictTree[arr[3*j]]

                if j is 0:
                    root = parent
            else:
                parent = dictTree[arr[3*j]]

            child = Node(int(arr[3*j+1]))

            if(arr[3*j+2] == 'L'):
                parent.left = child
            else:
                parent.right = child
            dictTree[arr[3*j+1]] = child

        mirror(root)

        inorderTraversal(root)
