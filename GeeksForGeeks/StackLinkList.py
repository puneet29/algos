# Problem Description: https://practice.geeksforgeeks.org/problems/implement-stack-using-linked-list/1


class StackNode:
    # Constructor to initialize a node
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        if(not self.head):
            self.head = StackNode(data)
            self.top = self.head
            return
        temp = self.head
        self.head = StackNode(data)
        self.head.next = temp

    def pop(self):
        if(self.isEmpty()):
            return -1
        temp = self.head
        self.head = self.head.next
        return temp.data

    def isEmpty(self):
        if(not self.head):
            return True
        return False


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = Stack()
        q = int(input())
        q1 = list(map(int, input().split()))
        i = 0
        while(i < len(q1)):
            if(q1[i] == 1):
                s.push(q1[i + 1])
                i = i + 2
            elif(q1[i] == 2):
                print(s.pop(), end=" ")
                i = i + 1
            elif(s.isEmpty()):
                print(-1)
        print()
