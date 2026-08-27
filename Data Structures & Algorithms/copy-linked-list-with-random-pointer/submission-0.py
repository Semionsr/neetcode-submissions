"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        checker = {None: None}
        first = head
        

        while first:
            copy = Node(first.val)
            checker[first] = copy
            first = first.next
        
        
        first = head
        while first:
            copy = checker[first]
            copy.next = checker[first.next]
            copy.random = checker[first.random]
            first = first.next



        
        return checker[head]