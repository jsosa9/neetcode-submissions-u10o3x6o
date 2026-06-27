# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        find the middle 
        once we have the middle we reverse one half of it 
        once we reverse one half we merge both 
        """
        tail = head
        slow, fast = head, head
        # finding the middle once fast is None 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None
        # once fast is None 
        prev, curr = None, second
        while curr: 
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        while prev and head:
            nxtH = head.next
            nxtP = prev.next

            head.next = prev
            prev.next = nxtH

            head = nxtH
            prev = nxtP
