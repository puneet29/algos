# Problem Description: https://practice.geeksforgeeks.org/problems/count-leaves-in-binary-tree/1/


class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


def countLeaves(root):
    if(not root):
        return 0
    if(not root.right and not root.left):
        return 1
    return countLeaves(root.right)+countLeaves(root.left)


if __name__ == '__main__':

    root = None
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = input().strip().split()
        if n == 0:
            print(0)
            continue
        dictTree = dict()

        for j in range(n):
            if arr[3*j] not in dictTree:
                dictTree[arr[3*j]] = Node(arr[3*j])
                parent = dictTree[arr[3*j]]
                if j is 0:
                    root = parent

            else:
                parent = dictTree[arr[3*j]]

            child = Node(arr[3*j+1])
            if (arr[3*j+2] == 'L'):
                parent.left = child
            else:
                parent.right = child
            dictTree[arr[3*j+1]] = child

        print(countLeaves(root))
