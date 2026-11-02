# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        # [1,2,3,4,5]
        # [1 -> 2 -> 3], curr=1, temp=2
        # [1 <- 2], curr=2, temp: 3
        # [1 <- 2 <- 3]
        # Imagining I have people in lines and they only know who is in "front" of them
        if head == None:
            return None 
            
        curr = head
        temp = curr.next
        head.next = None
        # link list all the way until there's nothing for us to link
        while temp != None:
            # First remember what is the next node
            nextNode = temp
            # Then, I need to update temp to be the next node of temp
            temp = temp.next
            # Then, I need to link the nextNode to the current node
            nextNode.next = curr
            # Finally I need to update the curr to be the iterated current node
            curr = nextNode
        return curr



