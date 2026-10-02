# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue, res = deque() , []
        queue.append(root)
        res.append([root.val])

        while queue:
            temp_list = []
            holding = []

            while queue:
                current = queue.popleft()

                if current.left:
                    temp_list.append(current.left.val)
                    holding.append(current.left)
                
                if current.right:
                    temp_list.append(current.right.val)
                    holding.append(current.right)

            if temp_list:
                res.append(temp_list)
                queue.extend(holding)

        return res

        