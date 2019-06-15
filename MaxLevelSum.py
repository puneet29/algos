# Problem Description: https://practice.geeksforgeeks.org/problems/max-level-sum-in-binary-tree/1

class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


class Tree:
    def createNode(self, data):
        return Node(data)

    def insert(self, node, data, ch):
        if node is None:
            return self.createNode(data)
        if (ch == 'L'):
            node.left = self.insert(node.left, data, ch)
            return node.left
        else:
            node.right = self.insert(node.right, data, ch)
            return node.right

    def search(self, lis, data):
        # if root is None or root is the search data.
        for i in lis:
            if i.data == data:
                return i


def maxLevelSum(root):
    if(not root):
        return(0)

    result = root.data
    q = []
    q.append(root)
    while(q != []):

        total = 0
        for _ in range(len(q)):
            temp = q[0]
            del q[0]

            total += temp.data

            if(temp.left):
                q.append(temp.left)
            if(temp.right):
                q.append(temp.right)

        result = max(total, result)
    return(result)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        if n == 0:
            print(1)
            continue
        tree = Tree()
        lis = []
        root = None
        root = tree.insert(root, int(arr[0]), 'L')
        lis.append(root)
        k = 0
        for j in range(n):
            ptr = None
            ptr = tree.search(lis, int(arr[k]))
            lis.append(tree.insert(ptr, int(arr[k+1]), arr[k+2]))
            k += 3
        print(maxLevelSum(root))
