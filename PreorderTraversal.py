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


def preorder(root):
    if(not root):
        return
    print(root.data, end=" ")
    if(root.left):
        preorder(root.left)
    if(root.right):
        preorder(root.right)


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = [x for x in input().split()]
        tree = Tree()

        for i in range(0, len(a), 3):
            parent = a[i]
            child = a[i+1]
            dir = a[i+2]
            tree.insert(parent, child, dir)

        preorder(tree.root)
        print()
