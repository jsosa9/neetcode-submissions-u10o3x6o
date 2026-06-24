# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Find the middle of the linked list (fast/slow pointer — you already know this)
        Reverse the second half of the list (prev/curr pattern — you already know this too)
        Merge the two halves by alternating nodes (similar to merge two sorted lists) 
        """
        slow, fast = head, head 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow
        second_start = mid.next  # save second half first
        mid.next = None          # then cut
        prev, curr = None, second_start  # use saved reference
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        first = head 
        second = prev
        while second:
            # save next pointers before rewiring
            tmp1 = first.next
            tmp2 = second.next
            # weave
            first.next = second
            second.next = tmp1
            # advance both
            first = tmp1
            second = tmp2
                    




