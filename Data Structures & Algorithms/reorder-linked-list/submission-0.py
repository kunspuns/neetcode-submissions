# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        seen = []
        top = -1 #keep track of last element of seen
        cur = head 
        bot = 0 #keep track of first element of seen
        dummy=ListNode()
        tail=dummy

        
        while cur:
            seen.append(cur)
            top += 1
            cur=cur.next

        while top>=bot:
            tail.next=seen[bot]
            tail=tail.next
            bot += 1

            if top>=bot:
                tail.next=seen[top]
                tail=tail.next
                top -= 1

        tail.next=None



        


        