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
        if not head:
            return None
        
        self_to_copy = {}

        def dfs(node):
            if not node:
                return
            if node in self_to_copy:
                return self_to_copy[node]
            
            copy = Node(node.val)
            self_to_copy[node] = copy

            copy.next = dfs(node.next)
            copy.random = dfs(node.random)
            return copy

        res = dfs(head)
        return res
            
        
            
        