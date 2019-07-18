# Problem Description: https://practice.geeksforgeeks.org/problems/intersection-point-in-y-shapped-linked-lists/1

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

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            return
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = new_node


def intersetPoint(head_a, head_b):
    seen = set()

    while(head_a):
        seen.add(head_a)
        head_a = head_a.next

    while(head_b):
        if(head_b in seen):
            return head_b
        head_b = head_b.next

    return -1


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        x, y, z = map(int, input().strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        b = LinkedList()  # create a new linked list 'b'.
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        nodes_common = list(map(int, input().strip().split()))
        for x in nodes_a:
            node = Node(x)
            a.append(node)  # add to the end of the list
        for x in nodes_b:
            node = Node(x)
            b.append(node)  # add to the end of the list
        for i in range(len(nodes_common)):
            node = Node(nodes_common[i])
            a.append(node)  # add to the end of the list a
            if i == 0:
                # add to the end of the list b, only the intersection
                b.append(node)
        if intersetPoint(a.head, b.head) == -1:
            print(-1)
        else:
            # print data present at the node.
            print(intersetPoint(a.head, b.head).data)
