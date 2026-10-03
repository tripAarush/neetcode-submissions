# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # breadth first search
        if not root:
            return []

        from collections import deque
        d = deque([root])
        res = []

        while d:
            level = []
            for i in range(len(d)):
                r = d.popleft()
                level.append(r.val)
                if r.left:
                    d.append(r.left)
                if r.right:
                    d.append(r.right)
            res.append(level)
        
        return res