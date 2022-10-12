# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first=head
        length=0
        while first:
            first=first.next
            length+=1
        curr=head
        for i in range(length):
            prev=curr
            curr=curr.next
            if length==n:
                    head=head.next
                    return head
            if i==length-(n+1):
                if curr:
                    prev.next=curr.next
                else:
                    prev.next=None
                return head
            
        