# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast.next:
            if fast.next and fast.next.next == None:
                return slow.next
            elif fast.next == None:
                return slow
            
            slow = slow.next
            fast = fast.next.next
        return slow
            
