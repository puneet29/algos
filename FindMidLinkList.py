class node:
    def __init__(self, val):
        self.data = val
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
        else:
            new_node = node(val)
            temp = self.head
            while(temp.next):
                temp = temp.next
            temp.next = new_node


def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head


def findMid(head):
    temp = head
    slow_pointer = head
    fast_pointer = head

    if(temp):
        while(fast_pointer and fast_pointer.next):
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next
    return(slow_pointer)


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]
        head = createList(arr, n)
        print(findMid(head).data)
