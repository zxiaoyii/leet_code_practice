# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Only have one node
        if not head.next:
            return
        # Split from middle
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the right part
        prev = None
        cur = slow.next
        slow.next = None
        while cur:
            node = cur.next
            cur.next = prev
            prev = cur
            cur = node
        # Merge two list together
        while head and prev:
            node = head.next
            head.next = prev
            node1 = prev.next
            prev.next = node
            head = node
            prev = node1

          