# Problem Description: https://practice.geeksforgeeks.org/problems/implement-queue-using-linked-list/1

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = MyQueue()
        q = int(input())
        q1 = list(map(int, input().split()))
        i = 0
        while(i < len(q1)):
            if(q1[i] == 1):
                s.push(q1[i+1])
                i = i+2
            elif(q1[i] == 2):
                print(s.pop(), end=" ")
                i = i+1
            elif(s.isEmpty()):
                print(-1)
                i = i+1
        print()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyQueue:

    def __init__(self):
        self.front = None
        self.rear = None

    # Method to add an item to the queue
    def push(self, item):
        if(not self.rear):
            self.rear = Node(item)
            self.front = self.rear
            return
        temp = Node(item)
        self.rear.next = temp
        self.rear = temp

    # Method to remove an item from queue
    def pop(self):
        if(not self.front):
            return -1
        temp = self.front
        if(self.front == self.rear):
            self.front = None
            self.rear = None
        else:
            self.front = self.front.next
        return temp.data
