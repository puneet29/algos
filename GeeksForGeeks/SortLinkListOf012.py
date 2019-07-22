# Problem Description: https://practice.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1/

import atexit
import io
import sys
_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER
@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


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


def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end=" ")
        curr_node = curr_node.next
    print(' ')


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList()
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)
        printList(segregate(a.head))


def segregate(head):
    if(not head):
        return None

    zeros = None
    zeros_head = None
    ones = None
    ones_head = None
    twos = None
    twos_head = None

    while(head):
        if(head.data == 0):
            if(zeros == None):
                zeros = Node(head.data)
                zeros_head = zeros
            else:
                zeros.next = head
                zeros = zeros.next
        elif(head.data == 1):
            if(ones == None):
                ones = Node(head.data)
                ones_head = ones
            else:
                ones.next = head
                ones = ones.next
        else:
            if(twos == None):
                twos = Node(head.data)
                twos_head = twos
            else:
                twos.next = head
                twos = twos.next
        head = head.next

    newHead = None
    intLast = None
    if(zeros_head):
        newHead = zeros_head
        intLast = zeros
    if(ones_head):
        if(not newHead):
            newHead = ones_head
        elif(intLast):
            intLast.next = ones_head
        intLast = ones
    if(twos_head):
        if(not newHead):
            newHead = twos_head
        elif(intLast):
            intLast.next = twos_head
        intLast = twos
    intLast.next = None

    return newHead
