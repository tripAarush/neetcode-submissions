# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return head.next

        slow, fast = ListNode(), head
        slow.next = head

        for _ in range(n):
            fast = fast.next

        while fast:
            slow = slow.next
            fast = fast.next
        if slow.next == head:
            return slow.next.next
        slow.next = slow.next.next
        return head