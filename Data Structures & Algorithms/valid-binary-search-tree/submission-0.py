# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check(root, maxm = float('inf'), minm = -float('inf')):
            if not root:
                return True
            if not (root.val < maxm and root.val > minm):
                return False
            return check(root.left, maxm = root.val, minm = minm) and check(root.right, maxm = maxm, minm = root.val)
        
        return check(root)
        