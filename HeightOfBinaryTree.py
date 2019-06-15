# Problem Description: https://practice.geeksforgeeks.org/problems/height-of-binary-tree/1

from collections import defaultdict


class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None


class Tree:
    def __init__(self):
        self.root = None
        self.map_nodes = defaultdict(None)

    def insert(self, parent, child, dir):
        if(self.root == None):
            root_node = Node(parent)
            child_node = Node(child)
            if(dir == 'L'):
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
        if(dir == 'L'):
            parent_node.left = child_node
        else:
            parent_node.right = child_node
        return


def height(root):
    if(not root):
        return(0)
    if(not root.right and not root.left):
        return(1)
    return(1 + max(height(root.left), height(root.right)))


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = [x for x in input().split()]
        tree = Tree()
        i = 0
        while(i < len(a)):
            parent = int(a[i])
            child = int(a[i+1])
            dir = a[i+2]
            i += 3
            tree.insert(parent, child, dir)
        print(height(tree.root))
