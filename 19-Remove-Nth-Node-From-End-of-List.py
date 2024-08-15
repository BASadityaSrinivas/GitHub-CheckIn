# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        lenn = 0
        runner = head
        while runner:
            runner = runner.next
            lenn += 1

        jumps = lenn - n 

        if jumps == 0:
            return head.next
        else:
            runner = head
            while jumps > 1:
                runner = runner.next
                jumps -= 1
            runner.next = runner.next.next
        return head
            
