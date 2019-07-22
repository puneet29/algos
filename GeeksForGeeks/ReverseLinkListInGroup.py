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
        while (temp):
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()


def reverseUtil(head, k):
    stack = []
    i = 0

    while(head and i < k):
        stack.append(head)
        head = head.next
        i += 1

    nextNode = None
    newHead = None
    if(head):
        nextNode = head

    if(len(stack) > 0):
        newHead = stack.pop()
    temp = newHead

    while(len(stack) > 0):
        temp.next = stack.pop()
        temp = temp.next
    temp.next = None
    return newHead, nextNode, temp


def reverse(head, k):
    newHead = Node(None)
    temp = newHead
    while(head):
        temp.next, head, lastNode = reverseUtil(head, k)
        temp = lastNode

    return newHead.next


if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        new_head = reverse(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1
