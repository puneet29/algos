# Problem Description: https://practice.geeksforgeeks.org/problems/rotate-a-linked-list/1


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print("")


def rotateList(head, k):
    i = 1
    newHead = None
    temp = head
    while(temp.next):
        if(i == k):
            newHead = temp.next
            temp.next = None
            temp = newHead
        else:
            temp = temp.next
        i += 1
    if(i > k):
        temp.next = head
    else:
        newHead = head
    return newHead


if __name__ == '__main__':
    start = LinkedList()
    t = int(input())
    while(t > 0):
        llist = LinkedList()
        n = int(input())
        values = list(map(int, input().strip().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = rotateList(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1
