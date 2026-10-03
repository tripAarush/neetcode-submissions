# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        from collections import deque
        if not p and not q:
            return True
        if not p or not q:
            return False
        p_queue, q_queue = deque(), deque()
        p_queue.append(p)
        q_queue.append(q)

        while p_queue and q_queue:
            p_node = p_queue.popleft()
            q_node = q_queue.popleft()
            if p_node.val != q_node.val or not p_node.left and q_node.left or not p_node.right and q_node.right or not q_node.left and p_node.left or not q_node.right and p_node.right:
                return False

            if p_node.left:
                p_queue.append(p_node.left)
            if p_node.right:
                p_queue.append(p_node.right)

            if q_node.left:
                q_queue.append(q_node.left)
            if q_node.right:
                q_queue.append(q_node.right)
        
        if q_queue != p_queue:
            return False
        return True