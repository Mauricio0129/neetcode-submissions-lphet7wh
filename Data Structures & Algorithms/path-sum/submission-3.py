# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.helper(root, targetSum, 0)
    
    def helper(self, root, targetSum, count):
        if not root:
            return False

        count += root.val

        if count == targetSum and not (root.left or root.right):
            return True
        
        elif self.helper(root.right, targetSum, count):
            return True

        elif self.helper(root.left, targetSum, count):
            return True
        
        return False
        
        




        



        
        