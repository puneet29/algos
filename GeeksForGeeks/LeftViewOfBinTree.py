# Problem Description: https://practice.geeksforgeeks.org/problems/left-view-of-binary-tree/1

import atexit
import io
import sys
import queue
from collections import defaultdict

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None
        self.map_nodes = defaultdict(Node)

    def Insert(self, parent, child, dir):
        if self.root is None:
            root_node = Node(parent)
            child_node = Node(child)
            if dir == 'L':
                root_node.left = child_node
            else:
                root_node.right = child_node
            self.root = root_node
            self.map_nodes[parent] = root_node
            self.map_nodes[child] = child_node
            return
        parent_node = self.map_nodes[parent]
        child_node = Node(child)
        self.map_nodes[child] = child_node
        if dir == 'L':
            parent_node.left = child_node
        else:
            parent_node.right = child_node
        return


def LeftViewUtil(root, a, i):
    if(not root):
        return
    if(len(a) < i+1):
        a.append(root.data)
    if(root.left):
        LeftViewUtil(root.left, a, i+1)
    if(root.right):
        LeftViewUtil(root.right, a, i+1)


def LeftView(root):
    '''
    :param root: root of given tree.
    :return: print the left view of tree, dont print new line
    '''
    a = []
    LeftViewUtil(root, a, 0)
    print(' '.join(map(str, a)), end='')


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())  # number of nodes in tree
        # parent child info in list
        a = list(map(str, input().strip().split()))
        # construct the tree according to given list
        tree = Tree()
        i = 0
        while (i < len(a)):
            parent = int(a[i])
            child = int(a[i + 1])
            dir = a[i + 2]
            i += 3
            tree.Insert(parent, child, dir)  # Insert the nodes in tree.
        LeftView(tree.root)
        print()
