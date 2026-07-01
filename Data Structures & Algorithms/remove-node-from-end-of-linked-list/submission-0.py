# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        seen = []
        cur=head
        while cur: 
            seen.append(cur)
            cur=cur.next

        if n<len(seen):
            seen[len(seen)-n-1].next = seen[len(seen)-n].next
        
        elif n==len(seen):
            head=head.next

        else:
            head=None

        return head