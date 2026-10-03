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
        if not head.next:
            return None
        # find midpoint using two pointer, reverse the second half
        fast = head
        slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        def reverse_llist(node):
            prev = None
            curr = node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        # half starts at slow.next
        rev_head = reverse_llist(slow.next)
        slow.next = None
        first, second = head, rev_head
        while second:
            f = first.next
            s = second.next

            first.next = second
            second.next = f

            first = f
            second = s