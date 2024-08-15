# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        \\\
        Do not return anything, modify head in-place instead.
        \\\
        # Find number of nodes
        temp = head
        n = 0
        while temp:
            temp = temp.next
            n += 1

        mid = n//2 + 1
        
        midNode = head
        while mid > 1:
            midNode = midNode.next
            mid -= 1

        nextToMidNode = midNode.next
        midNode.next = None

        # Reverse nextToMidNode until it's null
        prev = None
        runner = nextToMidNode

        while runner:
            nextt = runner.next
            runner.next = prev
            prev = runner
            runner = nextt

        secondPart = prev
        firstPart = head

        while secondPart:
            nextFP = firstPart.next
            firstPart.next = secondPart
            secondPart = secondPart.next    
            firstPart.next.next = nextFP
            firstPart = nextFP
        
        return head