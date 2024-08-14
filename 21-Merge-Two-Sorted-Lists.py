# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1:
            if list2:
                if list1.val > list2.val:
                    list1, list2 = list2, list1
            else:
                return list1
        else:
            return list2
        
        ogH1 = list1

        prevH1 = list1
        h1 = list1.next
        h2 = list2
        nextH2 = h2.next

        while h1 and h2:
            if h1.val >= h2.val:
                prevH1.next = h2
                nextH2 = h2.next
                h2.next = h1
                h2 = nextH2
                prevH1 = prevH1.next
            else:
                prevH1 = h1
                h1 = h1.next
        
        if h2:
            prevH1.next = h2

        return ogH1

