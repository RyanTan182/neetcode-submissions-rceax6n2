# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list2:
            return list1
        if not list1:
            return list2
        
        curr1 = list1
        curr2 = list2
        head3 = None

        if curr1.val < curr2.val:
            head3 = ListNode(curr1.val, None)
            curr1 = curr1.next
        else:
            head3 = ListNode(curr2.val, None)
            curr2 = curr2.next
        
        curr3 = head3

        while curr1 != None and curr2 != None:
            if curr1.val < curr2.val:
                curr3.next = ListNode(curr1.val, None)
                curr1 = curr1.next
                curr3 = curr3.next
            else:
                curr3.next = ListNode(curr2.val, None)
                curr2 = curr2.next
                curr3 = curr3.next
        
        if curr1 == None:
            curr3.next = curr2
        elif curr2 == None:
            curr3.next = curr1

        return head3


        