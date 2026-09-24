"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #copy the node with val and next and insert
        cur = head
        while cur:
            node = Node(cur.val)
            node.next = cur.next
            cur.next = node 
            cur = node.next
        #copy random
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
        #split
        dummy = Node(0)
        p1, p2 = head, dummy
        while p1:
            p2.next = p1.next
            p2 = p2.next
            p1.next = p2.next
            p1 = p1.next
        
        return dummy.next



       