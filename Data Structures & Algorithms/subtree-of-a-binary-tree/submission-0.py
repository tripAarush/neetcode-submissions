# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def subr(self, root, subRoot):
        if not root and not subRoot:
            return True
        elif not root or not subRoot or root.val != subRoot.val:
            return False
        return self.subr(root.left, subRoot.left) and self.subr(root.right, subRoot.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # have a function for checking same tree
        # loop through root until you see root = subroot and run func
        if not root or not subRoot:
            return False
        if root.val == subRoot.val:
            if self.subr(root, subRoot):
                return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)