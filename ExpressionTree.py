# Problem Description: https://practice.geeksforgeeks.org/problems/expression-tree/1

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def evalExpressionTree(root):
    if(not root):
        return(0)
    if(not root.right and not root.left):
        return(int(root.data))
    if(root.data == '*'):
        return(evalExpressionTree(root.left)*evalExpressionTree(root.right))
    if(root.data == '/'):
        return(evalExpressionTree(root.left)/evalExpressionTree(root.right))
    if(root.data == '+'):
        return(evalExpressionTree(root.left)+evalExpressionTree(root.right))
    if(root.data == '-'):
        return(evalExpressionTree(root.left)-evalExpressionTree(root.right))


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = input().strip().split()
        q = []
        p = 0
        root = Node(arr[p])
        q.append(root)
        p = 1
        while q != []:
            f = q.pop(0)
            l = Node(-1)
            r = Node(-1)
            if (p != n):
                l.data = arr[p]
                f.left = l
                p += 1
                l.left = l.right = None
                q.append(l)
            else:
                f.left = None
            if p != n:
                r.data = arr[p]
                f.right = r
                p += 1
                q.append(r)
                r.left = r.right = None
            else:
                f.right = None
        print(evalExpressionTree(root))
