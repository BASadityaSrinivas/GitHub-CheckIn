\\\
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
\\\

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        head1 = head
        head2 = Node(0)

        tempH1 = head1
        tempH2 = head2

        while tempH1:
            tempH2.next = Node(tempH1.val)
            tempH2 = tempH2.next
            tempH1 = tempH1.next
        
        head2 = head2.next
        h1 = head1
        h2 = head2

        while h1:
            randH1 = h1.random
            h1Trace = head1
            jumps = -1
            
            if randH1:
                while h1Trace:
                    if h1Trace == randH1:
                        jumps += 1
                        break
                    else:
                        jumps += 1
                        h1Trace = h1Trace.next
        
            h2Trace = head2
            h2Rand = None
            while jumps >= 0:
                h2Rand = h2Trace
                h2Trace = h2Trace.next
                jumps -= 1
            
            h2.random = h2Rand
        
            h1 = h1.next
            h2 = h2.next
        
        return head2