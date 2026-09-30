# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        _, res = self.helper(root)
        return res
    
    def helper(self, root):
        if not root:
            return 0, True
        
        l, l_balanced = self.helper(root.left)
        r, r_balanced = self.helper(root.right)
        res = l_balanced and r_balanced and abs(r - l) <= 1

        return max(r, l) + 1, res
        

        
        
        
        