# Problem Description: https://practice.geeksforgeeks.org/problems/full-binary-tree/1

from collections import defaultdict


class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


class Tree:
    def __init__(self):
        self.root = None
        self.map_nodes = defaultdict(Node)

    def insert(self, parent, child, dir):
        if(not self.root):
            root_node = Node(parent)
            child_node = Node(child)
            if(dir == 'L'):
                root_node.left = child_node
            elif(dir == 'R'):
                root_node.right = child_node
            self.root = root_node
            self.map_nodes[parent] = root_node
            self.map_nodes[child] = child_node
            return

        parent_node = self.map_nodes[parent]
        child_node = Node(child)
        if(dir == 'L'):
            parent_node.left = child_node
        elif(dir == 'R'):
            parent_node.right = child_node
        self.map_nodes[child] = child_node
        return


def isFullTree(root):
    if(not root.left and not root.right):
        return(True)
    if(root.left and root.right):
        return(isFullTree(root.left) and isFullTree(root.right))
    return(False)


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = [x for x in input().split()]
        tree = Tree()

        for i in range(0, n, 3):
            tree.insert(int(a[i]), int(a[i+1]), a[i+2])

        if(isFullTree(tree.root)):
            print('1')
        else:
            print('0')
