# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # split the list

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow2 = slow.next
        prev = slow.next = None

        #reverse second half:
        while slow2:
            tmp = slow2.next
            slow2.next = prev
            prev = slow2
            slow2 = tmp
        
        # merge
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2









