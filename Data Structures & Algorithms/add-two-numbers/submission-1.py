# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = "", ""

        while l1:
            num1 += str(l1.val)
            l1 = l1.next

        while l2:
            num2 += str(l2.val)
            l2 = l2.next

        total = str(int(num1[::-1]) + int(num2[::-1]))
        
        res = None
        

        for i in total[::-1]:
            res = self.append(i, res)

        return res
    
    def append(self, new_data, res):
        new_node = ListNode(new_data)

        if res is None:
            res = new_node
            return res

        last = res
        while (last.next):
            last = last.next

        last.next =  new_node
        
        return res
