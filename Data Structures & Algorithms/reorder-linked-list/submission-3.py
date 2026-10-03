# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse_ll(self, head):
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        # reverse 2nd half of ll
        # if odd lengths, include middle in 2nd half
        # if even, keep middle in first half
        # in odd, fast = None, even fast.next = None
        # odd cases include slow points, even start slow.next

        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None

        second = self.reverse_ll(second)

        first = head
        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next

        


        