class Node:
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


def frontBackSplit(head):
    # Finding mid and getting two halves
    fast_pointer = head.next
    slow_pointer = head

    while(fast_pointer):
        fast_pointer = fast_pointer.next
        if(fast_pointer):
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next

    frontRef = head
    backRef = slow_pointer.next
    slow_pointer.next = None
    return(frontRef, backRef)


def sortedMerge(a, b):
    result = Node(None)

    if(not a):
        return(b)
    elif(not b):
        return(a)

    if(a.data <= b.data):
        result = a
        result.next = sortedMerge(a.next, b)
    else:
        result = b
        result.next = sortedMerge(a, b.next)
    return(result)


def mergeSort(headRef):
    head = headRef

    if((not head) or (not head.next)):
        return

    firstHalf, secondHalf = frontBackSplit(head)

    mergeSort(firstHalf)
    mergeSort(secondHalf)

    head = sortedMerge(firstHalf, secondHalf)
    return(head)


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]

        ll = LinkedList()
        for i in range(len(a)):
            ll.append(a[i])

        ll.head = mergeSort(ll.head)
        ll.printList()
