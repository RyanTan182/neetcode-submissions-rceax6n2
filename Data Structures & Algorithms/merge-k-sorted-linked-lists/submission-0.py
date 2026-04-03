# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []

        for i in range(len(lists)):
            curr = lists[i]
            while curr != None:
                print("Curr.val", curr.val)
                heapq.heappush(min_heap, curr.val)
                curr = curr.next
        
        if not min_heap:
            return None
        
        head = ListNode(heapq.heappop(min_heap), None)
        curr = head
        for j in range(len(min_heap)):
            new_node = ListNode(heapq.heappop(min_heap), None)
            curr.next = new_node
            curr = curr.next

        return head


        