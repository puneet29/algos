# Problem Description: https://practice.geeksforgeeks.org/problems/first-non-repeating-character-in-a-stream/0


class Node:
    def __init__(self, val=None, next_node=None, prev_node=None):
        self.data = val
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList:
    def __init__(self):
        self.start = Node()
        self.end = Node(None, None, self.start)
        self.start.next = self.end

    def addNode(self, val):
        temp = Node(val, self.end, self.end.prev)
        self.end.prev.next = temp
        self.end.prev = temp
        return temp

    def delNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        del node

    def getHead(self):
        if(self.start.next == self.end):
            return None
        return self.start.next.data


def findNonRep(a):
    DLL = DoublyLinkedList()
    links = {}
    repeated = set()

    for i in range(len(a)):
        c = a[i]
        if(c not in repeated):
            if(c not in links):
                n = DLL.addNode(c)
                links[c] = n
            else:
                repeated.add(c)
                DLL.delNode(links[c])
                del links[c]
        if(len(links) != 0):
            print(DLL.getHead(), end=' ')
        else:
            print(-1, end=' ')
    print()


t = int(input())

for _ in range(t):
    n = int(input())
    a = [x for x in input().split()]

    findNonRep(a)
