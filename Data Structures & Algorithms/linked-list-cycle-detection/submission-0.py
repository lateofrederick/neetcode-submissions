# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = set()
        current = head

        while current:
            if not current in s:
                s.add(current)
            else:
                return True
            current = current.next
        
        return False
