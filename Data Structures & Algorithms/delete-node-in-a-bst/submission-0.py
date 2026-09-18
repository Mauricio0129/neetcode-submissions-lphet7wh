# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        else:
            if not (root.left and root.right):
                return root.left or root.right

            else:
                root.val = self.helper(root.left)
                root.left = self.deleteNode(root.left, root.val)
        
        return root
                
    
    def helper(self, root):
        while root and root.right:
            root = root.right
        return root.val

        