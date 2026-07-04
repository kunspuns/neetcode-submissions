# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1=l1
        cur2=l2
        carry_on = 0
        result = ListNode()
        head = result

        while cur1 or cur2:
            result.next = ListNode((carry_on + (cur1.val if cur1 else 0) + (cur2.val if cur2 else 0))%10 )
            carry_on = (carry_on + (cur1.val if cur1 else 0) + (cur2.val if cur2 else 0))//10
            if cur1: cur1 = cur1.next
            if cur2: cur2 = cur2.next
            result = result.next

        if carry_on != 0:
            result.next = ListNode(carry_on)
            result = result.next

        return head.next


            
            
        