# Problem Description: https://practice.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1

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

# Node Class


class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
# Linked List Class


class LinkedList:
    def __init__(self):
        self.head = None
    # creates a new node with given value and appends it at the end of the linked list

    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node
# prints the elements of linked list starting with head


def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data, end=" ")
        curr_node = curr_node.next
    print(' ')


def addBoth(head_a, head_b):
    sum_head = Node(0)
    carry = 0
    newHead = sum_head
    while(head_a and head_b):
        s = head_a.data + head_b.data + carry
        carry = s // 10
        s = s % 10
        sum_head.next = Node(s)
        head_a = head_a.next
        head_b = head_b.next
        sum_head = sum_head.next
    while(head_a):
        s = head_a.data + carry
        carry = s//10
        s = s % 10
        sum_head.next = Node(s)
        head_a = head_a.next
        sum_head = sum_head.next
    while(head_b):
        s = head_b.data + carry
        carry = s//10
        s = s % 10
        sum_head.next = Node(s)
        head_b = head_b.next
        sum_head = sum_head.next
    if(carry > 0):
        sum_head.next = Node(carry)

    return newHead.next


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n_a = int(input())
        a = LinkedList()  # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        nodes_a = nodes_a[::-1]  # reverse the input array
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        n_b = int(input())
        b = LinkedList()  # create a new linked list 'b'.
        nodes_b = list(map(int, input().strip().split()))
        nodes_b = nodes_b[::-1]  # reverse the input array
        for x in nodes_b:
            b.append(x)  # add to the end of the list
        result_head = addBoth(a.head, b.head)
        printList(result_head)
