# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i, l))
        dummy = ListNode()
        cur = dummy
        while heap:
            val, i, node = heapq.heappop(heap)
            cur.next = node
            temp = node.next
            node.next = None
            cur = cur.next
            if temp:
                heapq.heappush(heap, (temp.val, i, temp))
        return dummy.next