# Problem Description: https://practice.geeksforgeeks.org/problems/determine-if-two-trees-are-identical/1/

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


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


def isIdentical(root1, root2):
    if(not root1 and not root2):
        return True
    if(root1 and root2):
        return (root1.data == root2.data) and isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)
    return False


# Driver Program
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        tree = Tree()
        lis = []
        root1 = None
        root1 = tree.insert(root1, int(arr[0]), 'L')
        lis.append(root1)
        k = 0
        for j in range(n):
            ptr = None
            ptr = tree.search(lis, int(arr[k]))
            lis.append(tree.insert(ptr, int(arr[k+1]), arr[k+2]))
            k += 3
        n = int(input())
        arr = input().strip().split()
        tree = Tree()
        lis = []
        root2 = None
        root2 = tree.insert(root2, int(arr[0]), 'L')
        lis.append(root2)
        k = 0
        for j in range(n):
            ptr = None
            ptr = tree.search(lis, int(arr[k]))
            lis.append(tree.insert(ptr, int(arr[k+1]), arr[k+2]))
            k += 3
        if isIdentical(root1, root2):
            print(1)
        else:
            print(0)
