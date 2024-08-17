# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # Solution 1 - Using recursion
        def recur(prev, cur, maxx):
            if not cur.next:
                return cur.val
            maxx = max(cur.val, recur(cur, cur.next, maxx))
            if cur.val < maxx:
                prev.next = cur.next
            return maxx

        dummy = ListNode(0, head)
        recur(dummy, dummy.next, 0)

        return dummy.next
        
        # # Solution 2 - Using Stack
        # stack = []
        # while head:
        #     while stack and stack[-1].val < head.val:
        #         stack.pop()

        #     stack.append(head)
        #     head = head.next
            
        # for node in range(len(stack)-1):
        #     stack[node].next = stack[node+1]
        
        # return stack[0]



