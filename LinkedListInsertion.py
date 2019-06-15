# Problem Description: https://practice.geeksforgeeks.org/problems/linked-list-insertion/1

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


def insertAtBeginning(a, value):
    newNode = Node(value)
    newNode.next = a.head
    a.head = newNode


def insertAtEnd(a, value):
    newNode = Node(value)

    if(a.head==None):
        a.head = newNode
        return
    
    temp = a.head
    while(temp.next):
        temp = temp.next
    temp.next = newNode


t = int(input())

for _ in range(t):
    n = int(input())
    ins = [int(x) for x in input().split()]
    linkList = LinkedList()
    for i in range(n):
        el = ins[2*i]
        cmd = ins[2*i+1]

        if(cmd == 1):
            insertAtEnd(linkList, el)
        else:
            insertAtBeginning(linkList, el)


    temp = linkList.head
    while(temp.next!=None):
        print(temp.data, end=" ")
        temp = temp.next
    print(temp.data, end=" ")
    print()
