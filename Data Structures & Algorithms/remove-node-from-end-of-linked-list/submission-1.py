# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head

        while curr != None:
            count += 1
            curr = curr.next
        print("Count", count)
        idx_del = count - n
        curr = head
        print("Curr Value start", curr.val)
        if idx_del == 0:
            return head.next
        else:
            while curr != None and idx_del != 1:
                print("Heh")
                idx_del -= 1
                curr = curr.next
            print("Curr Value now", curr.val)

            curr.next = curr.next.next
            # curr.next.next = None

            return head
        
        