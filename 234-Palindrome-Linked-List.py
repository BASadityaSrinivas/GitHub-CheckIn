# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find mid
        sp = head
        fp = head

        while fp and fp.next:
            sp = sp.next
            fp = fp.next.next

        # Reverse from middle
        prev = None
        while sp:
            nextt = sp.next
            sp.next = prev
            prev = sp
            sp = nextt

        # Do palindrome check
        start = head
        end = prev

        while start and end:
            if start.val != end.val:
                return False
            start = start.next
            end = end.next

        return True
