# Problem Description: https://practice.geeksforgeeks.org/problems/merge-two-sorted-linked-lists/1/

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node

    def printList(self):
        if self.head is None:
            print(' ')
            return
        curr_node = self.head
        while curr_node:
            print(curr_node.data, end=" ")
            curr_node = curr_node.next
        print(' ')


def merge(head_a, head_b):
    s = None
    head = head_a

    while(head_a and head_b):
        if(head_a.data > head_b.data):
            temp = head_b
            s = head_b.data
            while(temp and head_a.data > temp.data):
                if(temp.next):
                    temp.data = temp.next.data
                prev = temp
                temp = temp.next
            prev.data = head_a.data
            head_a.data = s
        if(not head_a.next):
            last_a = head_a
        head_a = head_a.next
    last_a.next = head_b
    return head


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n, m = map(int, input().strip().split())
        a = LinkedList()
        b = LinkedList()
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)
        for x in nodes_b:
            b.append(x)
        a.head = merge(a.head, b.head)
        a.printList()
