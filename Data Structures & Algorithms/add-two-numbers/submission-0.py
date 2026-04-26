# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0
        x = 0
        if l1 is not None:
            while l1 is not None:
                num1 += (l1.val * (10 ** x))
                x += 1
                l1 = l1.next
            x = 0
        if l2 is not None:
            while l2 is not None:
                num2 += (l2.val * (10 ** x))
                x += 1
                l2 = l2.next
        
        total = num1 + num2
        num_digits = len(str(abs(total)))
        l3 = ListNode()
        l3.val = (total // (10 ** 0)) % 10
        curr = l3
        
        for i in range(1, num_digits):
            print(i)
            new_node = ListNode()
            new_node.val = total // (10 ** i) % 10
            print(new_node.val)
            curr.next = new_node
            curr = new_node
        return l3




        
        