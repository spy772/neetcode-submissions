# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if head and head.next == head:
            return True
        
        p1, p2 = head, head.next

        while p1 and p2:
            if p1 == p2:
                return True

            p1 = p1.next
            p2 = p2.next
            if not p2 or not p2.next: # Found the end of the list
                return False
            p2 = p2.next # Go forward twice as fast as p1

        return False