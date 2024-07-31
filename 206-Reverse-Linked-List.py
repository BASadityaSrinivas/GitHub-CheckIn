# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            cur = head.next
            head.next = None
            prev = head
            
            while cur:
                nextt = cur.next
                cur.next = prev
                prev = cur
                head = cur
                cur = nextt
            return head
        return head
        

        