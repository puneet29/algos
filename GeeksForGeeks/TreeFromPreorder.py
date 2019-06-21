# Problem Description: https://practice.geeksforgeeks.org/problems/construct-tree-from-preorder-traversal/1

class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


def printInorder(root):
    if(not root):
        return
    if(root.left):
        printInorder(root.left)
    print(root.data, end=" ")
    if(root.right):
        printInorder(root.right)


def constructTree(n, pre, preLN):
    root = Node(pre[0])
    if(n == 1):
        return root

    q = [root]
    i = 1
    temp = root
    while(i < n):
        curr_node = Node(pre[i])
        if(preLN[i] == 'N'):
            if(not temp.left):
                temp.left = curr_node
                temp = temp.left
            else:
                temp = q.pop()
                temp.right = curr_node
                temp = curr_node
            q.append(curr_node)
        elif(preLN[i] == 'L' and preLN[i-1] == 'N'):
            temp.left = curr_node
        elif(preLN[i] == 'L'):
            temp = q.pop()
            temp.right = curr_node
        i += 1

    return root


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        pre = [int(x) for x in input().split()]
        preLN = [x for x in input().split()]

        root = constructTree(n, pre, preLN)
        printInorder(root)
        print()
