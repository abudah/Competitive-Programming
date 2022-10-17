# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #first lets split the list into two
        if not head or not head.next :
            return head
        
        left=head
        right=self.getMid(head)
        temp=right.next
        right.next=None
        right=temp
        
        #sort the splitted lists from the two sides
        left=self.sortList(left)
        right=self.sortList(right)
        
        #finally merge the sorted lists
        return self.mergeSort(left,right)
    def getMid(self, head):
        slow,fast=head,head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    def mergeSort(self,left,right):
        tail=dummy=ListNode()
        while left and right:
            if left.val<right.val:
                tail.next=left
                left=left.next
            else:
                tail.next=right
                right=right.next
            tail=tail.next    
        if left:
            tail.next=left
        if right:
            tail.next=right
        return dummy.next