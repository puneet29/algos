# Problem Description: https://practice.geeksforgeeks.org/problems/check-for-balanced-tree/1/

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Height:
    def __init__(self):
        self.height = 0


def isBalancedUtil(root, height):
    if(not root):
        return True

    lh = Height()
    rh = Height()

    l = isBalancedUtil(root.left, lh)
    r = isBalancedUtil(root.right, rh)

    height.height = 1 + max(lh.height, rh.height)

    if(abs(lh.height-rh.height) < 2):
        return l and r
    return False


def isBalanced(root):
    height = Height()
    return isBalancedUtil(root, height)


if __name__ == '__main__':

    root = None
    t = int(input())
    for i in range(t):
        #root = None
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

        if isBalanced(root):
            print(1)
        else:
            print(0)
