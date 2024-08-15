# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        def recur(cur, val):
            if not cur or not cur.next:
                return
            
            if cur.next.val == val:
                cur.next = cur.next.next
                recur(cur, val)
            else:
                recur(cur.next, val)

        dummy = ListNode(0, head)
        recur(dummy, val)

        return dummy.next
