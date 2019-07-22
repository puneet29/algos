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


def reverse(head, k):
    stack = []
    i = 0

    temp = []
    while(head):
        temp.append(head)
        head = head.next
        i += 1
        if(i % k == 0):
            stack.append(temp)
            temp = []
    stack.append(temp)

    newHead = Node(None)
    temp = newHead

    for i in stack:
        for j in reversed(i):
            temp.next = j
            temp = temp.next
    temp.next = None
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
