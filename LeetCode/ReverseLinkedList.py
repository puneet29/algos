# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if(not head):
            return
        if(head.next == None):
            return head
        temp = head
        head = self.reverseList(head.next)
        temp.next.next = temp
        temp.next = None
        return head
