# Problem Description: https://practice.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome/1/

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
# returns the size of linked list


def getSize(head):
    count = 0
    curr_node = head
    while curr_node:
        count += 1
        curr_node = curr_node.next
    return count


def isPalindrome(head):
    rev = ''
    s = ''

    while(head):
        s += str(head.data)
        rev = str(head.data) + rev
        head = head.next
    return 1 if(rev == s) else 0


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        n = int(input())
        a = LinkedList()  # create a new linked list 'a'.
        nodes_a = list(map(int, input().strip().split()))
        for x in nodes_a:
            a.append(x)  # add to the end of the list
        if isPalindrome(a.head):
            print(1)
        else:
            print(0)
