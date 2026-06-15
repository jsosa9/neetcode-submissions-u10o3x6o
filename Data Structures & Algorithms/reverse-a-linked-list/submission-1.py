# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        so we have 
        0 -> 1 -> 2 -> 3 -> 4
        and we wanwt 
        0 <- 1 <- 2 <- 3 <- 4
        
        so the whole point of this is to store the next value 
        take the next value and assign it to the prev 
        take the prev value assing it to the current 
        then iterate 

        overall take the current value assing it to prev 
        take the prev value and assing it to the next 
        """
        prev, curr = None, head
        while curr:
            # next is assigned to the next value
            nxt = curr.next 
            # the actual next value is assigned to the prev value 
            curr.next = prev
            # the prev is assinged the current value 
            prev = curr
            # we now move onto the next iteration 
            curr = nxt
        return prev

        