# Problem Description: partition a linked list around a value x,
# such that all nodes less than x come before all nodes greater
# than or equal to x


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


def appendNode(head, val):
    newNode = Node(val)
    while(head.next):
        head = head.next
    head.next = newNode


def partition(head, pivot):
    temp = head
    i = head
    while(temp):
        if(temp.data < pivot):
            temp.data, i.data = i.data, temp.data
            i = i.next
        temp = temp.next


if __name__ == "__main__":
    head = Node(3)
    appendNode(head, 5)
    appendNode(head, 8)
    appendNode(head, 5)
    appendNode(head, 10)
    appendNode(head, 2)
    appendNode(head, 1)

    partition(head, 3)

    while(head):
        print(head.data, end=' ')
        head = head.next
