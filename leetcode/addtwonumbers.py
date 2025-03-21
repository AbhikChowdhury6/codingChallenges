import math
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        idx = 0
        Sum = 0
        l1_head = l1
        l2_head = l2
        while (l1_head is not None) or (l2_head is not None):
            if l1_head is not None:
                Sum += l1_head.val*(10**idx)
                l1_head = l1_head.next
            if l2_head is not None:
                Sum += l2_head.val*(10**idx)    
                l2_head = l2_head.next
            idx +=1


        number = str(Sum)[::-1]
        nodes = [ListNode(int(c), None) for c in number]
        for i in range(len(number)-1):
            nodes[i].next = nodes[i+1]

        return nodes[0]