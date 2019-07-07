# Problem Description: https://practice.geeksforgeeks.org/problems/detect-loop-in-linked-list/1

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
# Linked List Class


class LinkedList:
    def __init__(self):
        self.head = None
    # creates a new node with given value and appends it at the end of the linked list

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node
    # connects last node to node at position pos from begining.

    def add(self, pos):
        count = 0
        curr_node = self.head
        temp = None
        while curr_node.next:
            count += 1
            if(count == pos):
                temp = curr_node
            curr_node = curr_node.next
        curr_node.next = temp
        return


def detectLoop(head):
    seen = set()

    while(head):
        if(head in seen):
            return True
        else:
            seen.add(head)
        head = head.next
    return False


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList()  # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)
        loop = int(input())
        if(loop):
            a.add(loop)
        print(detectLoop(a.head))
