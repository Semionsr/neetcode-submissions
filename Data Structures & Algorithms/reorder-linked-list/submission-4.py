# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head,head
        #get to the middle of the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #splitting the list
        new = slow.next
        slow.next = None
        prev = None

        
        #Flip second Linked List
        while new:
            tmp = new.next
            new.next = prev
            prev = new
            new = tmp

        #Merge lists:
        slow = head
        
        while prev:
            tmp1 = slow.next
            tmp2 = prev.next
            slow.next = prev
            prev.next = tmp1

            slow = tmp1
            prev = tmp2
        

        
