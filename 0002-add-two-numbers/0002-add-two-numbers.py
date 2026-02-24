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
        dummy = ListNode() # result needs to be a ListNode
        curr = dummy # keeping track of the currrent position
        carry = 0 # keeping track of the carry for the next iteration

        while l1 or l2 or carry: #while these are not null
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # the addition part
            val = val1 + val2 + carry
            carry = val//10
            val = val % 10

            curr.next = ListNode(val)

            #iterating to the next value
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next

        