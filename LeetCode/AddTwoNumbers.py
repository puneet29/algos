# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        carry = 0
        head_answer = node_pointer = ListNode()
        while l1 or l2 or carry:
            digit_1 = l1.val if l1 else 0
            digit_2 = l2.val if l2 else 0
            summed_num = digit_1 + digit_2 + carry
            remainder = summed_num % 10
            carry = summed_num // 10
            node_pointer.next = ListNode(val=remainder)
            node_pointer = node_pointer.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head_answer.next
