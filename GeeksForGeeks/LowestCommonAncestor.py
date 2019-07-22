# Problem Description: https://practice.geeksforgeeks.org/problems/lowest-common-ancestor-in-a-bst/1/

import atexit
import io
import sys
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


class Node:
    def __init__(self, val):
        self.key = val
        self.left = None
        self.right = None


class BSTree:
    def __init__(self):
        self.root = None

    def Insert(self, x):
        if self.root is None:
            self.root = Node(x)
            return
        curr_node = self.root
        while curr_node:
            if curr_node.key < x:  # go to right subtree if value is more
                if curr_node.right is None:
                    break
                curr_node = curr_node.right
            elif curr_node.key > x:  # go to left subtree if value is more.
                if curr_node.left is None:
                    break
                curr_node = curr_node.left
            else:
                return  # no duplicate is to be inserted
        # insert key at the leaf position.
        if curr_node.key < x:
            curr_node.right = Node(x)
        else:
            curr_node.left = Node(x)


def LCA(root, n1, n2):
    '''
    :param root: given root of the bst
    :param n1: value one.
    :param n2: value two.
    :return: Lowest common Ancestor key.
    '''

    while(root):
        if(root.key > n1 and root.key > n2):
            root = root.left
        elif(root.key < n1 and root.key < n2):
            root = root.right
        else:
            break
    return root.key


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        # parent child info in list
        a = list(map(int, input().strip().split()))
        n1, n2 = map(int, input().strip().split())
        # construct the tree according to given list
        tree = BSTree()
        for value in a:
            tree.Insert(value)  # Insert the nodes in tree.
        print(LCA(tree.root, n1, n2))
