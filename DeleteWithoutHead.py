class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, new_value):
        new_node = Node(new_value)
        if(self.head is None):
            self.head = new_node
            return
        curr_node = self.head
        while(curr_node.next):
            curr_node = curr_node.next
        curr_node.next = new_node

    def getNode(self, value):
        curr_node = self.head
        while(curr_node.next and curr_node.data != value):
            curr_node = curr_node.next
        if(curr_node.data == value):
            return(curr_node)
        return(None)

    def printList(self):
        curr_node = self.head
        while(curr_node):
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print()


def deleteNode(node):
    curr_node = node
    if(curr_node):
        while(curr_node.next.next):
            curr_node.data = curr_node.next.data
            curr_node = curr_node.next
        curr_node.data = curr_node.next.data
        curr_node.next = None


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        linklist = LinkedList()
        nodes = [int(x) for x in input().split()]
        element = int(input())

        for i in nodes:
            linklist.append(i)

        node_to_delete = linklist.getNode(element)
        deleteNode(node_to_delete)
        linklist.printList()
