# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        sett = set()
        sett.add(head)

        while head:
            head = head.next
            if head in sett:
                return True
            sett.add(head)
        
        return False



