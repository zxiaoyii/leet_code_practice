# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode | None) -> bool:
        if not head:
            return True
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # reverse
        cur = slow.next
        slow.next = None
        prev = None
        while cur:
            node = cur.next
            cur.next = prev
            prev = cur
            cur = node
        
        head1 = prev
        while head and head1:
            if head.val != head1.val:
                return False
            head = head.next
            head1 = head1.next
        return True