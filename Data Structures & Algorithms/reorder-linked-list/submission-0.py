# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        count = 0
        curr = head
        while curr != None:
            count += 1
            stack.append(curr.val)
            curr = curr.next
        
        curr = head

        idx = 0

        while idx != count - 1 and curr != None and curr.next != None:
            if idx % 2 == 0:
                new_node = ListNode(stack.pop(), None)
                prev_next = curr.next
                curr.next = new_node
                new_node.next = prev_next
            
            idx += 1
            curr = curr.next
        
        curr.next = None
        

        
        
        