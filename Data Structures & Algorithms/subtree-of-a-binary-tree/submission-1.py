# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def check(self, node, copy):
        if not node and not copy:
            return True
        if not copy or not node:
            return False
        if node.val == copy.val and self.check(node.right, copy.right) and self.check(node.left, copy.left):
            return True
        
        return False
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if self.check(root, subRoot):
            return True
        
        if self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot):
            return True
        
        return False
        